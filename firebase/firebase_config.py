import firebase_admin
from firebase_admin import credentials, db

# Load Firebase credentials
cred = credentials.Certificate("firebase-service-account.json")

# Connect to Firebase
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://ai-mine-guardian-default-rtdb.firebaseio.com"
})

# Test data
test_data = {
    "status": "online",
    "message": "AI Mine Guardian connected"
}

# Write data to Firebase
db.reference("test").set(test_data)

print("Data successfully written to Firebase!")