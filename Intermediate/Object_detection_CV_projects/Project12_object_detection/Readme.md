# Real-Time Threat Detection System using YOLOv8 and OpenCV

A lightweight, real-time computer vision application that utilizes the YOLOv8 nano model to monitor a live webcam feed, detect objects, and flag specific items (like knives and scissors) as potential security threats.

## 🚀 Features
* **Live Webcam Streaming:** Captures and processes real-time video frames.
* **YOLOv8 Inference:** Utilizes a fast and accurate deep learning model (`yolov8n.pt`).
* **Threat Filtering:** Specifically monitors and highlights predefined threat objects.
* **On-Screen Telemetry:** Displays total object count, threat status, and a lifetime threat counter.
* **Snapshot on Exit:** Saves a final `screenshot.png` of the annotated frame automatically upon quitting.

## 🛠️ Prerequisites & Installation

### 1. Clone the Repository
```bash
git clone https://github.com
cd YOUR_REPOSITORY_NAME
```

### 2. Install Dependencies
Ensure you have Python installed, then install the required libraries:
```bash
pip install opencv-python ultralytics
```
*Note: The `ultralytics` package automatically downloads the weights for `yolov8n.pt` on its first run.*

## 💻 How to Run

Execute the script using Python:
```bash
python main.py
```

### Controls
* **Press `S`:** Saves a screenshot (`screenshot.png`) of the current frame and safely exits the application.

## ⚙️ How It Works
1. **Camera Initialization:** The script safely opens the default webcam (`cv2.VideoCapture(0)`).
2. **Frame-by-Frame Processing:** It reads individual frames and passes them silently (`verbose=False`) into the YOLOv8 pipeline.
3. **Object Evaluation:** It loops through every detected bounding box, maps the class ID to a human-readable label, and extracts confidence scores.
4. **Threat Flagging:** If the label matches items inside the `threat_objects` array, it triggers a visual warning status.
5. **Annotation & Rendering:** OpenCV draws text overlays and labeled bounding boxes onto the live video window.

## 📋 Customization
You can easily add more objects to monitor by modifying the `threat_objects` list in the script. YOLOv8 supports 80 default COCO classes (e.g., "fire hydrant", "backpack", "baseball bat").

```python
# Example: Adding more potential threats
threat_objects = ["knife", "scissors", "baseball bat"]
```

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
