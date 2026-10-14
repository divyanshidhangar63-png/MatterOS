
import cv2

files = {
    "START": "tokens/START.png",
    "OPEN": "tokens/OPEN.png",
    "WAIT": "tokens/WAIT.png",
    "PAUSE": "tokens/PAUSE.png",
    "STOP": "tokens/STOP.png",
}

dictionary = cv2.aruco.getPredefinedDictionary(
    cv2.aruco.DICT_4X4_50
)

detector = cv2.aruco.ArucoDetector(dictionary)

for name, path in files.items():
    image = cv2.imread(path)

    if image is None:
        print(f"{name}: Image not found at {path}")
        continue

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    corners, ids, rejected = detector.detectMarkers(gray)

    if ids is None:
        print(f"{name}: No valid ArUco marker detected")
    else:
        print(f"{name}: Detected marker ID(s): {ids.flatten()}")
