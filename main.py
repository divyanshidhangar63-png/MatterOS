

import cv2
import subprocess
import time

# MatterOS marker setup
aruco = cv2.aruco
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
detector = aruco.ArucoDetector(
    dictionary, aruco.DetectorParameters()
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
    print("Error: Could not open webcam.")
    raise SystemExit

def read_workflow(frame):
    """Detect markers and return them in left-to-right order."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, rejected = detector.detectMarkers(gray)

    cards = []

    if ids is not None:
        for corner, marker_id in zip(corners, ids.flatten()):
            marker_id = int(marker_id)

            if marker_id not in token_names:
                continue

            points = corner[0]
            center_x = int(points[:, 0].mean())
            center_y = int(points[:, 1].mean())

            cards.append((center_x, marker_id, center_y))
            cv2.polylines(
                frame, [points.astype(int)], True,
                (0, 220, 0), 3
            )

            cv2.putText(
                frame, token_names[marker_id],
                (center_x - 45, center_y - 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (0, 220, 0), 2
            )

    cards.sort(key=lambda item: item[0])
    return [card[1] for card in cards]

def execute_workflow(workflow):
    """Execute only predefined, safe MatterOS actions."""
    if not workflow or workflow[0] != 0:
        print("Workflow must begin with START.")
        return

    if 4 not in workflow:
        print("Workflow must include STOP.")
        return

    stop_index = workflow.index(4)
    commands = workflow[1:stop_index]

    print("Executing MatterOS workflow...")

    for command_id in commands:
        command = token_names[command_id]
        print(f"Running: {command}")

        if command == "OPEN":
            # Predefined application; no arbitrary shell commands.
            subprocess.Popen(["notepad.exe"])

        elif command == "WAIT":
            time.sleep(5)

        elif command == "PAUSE":
            print("Paused. Press SPACE in the MatterOS window to resume.")
            while True:
                key = cv2.waitKey(0) & 0xFF
                if key == ord(" "):
                    break
                if key == ord("q"):
                    print("Workflow cancelled.")
                    return

        elif command == "START":
            continue

    print("MatterOS workflow finished.")

print("MatterOS workflow reader started.")
print("Arrange cards in a row, then press E to execute.")
print("Press Q to quit.")

while True:
    success, frame = camera.read()

    if not success:
        print("Could not read from webcam.")
        break

    workflow = read_workflow(frame)

    names = [token_names[i] for i in workflow]
    preview = "  >  ".join(names) if names else "No tokens detected"

    cv2.rectangle(frame, (0, 0), (frame.shape[1], 45), (30, 30, 30), -1)
    cv2.putText(
        frame, preview[:90], (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX, 0.65,
        (255, 255, 255), 2
    )

    cv2.imshow("MatterOS - Workflow Reader", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("e"):
        # Execute the currently visible sequence once.
        execute_workflow(workflow)

    elif key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

