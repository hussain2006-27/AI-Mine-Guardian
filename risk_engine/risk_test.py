import firebase_admin
from firebase_admin import credentials, db

# Connect to Firebase
cred = credentials.Certificate("firebase-service-account.json")

firebase_admin.initialize_app(cred, {
    "databaseURL": "https://ai-mine-guardian-default-rtdb.firebaseio.com"
})


def calculate_risk(sensor_data):

    environment = sensor_data.get("environment", {})
    gases = sensor_data.get("gases", {})

    temperature = environment.get("temperature", 0)
    mq4 = gases.get("mq4_methane", 0)
    mq7 = gases.get("mq7_carbon_monoxide", 0)

    risk_score = 0
    reasons = []

    if temperature >= 33:
        risk_score += 1
        reasons.append("High temperature")

    if mq4 >= 400:
        risk_score += 2
        reasons.append("High MQ-4 methane reading")

    if mq7 >= 400:
        risk_score += 2
        reasons.append("High MQ-7 carbon monoxide reading")

    if risk_score >= 4:
        risk_level = "DANGER"
    elif risk_score >= 2:
        risk_level = "WARNING"
    else:
        risk_level = "SAFE"

    return risk_level, risk_score, reasons


# Test scenarios
test_cases = {

    "SAFE": {
        "environment": {
            "temperature": 27,
            "humidity": 60,
            "pressure": 1005
        },
        "gases": {
            "mq4_methane": 150,
            "mq7_carbon_monoxide": 200
        }
    },

    "WARNING": {
        "environment": {
            "temperature": 30,
            "humidity": 65,
            "pressure": 1005
        },
        "gases": {
            "mq4_methane": 450,
            "mq7_carbon_monoxide": 200
        }
    },

    "DANGER": {
        "environment": {
            "temperature": 35,
            "humidity": 70,
            "pressure": 1005
        },
        "gases": {
            "mq4_methane": 450,
            "mq7_carbon_monoxide": 450
        }
    }
}


for name, data in test_cases.items():

    level, score, reasons = calculate_risk(data)

    print("\n" + "=" * 50)
    print("TEST:", name)
    print("Risk Level :", level)
    print("Risk Score :", score)
    print("Reasons    :", reasons)

print("\nRisk testing completed.")