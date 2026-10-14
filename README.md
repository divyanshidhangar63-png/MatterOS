# MatterOS

**Turning physical actions into digital possibilities.**

MatterOS is a computer-vision project exploring a tangible way to interact with a computer using physical command cards. Built with Python and OpenCV, it uses ArUco markers to recognize cards through a webcam.

## Current Features

- Generates five ArUco command markers.
- Supports START, OPEN, WAIT, PAUSE, and STOP tokens.
- Detects markers using OpenCV.
- Includes custom-designed, color-coded token images.
- Explores reading physical cards as an ordered workflow.

## Tech Stack

- Python
- OpenCV
- ArUco markers
- Webcam-based computer vision

## Setup

### 1. Install Python

Install Python on your computer if you haven't already.

### 2. Clone the repository

```bash
git clone https://github.com/divyanshidhangar63-png/MatterOS.git
cd MatterOS
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate the marker images

```bash
python generate_tokens.py
```

### 5. Check the token images

```bash
python check_tokens.py
```

### 6. Run MatterOS

```bash
python main.py
```

## Command Tokens

| Marker ID | Command |
|---:|---|
| 0 | START |
| 1 | OPEN |
| 2 | WAIT |
| 3 | PAUSE |
| 4 | STOP |

## Project Status

**Early prototype.**

ArUco marker generation and image detection are working. Webcam-based workflow recognition and command execution are being developed.

## Future Goals

- Improve card ordering and workflow recognition.
- Execute predefined computer actions.
- Add more commands and improve usability.
- Build a more intuitive physical-to-digital interaction experience.

## License

No license has been selected yet.
