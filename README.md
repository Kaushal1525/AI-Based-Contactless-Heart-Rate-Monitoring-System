# AI-Based Contactless Heart Rate Monitoring System

## Overview

This project implements a real-time, contactless heart rate monitoring system using computer vision and remote photoplethysmography (rPPG). The application estimates a user's heart rate through a standard webcam by analyzing subtle color variations in the facial skin, eliminating the need for wearable sensors or physical contact.

The system detects the user's face, extracts a forehead region of interest (ROI), measures changes in the green color channel, filters the physiological signal using a Butterworth band-pass filter, and estimates heart rate using Fast Fourier Transform (FFT). A live heart rate graph and estimated Beats Per Minute (BPM) are displayed in real time.

This project demonstrates the integration of computer vision, digital signal processing, and biomedical sensing techniques for non-invasive health monitoring.

---

# Features

* Real-time webcam-based heart rate estimation
* Contactless physiological monitoring
* Automatic face detection
* Forehead Region of Interest (ROI) extraction
* Green channel signal analysis
* Remote Photoplethysmography (rPPG)
* Butterworth band-pass filtering
* FFT-based frequency analysis
* Live BPM estimation
* Real-time heart rate visualization
* Continuous signal processing
* Non-invasive monitoring

---

# Technologies Used

* Python 3
* OpenCV
* NumPy
* SciPy
* CVZone
* Matplotlib

---

# Project Structure

```text
AI-Heart-Rate-Monitor/
│
├── heart_rate_monitor.py
├── README.md
└── requirements.txt
```

---

# Installation

## Clone the repository

```bash
git clone https://github.com/Kaushal1525/AI-Heart-Rate-Monitor.git
```

## Navigate to the project directory

```bash
cd AI-Heart-Rate-Monitor
```

## Install the required dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install opencv-python numpy scipy matplotlib cvzone
```

---

# Running the Project

Execute the application:

```bash
python heart_rate_monitor.py
```

The system will:

* Open the webcam.
* Detect the user's face.
* Extract the forehead region.
* Analyze changes in the green color channel.
* Apply signal filtering.
* Estimate heart rate using FFT.
* Display the estimated BPM on the video feed.
* Plot the heart rate continuously in a live graph.

Press **Q** to exit the application.

---

# Working Principle

The system follows these processing stages:

1. Capture live video from the webcam.
2. Detect the user's face.
3. Extract the forehead region.
4. Measure average green channel intensity.
5. Store temporal signal samples.
6. Apply Butterworth band-pass filtering.
7. Perform Fast Fourier Transform (FFT).
8. Identify the dominant frequency.
9. Convert frequency into Beats Per Minute (BPM).
10. Display the estimated heart rate and live graph.

---

# System Architecture

```text
Webcam Input
      │
      ▼
Face Detection
      │
      ▼
Forehead ROI Extraction
      │
      ▼
Green Channel Signal Extraction
      │
      ▼
Signal Buffer
      │
      ▼
Band-Pass Filtering
      │
      ▼
Fast Fourier Transform (FFT)
      │
      ▼
Peak Frequency Detection
      │
      ▼
Heart Rate Estimation (BPM)
      │
      ├────────────► Live Video Display
      │
      └────────────► Real-Time BPM Graph
```

---

# Signal Processing Pipeline

The application estimates heart rate using the following sequence:

* Face detection
* Forehead ROI extraction
* Green channel intensity calculation
* Temporal signal buffering
* Noise reduction using Butterworth filtering
* Frequency-domain transformation using FFT
* Peak frequency identification
* BPM calculation

---

# Remote Photoplethysmography (rPPG)

The system is based on the principle of Remote Photoplethysmography (rPPG), where subtle skin color variations caused by blood circulation are captured by a conventional RGB camera.

The green channel is used because it generally contains the strongest pulse-related information under normal lighting conditions.

---

# Heart Rate Estimation

The dominant frequency within the physiological heart rate range is extracted from the filtered signal.

Heart Rate is calculated as:

```text
Heart Rate (BPM) = Peak Frequency × 60
```

---

# Applications

* Contactless patient monitoring
* Telemedicine
* Smart healthcare
* Biomedical signal processing
* Driver health monitoring
* Elderly care systems
* Fitness monitoring
* Human-computer interaction
* AI healthcare research
* Remote physiological monitoring

---

# Future Enhancements

* Multi-person heart rate estimation
* Blood oxygen (SpO₂) estimation
* Respiratory rate monitoring
* Heart Rate Variability (HRV) analysis
* Deep learning-based face tracking
* Motion artifact reduction
* Real-time data logging
* Mobile application integration
* Cloud health dashboard
* Edge AI deployment
* Raspberry Pi implementation
* Medical IoT integration

---

# Requirements

* Python 3.8 or later
* Webcam

---

# Dependencies

* opencv-python
* numpy
* scipy
* matplotlib
* cvzone

---

# Author

**Kaushal Reddy**

AI & Autonomous Systems Engineer

GitHub: https://github.com/Kaushal1525
