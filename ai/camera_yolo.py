import time

import cv2
from ultralytics import YOLO

import firebase_admin
from firebase_admin import credentials, db


# =========================================================
# FIREBASE CONNECTION
# =========================================================

print("🔥 Connecting to Firebase...")

cred = credentials.Certificate(
    "firebase-service-account.json"
)

firebase_admin.initialize_app(
    cred,
    {
        "databaseURL":
            "https://ai-mine-guardian-default-rtdb.firebaseio.com"
    }
)

print("✅ Firebase connected.")


# =========================================================
# LOAD YOLO
# =========================================================

print("🧠 Loading YOLO model...")

model = YOLO(
    "yolo11n.pt"
)

print("✅ YOLO model loaded successfully.")


# =========================================================
# OPEN CAMERA
# =========================================================

print("📷 Starting camera...")

camera = cv2.VideoCapture(0)


if not camera.isOpened():

    print("❌ Could not open camera.")

    exit()


print("✅ Camera opened successfully.")

print()
print("🚀 AI Mine Guardian Vision System Started")
print("👁 Detecting workers...")
print("🔥 Sending vision data to Firebase...")
print("Press Q to stop.")
print("-" * 60)


# =========================================================
# CAMERA LOOP
# =========================================================

try:

    while True:

        # -------------------------------------------------
        # READ FRAME
        # -------------------------------------------------

        success, frame = camera.read()


        if not success:

            print(
                "❌ Could not read camera frame."
            )

            break


        # -------------------------------------------------
        # YOLO DETECTION
        # -------------------------------------------------

        results = model(
            frame,
            verbose=False
        )


        # -------------------------------------------------
        # COUNT PEOPLE
        # -------------------------------------------------

        workers_detected = 0


        for box in results[0].boxes:

            class_id = int(
                box.cls[0]
            )


            class_name = model.names[
                class_id
            ]


            if class_name == "person":

                workers_detected += 1


        # -------------------------------------------------
        # CREATE VISION DATA
        # -------------------------------------------------

        vision_data = {

            "workers_detected":
                workers_detected,

            "model":
                "YOLO",

            "status":
                "active",

            "timestamp":
                int(time.time())

        }


        # -------------------------------------------------
        # SEND TO FIREBASE
        # -------------------------------------------------

        db.reference(
            "vision"
        ).set(
            vision_data
        )


        # -------------------------------------------------
        # DRAW YOLO RESULTS
        # -------------------------------------------------

        annotated_frame = (
            results[0].plot()
        )


        # -------------------------------------------------
        # DISPLAY WORKER COUNT
        # -------------------------------------------------

        cv2.putText(

            annotated_frame,

            f"Workers detected: {workers_detected}",

            (20, 40),

            cv2.FONT_HERSHEY_SIMPLEX,

            1,

            (0, 255, 0),

            2

        )


        # -------------------------------------------------
        # DISPLAY FIREBASE STATUS
        # -------------------------------------------------

        cv2.putText(

            annotated_frame,

            "Firebase: ONLINE",

            (20, 80),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.7,

            (0, 255, 0),

            2

        )


        # -------------------------------------------------
        # SHOW WINDOW
        # -------------------------------------------------

        cv2.imshow(

            "AI Mine Guardian - Vision",

            annotated_frame

        )


        # -------------------------------------------------
        # TERMINAL OUTPUT
        # -------------------------------------------------

        print(
            f"👷 Workers detected: "
            f"{workers_detected}"
        )

        print(
            "🔥 Firebase /vision updated"
        )

        print("-" * 60)


        # -------------------------------------------------
        # QUIT
        # -------------------------------------------------

        key = cv2.waitKey(1) & 0xFF


        if key == ord("q"):

            break


except KeyboardInterrupt:

    print()
    print(
        "🛑 Vision system interrupted."
    )


finally:

    # -----------------------------------------------------
    # CAMERA CLEANUP
    # -----------------------------------------------------

    camera.release()

    cv2.destroyAllWindows()


    print()
    print(
        "📷 Camera released."
    )

    print(
        "👁 Vision system stopped."
    )