import cv2
import time
import firebase_admin

from ultralytics import YOLO
from firebase_admin import credentials, db


# =====================================================
# CONFIGURATION
# =====================================================

ESP32_CAM_IP = "10.1.57.237"

STREAM_URL = f"http://{ESP32_CAM_IP}/stream"

FIREBASE_URL = "https://ai-mine-guardian-default-rtdb.firebaseio.com"

MODEL_PATH = "yolo11n.pt"

# Minimum confidence for person detection
PERSON_CONFIDENCE = 0.40

# How often vision information is written to Firebase
FIREBASE_UPDATE_INTERVAL = 1.0


# =====================================================
# FIREBASE
# =====================================================

print()
print("==============================================")
print("       AI MINE GUARDIAN VISION")
print("==============================================")

print()
print("Connecting to Firebase...")

cred = credentials.Certificate(
    "firebase-service-account.json"
)

firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": FIREBASE_URL
    }
)

print("Firebase connected!")


# =====================================================
# LOAD YOLO
# =====================================================

print()
print("Loading YOLO model...")

model = YOLO(MODEL_PATH)

print("YOLO model loaded!")


# =====================================================
# CONNECT TO ESP32-CAM
# =====================================================

print()
print("Connecting to ESP32-CAM...")
print("Stream:", STREAM_URL)

cap = cv2.VideoCapture(STREAM_URL)

# Helps with some OpenCV/FFmpeg builds
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)


if not cap.isOpened():

    print()
    print("ERROR: Could not connect to ESP32-CAM.")
    print("Check the ESP32-CAM IP address.")
    print("Stream:", STREAM_URL)

    exit()


print("ESP32-CAM connected successfully!")


# =====================================================
# FIREBASE REFERENCE
# =====================================================

vision_ref = db.reference("vision")


# =====================================================
# VARIABLES
# =====================================================

last_firebase_update = 0

frame_count = 0


# =====================================================
# MAIN LOOP
# =====================================================

while True:

    ret, frame = cap.read()

    if not ret:

        print("Camera frame failed.")

        cap.release()

        time.sleep(2)

        cap = cv2.VideoCapture(STREAM_URL)

        continue


    frame_count += 1


    # =================================================
    # YOLO DETECTION
    # =================================================

    results = model(
        frame,
        verbose=False
    )


    workers_detected = 0

    highest_person_confidence = 0.0

    detected_objects = []


    # =================================================
    # PROCESS DETECTIONS
    # =================================================

    for result in results:

        if result.boxes is None:
            continue


        for box in result.boxes:

            class_id = int(
                box.cls[0]
            )

            confidence = float(
                box.conf[0]
            )

            class_name = model.names[
                class_id
            ]


            # -----------------------------------------
            # Store detected object
            # -----------------------------------------

            detected_objects.append(
                {
                    "object": class_name,
                    "confidence": round(
                        confidence,
                        2
                    )
                }
            )


            # -----------------------------------------
            # PERSON / WORKER
            # -----------------------------------------

            if (
                class_name == "person"
                and
                confidence >= PERSON_CONFIDENCE
            ):

                workers_detected += 1


                if (
                    confidence >
                    highest_person_confidence
                ):

                    highest_person_confidence = (
                        confidence
                    )


    # =================================================
    # CREATE VISION DATA
    # =================================================

    vision_data = {

        "workers_detected":
            workers_detected,

        "highest_person_confidence":
            round(
                highest_person_confidence,
                2
            ),

        "objects_detected":
            detected_objects,

        "model":
            "YOLO",

        "status":
            "active",

        "timestamp":
            int(time.time())

    }


    # =================================================
    # SEND TO FIREBASE
    # =================================================

    current_time = time.time()


    if (
        current_time -
        last_firebase_update
        >=
        FIREBASE_UPDATE_INTERVAL
    ):

        try:

            vision_ref.set(
                vision_data
            )

            last_firebase_update = (
                current_time
            )


        except Exception as e:

            print()
            print(
                "Firebase vision update error:",
                e
            )


    # =================================================
    # DISPLAY YOLO WINDOW
    # =================================================

    annotated_frame = results[0].plot()


    cv2.imshow(
        "AI Mine Guardian - YOLO",
        annotated_frame
    )


    # =================================================
    # TERMINATE
    # =================================================

    key = cv2.waitKey(1) & 0xFF


    if key == ord("q"):

        print()
        print("Stopping YOLO...")

        break


    # =================================================
    # CONSOLE STATUS
    # =================================================

    if frame_count % 30 == 0:

        print(
            f"Workers: {workers_detected} | "
            f"Objects: {len(detected_objects)}"
        )


# =====================================================
# CLEANUP
# =====================================================

cap.release()

cv2.destroyAllWindows()

print()
print("==============================================")
print("VISION SYSTEM STOPPED")
print("==============================================")