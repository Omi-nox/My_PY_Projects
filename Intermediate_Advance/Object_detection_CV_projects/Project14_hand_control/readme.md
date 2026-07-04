# 👆 ARIA Gesture Control (AI Virtual Mouse & Hand Gesture Controller)

An advanced, low-latency Virtual Mouse and OS Controller built using **Python**, **OpenCV**, **PyAutoGUI**, and **MediaPipe's Hand Landmarker Tasks API**. This system maps human hand tracking landmarks to real-time OS actions, turning your index finger into a smooth mouse cursor with custom gesture macros.

---

## ✨ Features

- **Smooth Cursor Movement:** Uses a mathematical exponential moving average interpolation algorithm to completely eliminate raw hand jitter and flicker.
- **Active Zone Mapping:** Constrains the cursor to a sub-section of the camera frame, allowing full-screen coverage with minimal physical hand movement.
- **Intelligent Gestures:**
  - 📜 **Scroll Down:** Raise only the Index Finger.
  - 📜 **Scroll Up:** Raise both Index and Middle Fingers.
  - 🖱️ **Left Click:** Pinch index finger and thumb together (Distance $< 20px$ with a $0.9s$ cooldown).
  - 🗂️ **Windows Task View (`WIN + TAB`):** Raise Index and Pinky fingers while keeping others down.
- **Fail-Safe Mechanism:** Hard-coded fail-safe configuration allowing emergency script escape by throwing the cursor to corners.

---

## 🛠️ System Architecture & Logic

### 1. Exponential Smoothing Formula
To prevent the mouse cursor from jumping wildly due to minor webcam noise, the script applies an accumulation filter over frame arrays:
$$\text{Smooth\_X} \leftarrow \text{Smooth\_X} + \frac{\text{Target\_X} - \text{Smooth\_X}}{\text{Smoothing\_Factor}}$$
*Higher smoothing factors yield cinematic cursor stability, while lower numbers provide instantaneous twitch responses.*

### 2. Normalized Interpolation (`np.interp`)
Camera pixel fields ($640 \times 480$) do not match desktop grid aspect ratios (e.g., $1920 \times 1080$). The app dynamically maps boundaries:
- **X-Axis:** Maps camera margins $[100 \rightarrow \text{Width} - 100]$ linearly to $[0 \rightarrow \text{Screen Width}]$.
- **Y-Axis:** Maps camera vertical constraints $[50 \rightarrow \text{Height} - 80]$ to $[0 \rightarrow \text{Screen Height}]$, ensuring full taskbar reach.

---

## ⚙️ Project Setup

### 1. Prerequisites
Ensure you are using Python 3.9+ environment. Install the dependency framework using pip:

```bash
pip install opencv-python mediapipe pyautogui numpy
```

### 2. Download the Model File
This project targets MediaPipe's dedicated hand landmarker topology bundle:
- Download [hand_landmarker.task](https://googleapis.com)
- Place the downloaded asset directly in your main project folder root.

### 3. Running the App
Initiate the hand-space mouse engine using:

```bash
python gesture_mouse.py
```
*Press **'q'** on the camera runtime frame window to kill the process loop safely.*

---

## 🛑 Important Safety Note
- **Emergency Stop:** Move the mouse cursor directly to the **TOP LEFT corner** of your physical monitor to invoke PyAutoGUI safety tripwire if the gesture system loops unpredictably.

---

