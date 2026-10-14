
import cv2

aruco = cv2.aruco

dictionary = aruco.getPredefinedDictionary(
    aruco.DICT_4X4_50
)

detector = aruco.ArucoDetector(
    dictionary,
    aruco.DetectorParameters()
)

token_names = {
    0: "START",
    1: "OPEN",
    2: "WAIT",
    3: "PAUSE",
    4: "STOP",
}

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not open webcam.")
    raise SystemExit

print("Show a MatterOS token to the camera.")
print("Press Q to quit.")

while True:
    success, frame = camera.read()

    if not success:
        break

    corners, ids, rejected = detector.detectMarkers(frame)

    if ids is not None:
        aruco.drawDetectedMarkers(frame, corners, ids)

        for marker_id in ids.flatten():
            name = token_names.get(
                int(marker_id), "UNKNOWN"
            )
            print(f"Detected: {name} (ID {marker_id})")

    cv2.imshow("MatterOS - Token Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
