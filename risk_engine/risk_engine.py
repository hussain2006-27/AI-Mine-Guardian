import time

import firebase_admin
from firebase_admin import credentials, db


# =========================================================
# FIREBASE CONNECTION
# =========================================================

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


print()
print("🧠 AI Mine Guardian Risk Engine Started")
print("📡 Monitoring sensors + AI vision...")
print("🚨 Risk history enabled")
print("-" * 60)


# =========================================================
# VARIABLES
# =========================================================

last_risk_level = None


# =========================================================
# RISK CALCULATION
# =========================================================

def calculate_risk(sensor_data, vision_data=None):

    if vision_data is None:

        vision_data = {}


    # -----------------------------------------------------
    # SENSOR GROUPS
    # -----------------------------------------------------

    environment = sensor_data.get(
        "environment",
        {}
    )

    gases = sensor_data.get(
        "gases",
        {}
    )


    # -----------------------------------------------------
    # SENSOR VALUES
    # -----------------------------------------------------

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


    mq7 = float(
        gases.get(
            "mq7_carbon_monoxide",
            0
        )
    )


    # -----------------------------------------------------
    # AI VISION
    # -----------------------------------------------------

    workers_detected = int(
        vision_data.get(
            "workers_detected",
            0
        )
    )


    # =====================================================
    # RISK SCORE
    # =====================================================

    risk_score = 0

    reasons = []


    # =====================================================
    # TEMPERATURE
    # =====================================================

    if temperature >= 40:

        risk_score += 25

        reasons.append(
            "Critical temperature detected"
        )

    elif temperature >= 33:

        risk_score += 15

        reasons.append(
            "High temperature detected"
        )


    # =====================================================
    # MQ-4 METHANE
    # =====================================================

    if mq4 >= 700:

        risk_score += 35

        reasons.append(
            "Critical MQ-4 methane reading"
        )

    elif mq4 >= 400:

        risk_score += 25

        reasons.append(
            "High MQ-4 methane reading"
        )


    # =====================================================
    # MQ-7 CARBON MONOXIDE
    # =====================================================

    if mq7 >= 700:

        risk_score += 35

        reasons.append(
            "Critical MQ-7 carbon monoxide reading"
        )

    elif mq7 >= 400:

        risk_score += 25

        reasons.append(
            "High MQ-7 carbon monoxide reading"
        )


    # =====================================================
    # AI VISION
    # =====================================================

    if workers_detected > 0:

        risk_score += 20

        reasons.append(
            f"{workers_detected} worker(s) detected by AI vision"
        )


    # =====================================================
    # HUMIDITY
    # =====================================================

    if humidity >= 90:

        reasons.append(
            "Very high humidity detected"
        )


    # =====================================================
    # LIMIT SCORE
    # =====================================================

    risk_score = min(
        risk_score,
        100
    )


    # =====================================================
    # RISK LEVEL
    # =====================================================

    if risk_score >= 70:

        risk_level = "DANGER"

    elif risk_score >= 30:

        risk_level = "WARNING"

    else:

        risk_level = "SAFE"


    # =====================================================
    # RESULT
    # =====================================================

    return {

        "level":
            risk_level,

        "score":
            risk_score,

        "reasons":
            reasons,

        "inputs": {

            "temperature":
                temperature,

            "humidity":
                humidity,

            "mq4_methane":
                mq4,

            "mq7_carbon_monoxide":
                mq7,

            "workers_detected":
                workers_detected

        },

        "timestamp":
            int(time.time())

    }


# =========================================================
# SAVE RISK EVENT
# =========================================================

def save_risk_event(risk_result):

    history_ref = db.reference(
        "risk_history"
    )


    history_ref.push(
        risk_result
    )


    print(
        "📝 Risk event saved to Firebase."
    )


# =========================================================
# CONTINUOUS MONITORING
# =========================================================

while True:

    try:

        # -------------------------------------------------
        # READ SENSOR DATA
        # -------------------------------------------------

        sensor_data = (
            db.reference(
                "sensors"
            ).get()
        )


        # -------------------------------------------------
        # READ VISION DATA
        # -------------------------------------------------

        vision_data = (
            db.reference(
                "vision"
            ).get()
        )


        # -------------------------------------------------
        # CHECK DATA
        # -------------------------------------------------

        if sensor_data:

            # Calculate risk

            risk_result = calculate_risk(
                sensor_data,
                vision_data
            )


            # -------------------------------------------------
            # WRITE CURRENT RISK
            # -------------------------------------------------

            db.reference(
                "combined_risk"
            ).set(
                risk_result
            )


            # -------------------------------------------------
            # DETECT RISK CHANGE
            # -------------------------------------------------

            current_level = (
                risk_result["level"]
            )


            if (
                last_risk_level is None
                or current_level != last_risk_level
            ):

                save_risk_event(
                    risk_result
                )


                print(
                    f"🚨 RISK STATE CHANGED:"
                    f" {last_risk_level}"
                    f" → {current_level}"
                )


                last_risk_level = (
                    current_level
                )


            # -------------------------------------------------
            # TERMINAL OUTPUT
            # -------------------------------------------------

            print()

            print(
                "📡 Sensor data received"
            )


            print(
                f"🌡 Temperature: "
                f"{risk_result['inputs']['temperature']} °C"
            )


            print(
                f"🔥 MQ-4: "
                f"{risk_result['inputs']['mq4_methane']}"
            )


            print(
                f"☁ MQ-7: "
                f"{risk_result['inputs']['mq7_carbon_monoxide']}"
            )


            print(
                f"👷 Workers: "
                f"{risk_result['inputs']['workers_detected']}"
            )


            print()

            print(
                f"🧠 RISK LEVEL: "
                f"{risk_result['level']}"
            )


            print(
                f"📊 RISK SCORE: "
                f"{risk_result['score']}/100"
            )


            print(
                f"🚨 REASONS: "
                f"{risk_result['reasons']}"
            )


            print("-" * 60)


        else:

            print(
                "❌ No sensor data found"
            )


    except Exception as error:

        print()

        print(
            "❌ Risk Engine Error:"
        )

        print(
            error
        )

        print("-" * 60)


    # -----------------------------------------------------
    # WAIT
    # -----------------------------------------------------

    time.sleep(3)