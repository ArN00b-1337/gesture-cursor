# gesture-cursor



## Description

This project uses computer vision and hand tracking to control your mouse cursor with hand gestures. Move your index finger to control the cursor, and pinch your thumb and index finger together to click.

## Requirements

- Python 3.7+
- Webcam
- Libraries: `opencv-python`, `mediapipe`, `pyautogui`

## Installation

```bash
pip install opencv-python mediapipe pyautogui
```

## Usage

1. Run the script:
```bash
python gestureCursor.py
```

2. Move your index finger to control the cursor
3. Pinch thumb and index finger together to click
4. Press 'q' to quit

## How It Works

1. Captures webcam feed and detects hand landmarks using MediaPipe
2. Tracks index finger (landmark 8) position and maps it to screen coordinates
3. Tracks thumb (landmark 4) position
4. Performs click when thumb and index finger are within 20 pixels

## Customization

- **Click sensitivity**: Adjust distance threshold (line 40)
  ```python
  if abs(index_y - thumb_y) < 20:  # Change 20
  ```

- **Click delay**: Modify sleep time (line 42)
  ```python
  pyautogui.sleep(1)  # Change duration
  ```

## Technologies Used

- **OpenCV**: Computer vision and image processing
- **MediaPipe**: Hand tracking and landmark detection
- **PyAutoGUI**: Mouse control automation
