# 🖌️ ARIA Finger Drawing (AI Air Writing)

An interactive Computer Vision project built with **Python**, **OpenCV**, and the latest **Google MediaPipe Tasks API (v0.10.35+)**. This application turns your laptop webcam into a dynamic canvas, allowing you to draw in the air using simple hand gestures.

---

## ✨ Features

*   **Pinch-to-Draw**: Uses **Euclidean Distance** between your Thumb and Index finger to activate/deactivate drawing mode.
*   **Fist-to-Erase**: Automatically clears the entire drawing canvas when you make a fist (Index finger curled down).
*   **Dynamic Color Switching**: Change ink colors instantly using your keyboard shortcuts.
*   **Snapshot Saver**: Save your final masterpieces directly to your local folder with a single keypress.
*   **Optimized Alignment**: Handles the latest MediaPipe flip-coordinate tracking behavior for precision drawing.

---

## 🛠️ Controls Menu

Show your hand on camera and use these keyboard buttons to control the application:

| Key | Action | Description |
| :---: | :--- | :--- |
| **Pinch** | 🟢 Draw | Touch Thumb and Index tips together to paint. |
| **Fist** | 🧼 Clear | Make a fist to wipe the entire screen clean. |
| **`R`** | 🔴 Red | Change drawing ink to Red (Default). |
| **`G`** | 🟢 Green | Change drawing ink to Green. |
| **`B`** | 🔵 Blue | Change drawing ink to Blue. |
| **`W`** | ⚪ White | Change drawing ink to White. |
| **`S`** | 📸 Save | Take a screenshot and save it as `screenshot.png`. |
| **`Q`** | 🚪 Quit | Safely close the camera window and exit. |

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.10+ installed on your operating system.

### 2. Installation
Clone the repository and install the required dependencies:

```bash
pip install opencv-python mediapipe numpy
```

### 3. Download the AI Model File
The latest MediaPipe Tasks API requires an explicit model bundle file to process landmarks.
1. Run the Python automated download script or visit Google's official link to grab **`hand_landmarker.task`**.
2. Place the `hand_landmarker.task` file inside the **same directory** as your main script.

### 4. Run the Project
Execute the main file to boot up your air drawing board:

```bash
python finger_drawing.py
```

---

## 📐 How it Works (Under the Hood)

1.  **Frame Optimization**: Captures BGR webcam feed, clones it for individual RGB processing via MediaPipe, and flips the display stream horizontally to provide a natural, mirror-like feel.
2.  **Tracking & Normalization**: Extracts explicit 21 3D coordinate-joints of the hand. Translates normalized vector metrics (0.0 to 1.0) into accurate target screen pixels.
3.  **Euclidean Distance Filter**: Continuously computes the distance vector between **Landmark 4 (Thumb Tip)** and **Landmark 8 (Index Tip)** using:
    \[\text{Distance} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}\]
    If the threshold drops below 85 px, drawing lines are appended onto an independent canvas layer.
4.  **Weighted Blending**: Merges the camera matrix frames together using structural linear weights:
    \[\text{Combined} = (\text{Frame} \times 1) + (\text{Canvas} \times 1) + 0\]

---

## 📂 Project Structure

```text
Object_detection_CV_projects/
│
├── finger_drawing.py       # Main Application Script
├── hand_landmarker.task    # Google MediaPipe Hand Detection Model File
└── README.md               # Project Documentation
```
