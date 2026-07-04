# 🏋️‍♂️ ARIA Workout Counter (Bicep Curl Rep Counter)

An AI-powered professional workout repetition counter built using **Python**, **OpenCV**, and **MediaPipe's Next-Gen Tasks API**. This project tracks human pose landmarks in real-time, calculates precise joint angles using 3D vector geometry, and features an anti-double-counting state lock system.

---

## ✨ Features

- **3D World Landmark Tracking:** Uses MediaPipe's `pose_world_landmarks` (measured in meters) to calculate glitch-free angles, avoiding 2D perspective distortions.
- **Advanced Debouncing Logic:** Built-in time-based cooldown system to prevent multiple accidental counts (double-counting) within sub-second frames.
- **Smooth Real-time Visualization:** Overlays joint points, connecting skeleton bones, and current live angle measurements on the screen.
- **Dynamic Dashboard:** Clean dark HUD overlay showing total completed reps and current movement stage (`up` / `down`).

---

## 🛠️ The Logic & Tech Behind It (For Techies)

- **Vector Mathematics:** Instead of simple distance mapping, the app extracts 3D coordinate tensors for the **Shoulder**, **Elbow**, and **Wrist**.
- **Dot Product & Cosine Theorem:** Calculates the strict inner angle of the elbow joint using:
  $$\theta = \arccos\left(\frac{\vec{BA} \cdot \vec{BC}}{\|\vec{BA}\| \|\vec{BC}\|}\right)$$
- **Why Cosine?** Cosine provides unique monotonic mapping from $0^\circ$ to $180^\circ$ ensuring the engine never confuses extension with flexion.

---

## ⚙️ Project Setup

### 1. Prerequisites
Make sure you have Python 3.9+ installed. Install the required dependencies using pip:

```bash
pip install opencv-python mediapipe numpy
```

### 2. Download the Model Bundle
This project relies on MediaPipe's Task Vision models. Download the model asset file:
- Download [pose_landmarker_lite.task](https://googleapis.com)
- Place the downloaded file inside your main project root directory.

### 3. Execution
Run the tracking system using the following command:

```bash
python workout_counter.py
```
*Press **'q'** anytime on the camera window to terminate the session.*

---

## 📊 How To Use

1. Step back so your upper body (Shoulder, Elbow, and Wrist) is clearly visible in the webcam.
2. Perform a **Bicep Curl** motion.
3. Bring your hand completely down (extension $> 150^\circ$) to reset the system state to `down`.
4. Curl your arm up completely (flexion $< 70^\circ$). The dashboard will increment the counter seamlessly.

---

