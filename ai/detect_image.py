from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolo11n.pt")

# Run detection
results = model("ai/test_images/test.jpg")

# Display detected objects
for result in results:

    print("\nDetected objects:")

    for box in result.boxes:

        class_id = int(box.cls[0])
        confidence = float(box.conf[0])

        class_name = model.names[class_id]

        print(
            f"{class_name} - "
            f"confidence: {confidence:.2f}"
        )

# Save the image with detections
results[0].save(filename="ai/test_images/detected.jpg")

print("\nDetection completed!")
print("Result saved as detected.jpg")