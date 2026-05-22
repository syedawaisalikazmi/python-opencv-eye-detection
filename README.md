# 👀 Python Real-Time Eye Detection System
📌 Description

A real-time eye detection project built using Python and OpenCV.

This application captures live webcam video and detects human eyes using OpenCV's Haar Cascade classifier.

Detected eyes are highlighted with green rectangles in real time.

🚀 Features

✅ Real-time webcam eye detection
✅ Haar Cascade classifier integration
✅ Live video frame processing
✅ Green rectangle highlighting
✅ Press Q to quit
✅ Camera safety check
✅ Automatic resource cleanup

🛠 Technologies Used
Python
OpenCV (cv2)
Haar Cascade Classifier
Computer Vision
Real-Time Video Processing
📦 Requirements

Install OpenCV before running the project:

pip install opencv-python
▶️ How to Run
python eye_detection.py
💻 Example Workflow
Start Program
↓
Load Eye Cascade Model
↓
Open Webcam
↓
Capture Live Frames
↓
Convert Frame to Grayscale
↓
Detect Eyes
↓
Draw Green Rectangles
↓
Display Live Video
↓
Press Q to Exit
📂 File Structure
eye_detection.py
README.md
🧠 How It Works
1️⃣ Load Haar Cascade Model
cv2.CascadeClassifier()

Loads the pre-trained eye detection model.

2️⃣ Open Webcam
cv2.VideoCapture(0)

Starts the default webcam.

3️⃣ Capture Frames
camera_detect.read()

Reads live video frames from the camera.

4️⃣ Convert to Grayscale
cv2.cvtColor()

Improves detection speed and performance.

5️⃣ Detect Eyes
detectMultiScale()

Scans the image and detects eyes.

6️⃣ Draw Rectangles
cv2.rectangle()

Highlights detected eyes using green rectangles.

🎨 Color Information
(0,255,0)

OpenCV uses BGR color format:

Blue → (255,0,0)
Green → (0,255,0)
Red → (0,0,255)
📈 Future Improvements
Face + Eye combined detection
Blink detection system
Drowsiness detector
Eye tracking
AI attendance system
📊 Project Status

Completed ✅

👨‍💻 Created by Awi Ali
