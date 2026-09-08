import cv2


print("📷 Starting camera test...")
print("Press Q to quit.")


camera = cv2.VideoCapture(0)


if not camera.isOpened():

    print("❌ Could not open the camera.")

    print(
        "Check that your webcam is connected "
        "and not being used by another application."
    )

    exit()


print("✅ Camera opened successfully.")


while True:

    success, frame = camera.read()


    if not success:

        print("❌ Could not read camera frame.")

        break


    cv2.imshow(
        "AI Mine Guardian - Camera Test",
        frame
    )


    key = cv2.waitKey(1) & 0xFF


    if key == ord("q"):

        break


camera.release()

cv2.destroyAllWindows()

print("🛑 Camera test stopped.")