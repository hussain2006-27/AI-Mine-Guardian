import random
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


# =========================================================
# SETTINGS
# =========================================================

print()
print("AI MINE GUARDIAN SENSOR SIMULATOR")
print("=" * 60)

print()
print("[1] SAFE")
print("[2] WARNING")
print("[3] DANGER")
print("[4] RANDOM")
print("[5] CUSTOM")
print()


# =========================================================
# SELECT MODE
# =========================================================

while True:

    mode = input("Enter mode (1-5): ").strip()

    if mode in ["1", "2", "3", "4", "5"]:
        break

    print("Please enter a number from 1 to 5.")


# =========================================================
# CUSTOM MODE
# =========================================================

custom_values = None

if mode == "5":

    print()
    print("CUSTOM SENSOR MODE")
    print("-" * 40)

    temperature = float(
        input("Temperature °C: ")
    )

    humidity = float(
        input("Humidity %: ")
    )

    mq4 = float(
        input("MQ-4 methane PPM: ")
    )

    mq9 = float(
        input("MQ-9 carbon monoxide PPM: ")
    )

    water = int(
        input("Water level %: ")
    )

    distance = float(
        input("Distance cm: ")
    )

    angle_x = float(
        input("Tilt X: ")
    )

    angle_y = float(
        input("Tilt Y: ")
    )

    custom_values = {
        "temperature": temperature,
        "humidity": humidity,
        "mq4": mq4,
        "mq9": mq9,
        "water": water,
        "distance": distance,
        "angle_x": angle_x,
        "angle_y": angle_y
    }


# =========================================================
# GENERATE SENSOR DATA
# =========================================================

def generate_sensor_data():

    # -----------------------------------------------------
    # SAFE
    # -----------------------------------------------------

    if mode == "1":

        temperature = round(
            random.uniform(24, 30), 2
        )

        humidity = round(
            random.uniform(45, 70), 2
        )

        mq4 = round(
            random.uniform(100, 500), 2
        )

        mq9 = round(
            random.uniform(100, 500), 2
        )

        water = random.randint(30, 70)

        distance = round(
            random.uniform(50, 150), 2
        )

        angle_x = round(
            random.uniform(0, 10), 2
        )

        angle_y = round(
            random.uniform(0, 10), 2
        )


    # -----------------------------------------------------
    # WARNING
    # -----------------------------------------------------

    elif mode == "2":

        temperature = round(
            random.uniform(46, 55), 2
        )

        humidity = round(
            random.uniform(55, 80), 2
        )

        mq4 = round(
            random.uniform(1100, 1500), 2
        )

        mq9 = round(
            random.uniform(500, 900), 2
        )

        water = random.randint(20, 60)

        distance = round(
            random.uniform(20, 50), 2
        )

        angle_x = round(
            random.uniform(10, 25), 2
        )

        angle_y = round(
            random.uniform(10, 25), 2
        )


    # -----------------------------------------------------
    # DANGER
    # -----------------------------------------------------

    elif mode == "3":

        temperature = round(
            random.uniform(55, 70), 2
        )

        humidity = round(
            random.uniform(70, 95), 2
        )

        mq4 = round(
            random.uniform(1500, 3000), 2
        )

        mq9 = round(
            random.uniform(1500, 3000), 2
        )

        water = random.randint(70, 100)

        distance = round(
            random.uniform(5, 14), 2
        )

        angle_x = round(
            random.uniform(30, 60), 2
        )

        angle_y = round(
            random.uniform(30, 60), 2
        )


    # -----------------------------------------------------
    # RANDOM
    # -----------------------------------------------------

    elif mode == "4":

        temperature = round(
            random.uniform(24, 70), 2
        )

        humidity = round(
            random.uniform(40, 95), 2
        )

        mq4 = round(
            random.uniform(100, 3000), 2
        )

        mq9 = round(
            random.uniform(100, 3000), 2
        )

        water = random.randint(0, 100)

        distance = round(
            random.uniform(5, 150), 2
        )

        angle_x = round(
            random.uniform(0, 60), 2
        )

        angle_y = round(
            random.uniform(0, 60), 2
        )


    # -----------------------------------------------------
    # CUSTOM
    # -----------------------------------------------------

    else:

        temperature = custom_values["temperature"]
        humidity = custom_values["humidity"]
        mq4 = custom_values["mq4"]
        mq9 = custom_values["mq9"]
        water = custom_values["water"]
        distance = custom_values["distance"]
        angle_x = custom_values["angle_x"]
        angle_y = custom_values["angle_y"]


    # =====================================================
    # RAW WATER ADC
    # =====================================================

    raw_water = int(
        water * 4095 / 100
    )


    # =====================================================
    # RISK CALCULATION
    #
    # Same four criteria as your ESP32:
    #
    # 1. Temperature
    # 2. MQ-4
    # 3. MQ-9
    # 4. Obstacle
    # =====================================================

    criteria_crossed = 0

    if temperature > 45:
        criteria_crossed += 1

    if mq4 > 1000:
        criteria_crossed += 1

    if mq9 > 1000:
        criteria_crossed += 1

    if distance > 0 and distance < 15:
        criteria_crossed += 1


    # =====================================================
    # STATUS
    # =====================================================

    if criteria_crossed > 2:

        status = "DANGER"

    elif criteria_crossed >= 1:

        status = "WARNING"

    else:

        status = "SAFE"


    # =====================================================
    # RISK SCORE
    # =====================================================

    score = criteria_crossed * 25


    # =====================================================
    # SENSOR JSON
    # =====================================================

    sensor_data = {

        "environment": {

            "temperature":
                temperature,

            "humidity":
                humidity

        },

        "gases": {

            "mq4_methane":
                mq4,

            "mq9_carbon_monoxide":
                mq9

        },

        "water": {

            "level":
                water,

            "raw":
                raw_water

        },

        "obstacle": {

            "distance":
                distance

        },

        "motion": {

            "angleX":
                angle_x,

            "angleY":
                angle_y,

            "status":
                "HIGH TILT"
                if angle_x > 45 or angle_y > 45
                else "NORMAL"

        },

        "timestamp":
            int(time.time())

    }


    # =====================================================
    # COMBINED RISK
    # =====================================================

    risk_data = {

        "level":
            status,

        "score":
            score,

        "criteriaCrossed":
            criteria_crossed,

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
                distance

        }

    }


    return sensor_data, risk_data


# =========================================================
# MAIN LOOP
# =========================================================

print()
print("Simulation started...")
print("Press Ctrl + C to stop.")
print("=" * 60)


try:

    while True:

        # -------------------------------------------------
        # Generate data
        # -------------------------------------------------

        sensor_data, risk_data = (
            generate_sensor_data()
        )


        # -------------------------------------------------
        # SEND SENSOR DATA
        # -------------------------------------------------

        db.reference(
            "sensors"
        ).set(
            sensor_data
        )


        # -------------------------------------------------
        # SEND RISK DATA
        # -------------------------------------------------

        db.reference(
            "combined_risk"
        ).set(
            risk_data
        )


        # -------------------------------------------------
        # DISPLAY
        # -------------------------------------------------

        print()
        print("SENSOR DATA SENT")
        print("-" * 60)

        print(
            f"Temperature : "
            f"{sensor_data['environment']['temperature']} °C"
        )

        print(
            f"Humidity    : "
            f"{sensor_data['environment']['humidity']} %"
        )

        print(
            f"MQ-4        : "
            f"{sensor_data['gases']['mq4_methane']} PPM"
        )

        print(
            f"MQ-9        : "
            f"{sensor_data['gases']['mq9_carbon_monoxide']} PPM"
        )

        print(
            f"Water       : "
            f"{sensor_data['water']['level']} %"
        )

        print(
            f"Distance    : "
            f"{sensor_data['obstacle']['distance']} cm"
        )

        print(
            f"Tilt X      : "
            f"{sensor_data['motion']['angleX']}°"
        )

        print(
            f"Tilt Y      : "
            f"{sensor_data['motion']['angleY']}°"
        )

        print()

        print(
            f"Criteria    : "
            f"{risk_data['criteriaCrossed']} / 4"
        )

        print(
            f"Risk Score  : "
            f"{risk_data['score']} / 100"
        )

        print(
            f"Status      : "
            f"{risk_data['level']}"
        )

        print("-" * 60)


        # -------------------------------------------------
        # WAIT
        # -------------------------------------------------

        time.sleep(3)


except KeyboardInterrupt:

    print()
    print("Sensor simulator stopped.")