import time
import firebase_admin

from firebase_admin import credentials, db


# =====================================================
# FIREBASE
# =====================================================

FIREBASE_URL = (
    "https://ai-mine-guardian-default-rtdb.firebaseio.com"
)


cred = credentials.Certificate(
    "firebase-service-account.json"
)


firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": FIREBASE_URL
    }
)


# =====================================================
# REFERENCES
# =====================================================

sensors_ref = db.reference("sensors")

vision_ref = db.reference("vision")

combined_ref = db.reference("combined_risk")


# =====================================================
# THRESHOLDS
# =====================================================

MAX_TEMPERATURE = 45.0

MAX_MQ4 = 1000.0

MAX_MQ9 = 1000.0

MIN_DISTANCE = 15.0


# =====================================================
# ENGINE
# =====================================================

print()
print("==============================================")
print("      AI MINE GUARDIAN RISK ENGINE")
print("==============================================")

print()
print("Risk engine started.")
print("Waiting for sensor + vision data...")


# =====================================================
# MAIN LOOP
# =====================================================

while True:

    try:

        # =================================================
        # READ SENSOR DATA
        # =================================================

        sensor_data = sensors_ref.get()


        if sensor_data is None:

            print(
                "Waiting for sensor data..."
            )

            time.sleep(1)

            continue


        environment = sensor_data.get(
            "environment",
            {}
        )


        gases = sensor_data.get(
            "gases",
            {}
        )


        obstacle = sensor_data.get(
            "obstacle",
            {}
        )


        # =================================================
        # SENSOR VALUES
        # =================================================

        temperature = float(
            environment.get(
                "temperature",
                0
            )
        )


        humidity = float(
            environment.get(
                "humidity",
                0
            )
        )


        mq4 = float(
            gases.get(
                "mq4_methane",
                0
            )
        )


        # IMPORTANT:
        # Your ESP32 currently sends MQ-9
        # as mq9_carbon_monoxide

        mq9 = float(
            gases.get(
                "mq9_carbon_monoxide",
                0
            )
        )


        distance = float(
            obstacle.get(
                "distance",
                999
            )
        )


        # =================================================
        # READ VISION DATA
        # =================================================

        vision_data = vision_ref.get()


        if vision_data is None:

            vision_data = {}


        workers_detected = int(
            vision_data.get(
                "workers_detected",
                0
            )
        )


        highest_person_confidence = float(
            vision_data.get(
                "highest_person_confidence",
                0
            )
        )


        # =================================================
        # RISK CRITERIA
        # =================================================

        criteria_crossed = 0

        reasons = []


        # =================================================
        # 1. TEMPERATURE
        # =================================================

        if temperature > MAX_TEMPERATURE:

            criteria_crossed += 1

            reasons.append(
                "High temperature"
            )


        # =================================================
        # 2. MQ-4 METHANE
        # =================================================

        if mq4 > MAX_MQ4:

            criteria_crossed += 1

            reasons.append(
                "High MQ-4 methane reading"
            )


        # =================================================
        # 3. MQ-9 CARBON MONOXIDE
        # =================================================

        if mq9 > MAX_MQ9:

            criteria_crossed += 1

            reasons.append(
                "High MQ-9 carbon monoxide reading"
            )


        # =================================================
        # 4. OBSTACLE
        # =================================================

        if (
            distance > 0
            and
            distance < MIN_DISTANCE
        ):

            criteria_crossed += 1

            reasons.append(
                "Obstacle detected too close"
            )


        # =================================================
        # OVERALL RISK
        # =================================================

        if criteria_crossed > 2:

            risk_level = "DANGER"


        elif criteria_crossed >= 1:

            risk_level = "WARNING"


        else:

            risk_level = "SAFE"


        # =================================================
        # VISION INFORMATION
        # =================================================

        if workers_detected > 0:

            vision_reason = (
                f"{workers_detected} worker(s) "
                f"detected by AI vision"
            )

        else:

            vision_reason = (
                "No workers detected"
            )


        # =================================================
        # CREATE RESULT
        # =================================================

        combined_result = {

            "level":
                risk_level,

            "score":
                criteria_crossed,

            "criteriaCrossed":
                criteria_crossed,

            "maxCriteria":
                4,

            "reasons":
                reasons,

            "inputs": {

                "temperature":
                    temperature,

                "humidity":
                    humidity,

                "mq4_methane":
                    mq4,

                "mq9_carbon_monoxide":
                    mq9,

                "distance":
                    distance,

                "workers_detected":
                    workers_detected,

                "person_confidence":
                    highest_person_confidence

            },

            "vision": {

                "workers_detected":
                    workers_detected,

                "highest_person_confidence":
                    highest_person_confidence,

                "status":
                    vision_data.get(
                        "status",
                        "unknown"
                    )

            },

            "timestamp":
                int(time.time())

        }


        # =================================================
        # SEND TO FIREBASE
        # =================================================

        combined_ref.set(
            combined_result
        )


        # =================================================
        # CONSOLE
        # =================================================

        print()
        print(
            "=============================================="
        )

        print(
            "       COMBINED MINE RISK"
        )

        print(
            "=============================================="
        )

        print(
            f"Temperature : {temperature:.2f} °C"
        )

        print(
            f"MQ-4       : {mq4:.2f} PPM"
        )

        print(
            f"MQ-9       : {mq9:.2f} PPM"
        )

        print(
            f"Distance   : {distance:.2f} cm"
        )

        print(
            f"Workers    : {workers_detected}"
        )

        print(
            f"Criteria   : "
            f"{criteria_crossed} / 4"
        )

        print(
            f"STATUS     : {risk_level}"
        )

        print(
            "=============================================="
        )


    except Exception as e:

        print()
        print(
            "Risk engine error:",
            e
        )


    # =================================================
    # UPDATE RATE
    # =================================================

    time.sleep(1)