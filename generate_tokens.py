

import cv2
from pathlib import Path

output_folder = Path("tokens")
output_folder.mkdir(exist_ok=True)

tokens = {
    0: "START",
    1: "OPEN",
    2: "WAIT",
    3: "PAUSE",
    4: "STOP",
}

aruco = cv2.aruco
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

for marker_id, name in tokens.items():
    # Generate a genuine ArUco marker
    marker = aruco.generateImageMarker(
        dictionary, marker_id, 400
    )

    # Add a white margin around the marker
    marker = cv2.copyMakeBorder(
        marker, 60, 60, 60, 60,
        cv2.BORDER_CONSTANT,
        value=255
    )

    filepath = output_folder / f"{name}.png"
    if not cv2.imwrite(str(filepath), marker):
        raise RuntimeError(f"Could not save {filepath}")

    print(f"Saved: {filepath.resolve()}")

print("All five ArUco markers generated successfully.")
