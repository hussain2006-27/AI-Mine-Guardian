# 🛡️ AI Mine Guardian

## AI-Powered Underground Mine Safety, Monitoring and Rescue System

AI Mine Guardian is an intelligent mine-safety system designed to monitor underground mining environments using **IoT sensors, computer vision, AI-based risk analysis, and real-time dashboards**.

The system combines environmental sensor data with visual information to identify hazardous conditions and provide a centralized view of mine safety.

---

## 🚨 Problem

Underground mines can expose workers to hazards such as:

* Toxic and combustible gases
* Unsafe temperature and humidity conditions
* Structural or environmental hazards
* Poor visibility
* Delayed detection of dangerous conditions

Traditional monitoring systems may depend heavily on individual sensors and may not provide a complete picture of the environment.

---

## 💡 Proposed Solution

AI Mine Guardian combines multiple sources of information into a unified monitoring system.

### System Overview

```text
        ┌──────────────────────┐
        │   Mine Environment   │
        └──────────┬───────────┘
                   │
          ┌────────┴─────────┐
          │                  │
     IoT Sensors          Camera
          │                  │
          │             YOLO / OpenCV
          │                  │
          └────────┬─────────┘
                   │
             Risk Analysis
                   │
          ┌────────┴─────────┐
          │                  │
     Sensor Risk        Vision Risk
          │                  │
          └────────┬─────────┘
                   │
            Combined Risk
              Analysis
                   │
                   ▼
          ┌─────────────────┐
          │   Dashboard     │
          │ Monitoring &    │
          │ Alerts          │
          └─────────────────┘
```

---

## 🔧 Technologies Used

| Category             | Technologies                |
| -------------------- | --------------------------- |
| Microcontroller      | ESP32                       |
| Sensors              | MQ-4, MQ-7, BME280, HC-SR04 |
| Camera               | ESP32-CAM / OV2640          |
| AI / Computer Vision | YOLO, OpenCV                |
| Backend              | Python                      |
| Risk Analysis        | Python                      |
| Database             | Firebase                    |
| Dashboard            | HTML, CSS, JavaScript       |
| Communication        | Wi-Fi                       |
| Simulation           | Python                      |
| Model                | YOLO11n                     |

---

## 📁 Project Structure

```text
AI-Mine-Guardian/
│
├── ai/
│   ├── camera_config.py
│   ├── camera_test.py
│   ├── camera_yolo.py
│   ├── detect_image.py
│   ├── test_environment.py
│   ├── yolo_test.py
│   └── test_images/
│
├── dashboard/
│   ├── index.html
│   └── style.css
│
├── firebase/
│   └── firebase_config.py
│
├── risk_engine/
│   ├── combined_risk_engine.py
│   ├── risk_engine.py
│   └── risk_test.py
│
├── simulation/
│   └── sensor_simulator.py
│
├── vision/
│   └── vision_detector.py
│
├── yolo11n.pt
├── .gitignore
└── README.md
```

---

## 🧠 AI Vision System

The vision subsystem uses **YOLO** and **OpenCV** to process camera images and identify relevant visual conditions.

The YOLO model is used for object detection, while OpenCV provides image-processing capabilities.

The detected visual information can be incorporated into the overall mine-risk assessment.

---

## 🌡️ Environmental Monitoring

The system can process data from multiple environmental sensors.

Example parameters include:

* Methane concentration using MQ-4
* Carbon monoxide using MQ-7
* Temperature using BME280
* Humidity using BME280
* Atmospheric pressure using BME280
* Distance information using HC-SR04

The sensor values are evaluated by the risk engine to determine the current safety condition.

---

## ⚠️ Multimodal Risk Engine

One of the main features of AI Mine Guardian is the combination of different sources of information.

```text
Sensor Data
     │
     ▼
Sensor Risk Score
     │
     ├──────────────┐
     │              │
     │         Vision Data
     │              │
     │              ▼
     │        Vision Analysis
     │              │
     └───────┬──────┘
             ▼
       Combined Risk
             │
             ▼
     SAFE / WARNING / DANGER
```

This allows the system to consider both **environmental conditions and visual information** instead of depending on a single sensor.

---

## 📊 Monitoring Dashboard

The project includes a web-based dashboard for displaying mine-monitoring information.

The dashboard is designed to provide a centralized view of:

* Sensor readings
* Environmental conditions
* Vision information
* Mine risk status
* Safety alerts

Firebase is used for storing and synchronizing relevant monitoring data.

---

## 🔥 Firebase Integration

Firebase is used as the backend database for storing monitoring information.

> **Security:** Firebase service-account credentials are intentionally excluded from this repository using `.gitignore`.

Create your own Firebase service-account configuration locally before running the Firebase components.

---

## 🧪 Simulation

The project includes a sensor simulation component that can generate sensor data for testing the monitoring and risk-analysis system without requiring all physical sensors.

This helps test the software components during development.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/hussain2006-27/AI-Mine-Guardian.git
cd AI-Mine-Guardian
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

---

## 🔐 Firebase Configuration

Do not upload your Firebase service-account JSON file to GitHub.

Place your local Firebase credentials in the project according to the configuration expected by the Firebase Python code.

The credential file is excluded through:

```text
firebase-service-account.json
```

---

## ▶️ Running the Project

### Run the risk engine

```bash
python risk_engine/risk_engine.py
```

### Run the combined risk engine

```bash
python risk_engine/combined_risk_engine.py
```

### Run the sensor simulator

```bash
python simulation/sensor_simulator.py
```

### Run the dashboard

From the project directory:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/dashboard/
```

---

## 🎯 Key Features

* Real-time environmental monitoring
* Multi-sensor data analysis
* AI-based visual detection
* YOLO object detection
* OpenCV image processing
* Combined sensor and vision risk analysis
* Firebase data integration
* Web-based monitoring dashboard
* Sensor-data simulation for testing
* ESP32-based IoT architecture

---

## 🚀 Future Enhancements

* Real-time video streaming from ESP32-CAM
* Advanced mine hazard detection
* Automated emergency alerts
* GPS-based location tracking
* Mine mapping and navigation
* SLAM-based rover navigation
* WebSocket-based real-time telemetry
* Improved multimodal AI risk prediction
* Autonomous mine inspection rover

---

## 👨‍💻 Project

**AI Mine Guardian**

AI-Powered Underground Mine Safety, Monitoring and Rescue System

Developed as an IoT + AI solution for intelligent underground mine monitoring and safety.

---

## 📜 License

This project is intended for educational, research, and prototype development purposes.
