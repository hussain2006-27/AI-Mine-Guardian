# 🛡️ AI Mine Guardian

## AI-Powered Underground Mine Safety, Monitoring and Rescue System

AI Mine Guardian is an intelligent underground mine safety and monitoring system that combines **IoT sensors, embedded systems, computer vision, artificial intelligence, risk analysis, cloud connectivity, and a web-based dashboard**.

The system is designed to continuously monitor environmental conditions and visual information inside underground mining environments. Sensor and camera data are processed to identify potentially unsafe conditions and classify the overall mine status as **SAFE, WARNING, or DANGER**.

---

## 🚨 Problem Statement

Underground mining environments can expose workers and equipment to several potentially dangerous conditions, including:

- Toxic and combustible gases
- Carbon monoxide accumulation
- Unsafe temperature and humidity
- Poor environmental conditions
- Obstacles and possible structural hazards
- Limited visibility
- Delayed detection of hazardous situations
- Difficulty in continuously monitoring underground areas

Conventional monitoring approaches may rely mainly on individual sensors. However, a single sensor cannot provide a complete understanding of the mine environment.

AI Mine Guardian addresses this limitation by combining **multiple environmental sensors with computer vision and AI-based risk analysis**.

---

## 💡 Proposed Solution

AI Mine Guardian provides a unified monitoring system that combines:

- IoT-based environmental sensing
- ESP32-based embedded processing
- ESP32-CAM visual monitoring
- YOLO-based object detection
- OpenCV image processing
- Multimodal risk analysis
- Firebase data synchronization
- Web-based monitoring dashboard
- Sensor-data simulation for software testing

The system combines environmental and visual information to produce an overall safety assessment.

---

## 🏗️ System Overview

```text
                    ┌────────────────────────┐
                    │   UNDERGROUND MINE     │
                    │      ENVIRONMENT       │
                    └───────────┬────────────┘
                                │
                ┌───────────────┴───────────────┐
                │                               │
                ▼                               ▼
       ┌─────────────────┐             ┌─────────────────┐
       │  IoT Sensors    │             │     Camera      │
       │                 │             │   ESP32-CAM     │
       ├─────────────────┤             │     OV2640      │
       │ MQ-4            │             └────────┬────────┘
       │ MQ-7            │                      │
       │ BME280          │                      ▼
       │ HC-SR04         │               YOLO / OpenCV
       └────────┬────────┘                      │
                │                               │
                ▼                               ▼
       ┌─────────────────┐             ┌─────────────────┐
       │ Sensor Analysis │             │ Vision Analysis │
       └────────┬────────┘             └────────┬────────┘
                │                               │
                └───────────────┬───────────────┘
                                │
                                ▼
                    ┌────────────────────────┐
                    │  MULTIMODAL RISK       │
                    │       ENGINE            │
                    └───────────┬────────────┘
                                │
                                ▼
                    ┌────────────────────────┐
                    │ SAFE / WARNING / DANGER │
                    └───────────┬────────────┘
                                │
                                ▼
                    ┌────────────────────────┐
                    │       FIREBASE         │
                    │        DATABASE        │
                    └───────────┬────────────┘
                                │
                                ▼
                    ┌────────────────────────┐
                    │   WEB DASHBOARD        │
                    │ Monitoring & Alerts    │
                    └────────────────────────┘
🔧 Technologies Used
Category	Technologies
Microcontroller	ESP32
Sensors	MQ-4, MQ-7, BME280, HC-SR04
Camera	ESP32-CAM / OV2640
AI / Computer Vision	YOLO11n, OpenCV
Backend	Python
Risk Analysis	Python
Database	Firebase Realtime Database
Dashboard	HTML, CSS, JavaScript
Communication	Wi-Fi
Simulation	Python
Development Tools	VS Code, Arduino IDE
Version Control	Git, GitHub
🔩 Hardware Components
Component	Purpose
ESP32	Main microcontroller for sensor data collection and communication
ESP32-CAM	Captures visual information from the mine environment
OV2640	Camera sensor used with ESP32-CAM
MQ-4	Methane and combustible gas monitoring
MQ-7	Carbon monoxide monitoring
BME280	Temperature, humidity and atmospheric pressure monitoring
HC-SR04	Distance and obstacle detection
Rover Platform	Mobile platform for the mine-monitoring prototype
Wi-Fi	Wireless communication
📁 Project Structure
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
│       ├── detected.jpg
│       └── test.jpg
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
├── images/
│   ├── Team.jpeg
│   ├── proto_1.jpeg
│   ├── proto_2.jpeg
│   ├── proto_3.jpeg
│   ├── dashboard-safe.jpeg
│   ├── dashboard-warning.jpeg
│   └── dashboard-danger.jpeg
│
├── yolo11n.pt
├── .gitignore
└── README.md
🧠 AI Vision System

The vision subsystem uses YOLO11n and OpenCV to process camera images and identify relevant visual information.

The YOLO model performs object detection, while OpenCV provides image-processing capabilities.

The detected visual information can be incorporated into the overall mine-risk assessment.

The vision system can provide information such as:

Detected objects
Object classes
Bounding boxes
Detection confidence
Visual information from the mine environment
👁️ Computer Vision Workflow
                 ESP32-CAM
                     │
                     ▼
              Image Capture
                     │
                     ▼
            OpenCV Processing
                     │
                     ▼
                  YOLO11n
                     │
                     ▼
             Object Detection
                     │
                     ▼
          Detection Information
                     │
                     ▼
              Vision Analysis
                     │
                     ▼
            Vision Risk Input
                     │
                     ▼
          Multimodal Risk Engine

The camera captures visual information from the environment.

The image is processed using OpenCV and passed to the YOLO model.

YOLO identifies objects in the image and generates detection information that can be used as an additional input to the risk-analysis system.

🌡️ Environmental Monitoring

The system can process data from multiple environmental sensors.

MQ-4

The MQ-4 sensor is used for methane and combustible-gas monitoring.

Methane monitoring is important in underground mining environments because the accumulation of combustible gas can create serious safety risks.

MQ-7

The MQ-7 sensor is used for carbon monoxide monitoring.

Carbon monoxide can be hazardous in enclosed environments, making continuous monitoring useful for mine safety.

BME280

The BME280 provides:

Temperature
Humidity
Atmospheric pressure

These parameters provide additional information about the environmental condition.

HC-SR04

The HC-SR04 provides distance measurements.

It can be used for detecting nearby obstacles and supporting mobile-rover monitoring and navigation.

📡 Sensor Data Flow
             ┌───────────┐
             │   MQ-4    │
             └─────┬─────┘
                   │
             ┌─────▼─────┐
             │   MQ-7    │
             └─────┬─────┘
                   │
             ┌─────▼─────┐
             │  BME280   │
             └─────┬─────┘
                   │
             ┌─────▼─────┐
             │  HC-SR04  │
             └─────┬─────┘
                   │
                   ▼
             Sensor Data
                   │
                   ▼
           Sensor Processing
                   │
                   ▼
            Sensor Risk Score
                   │
                   ▼
             Risk Engine
⚠️ Multimodal Risk Engine

One of the main features of AI Mine Guardian is the combination of different sources of information.

The system considers both environmental sensor information and visual information instead of depending on a single sensor.

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

The combined risk analysis provides a centralized assessment of the current mine condition.

🟢 SAFE Condition

The system identifies a SAFE condition when monitored parameters remain within the defined acceptable range and no significant risk is detected.

SAFE

The dashboard displays the current sensor information and overall safety status.

🟡 WARNING Condition

The system identifies a WARNING condition when abnormal sensor values or visual information indicate a potentially unsafe situation.

WARNING

This condition indicates that the situation should be monitored carefully.

🔴 DANGER Condition

The system identifies a DANGER condition when critical conditions are detected.

DANGER

This condition indicates that immediate attention may be required.

📊 Monitoring Dashboard

The project includes a web-based dashboard for displaying mine-monitoring information.

The dashboard is designed to provide a centralized view of:

Sensor readings
Environmental conditions
Vision information
Mine risk status
Safety alerts
Overall monitoring status

Firebase is used for storing and synchronizing relevant monitoring data.

🟢 Dashboard — Safe Condition

The dashboard displays SAFE when the monitored conditions are within the defined safe range.

🟡 Dashboard — Warning Condition

The dashboard displays WARNING when potentially unsafe conditions are detected.

🔴 Dashboard — Danger Condition

The dashboard displays DANGER when critical conditions are detected.

🔥 Firebase Integration

Firebase is used as the backend database for storing monitoring information.

The system can synchronize relevant sensor, vision, and risk information with Firebase so that the dashboard can access the latest monitoring data.

Firebase Data Flow
ESP32 / Python
      │
      ▼
Sensor + Vision Data
      │
      ▼
Risk Analysis
      │
      ▼
Firebase Realtime Database
      │
      ▼
Web Dashboard

Security: Firebase service-account credentials are intentionally excluded from this repository using .gitignore.

Do not upload your Firebase service-account JSON file to GitHub.

The credential file:

firebase-service-account.json

is excluded from the repository.

🤖 Project Prototype

The AI Mine Guardian prototype demonstrates the physical implementation of the proposed mine-monitoring system.

The prototype integrates the mobile platform, embedded electronics, sensors, and camera-based monitoring.

👥 Team

🚙 Overall Prototype

🔌 Prototype Hardware

🔍 Prototype Details

🧪 Simulation

The project includes a sensor simulation component that can generate sensor data for testing the monitoring and risk-analysis system without requiring all physical sensors.

This helps test the software components during development.

Simulation Flow
       Simulated Sensor Data
                │
                ▼
        Sensor Processing
                │
                ▼
          Risk Engine
                │
                ▼
        Risk Classification
                │
                ▼
           Dashboard
🔄 Overall System Workflow
1. Sensors collect environmental information
                    │
                    ▼
2. ESP32 processes / transmits sensor data
                    │
                    ▼
3. ESP32-CAM captures visual information
                    │
                    ▼
4. YOLO + OpenCV process camera data
                    │
                    ▼
5. Sensor risk is calculated
                    │
                    ▼
6. Vision information is analyzed
                    │
                    ▼
7. Sensor and vision information are combined
                    │
                    ▼
8. System determines SAFE / WARNING / DANGER
                    │
                    ▼
9. Monitoring information is synchronized
   with Firebase
                    │
                    ▼
10. Dashboard displays the current status
🏗️ Software Architecture
┌──────────────────────────────────────────────────────┐
│                    AI MINE GUARDIAN                  │
└─────────────────────────┬────────────────────────────┘
                          │
          ┌───────────────┴────────────────┐
          │                                │
          ▼                                ▼
┌────────────────────┐          ┌─────────────────────┐
│ Environmental Data │          │    Vision Data      │
│                    │          │                     │
│ MQ-4               │          │ ESP32-CAM           │
│ MQ-7               │          │ OV2640              │
│ BME280             │          │ YOLO11n              │
│ HC-SR04            │          │ OpenCV               │
└─────────┬──────────┘          └──────────┬──────────┘
          │                                │
          ▼                                ▼
┌────────────────────┐          ┌─────────────────────┐
│ Sensor Risk Engine │          │   Vision Analysis   │
└─────────┬──────────┘          └──────────┬──────────┘
          │                                │
          └───────────────┬────────────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Multimodal Risk    │
                │ Engine             │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ SAFE / WARNING /   │
                │ DANGER             │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Firebase Database  │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Web Dashboard      │
                └────────────────────┘
📈 Risk Classification
Condition	Risk Level	System Status
Normal environmental and visual conditions	Low	🟢 SAFE
Abnormal condition detected	Medium	🟡 WARNING
Critical condition detected	High	🔴 DANGER
🔄 Data Processing Pipeline
        Underground Environment
                 │
                 ▼
          Sensors + Camera
                 │
                 ▼
           Data Collection
                 │
        ┌────────┴────────┐
        │                 │
        ▼                 ▼
  Sensor Processing   Image Processing
        │                 │
        ▼                 ▼
 Sensor Risk Score    YOLO Detection
        │                 │
        └────────┬────────┘
                 │
                 ▼
        Multimodal Analysis
                 │
                 ▼
          Risk Classification
                 │
        ┌────────┼────────┐
        ▼        ▼        ▼
      SAFE    WARNING   DANGER
                 │
                 ▼
          Firebase Database
                 │
                 ▼
             Dashboard
🧩 Project Modules
1. AI Module

Responsible for camera processing, YOLO-based object detection, and AI-based visual analysis.

2. Vision Module

Processes visual information and provides detection results that can be used by the risk engine.

3. Risk Engine

Analyzes sensor and vision information and determines the overall risk condition.

4. Firebase Module

Handles communication with the Firebase database and provides data synchronization for the monitoring system.

5. Dashboard Module

Provides a web-based interface for viewing sensor information, risk status, and monitoring data.

6. Simulation Module

Generates simulated sensor data for testing the software and risk-analysis components.

🎯 Key Features
Real-time environmental monitoring
Multi-sensor data analysis
Methane monitoring
Carbon monoxide monitoring
Temperature monitoring
Humidity monitoring
Atmospheric pressure monitoring
Distance and obstacle detection
ESP32-based IoT architecture
ESP32-CAM visual monitoring
YOLO object detection
OpenCV image processing
Multimodal risk analysis
SAFE / WARNING / DANGER classification
Firebase database integration
Web-based monitoring dashboard
Sensor-data simulation
Mobile mine-monitoring prototype
🚨 Safety Alert Concept

The system can be extended to trigger alerts when dangerous conditions are detected.

Critical Condition
       │
       ▼
Risk Engine
       │
       ▼
DANGER Status
       │
       ├───────────────► Dashboard Alert
       │
       ├───────────────► Remote Notification
       │
       └───────────────► Emergency Response

This provides a foundation for future automated emergency-response capabilities.

⚙️ Installation
1. Clone the repository
git clone https://github.com/hussain2006-27/AI-Mine-Guardian.git
cd AI-Mine-Guardian
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment

For Windows:

.venv\Scripts\activate
4. Install dependencies

If a requirements.txt file is available:

pip install -r requirements.txt
🔐 Firebase Configuration

Do not upload your Firebase service-account JSON file to GitHub.

Place your local Firebase credentials in the project according to the configuration expected by the Firebase Python code.

The credential file is excluded through:

firebase-service-account.json

Make sure sensitive credentials remain local and are not committed to the repository.

▶️ Running the Project
Run the Risk Engine
python risk_engine/risk_engine.py
Run the Combined Risk Engine
python risk_engine/combined_risk_engine.py
Run the Sensor Simulator
python simulation/sensor_simulator.py
Run the Dashboard

From the project directory:

python -m http.server 8000

Then open:

http://localhost:8000/dashboard/
🧪 Testing

The project contains testing scripts for validating individual components.

Examples include:

ai/camera_test.py
ai/yolo_test.py
ai/test_environment.py
risk_engine/risk_test.py

These scripts can be used to test individual modules during development and debugging.

🛠️ Development Environment

The project can be developed and tested using:

Visual Studio Code
Python
Arduino IDE
ESP32 development environment
Firebase
Git
GitHub
📱 Dashboard Purpose

The dashboard acts as the central monitoring interface.

Instead of checking each sensor individually, the operator can view the overall system status through a single interface.

The dashboard can display:

Live sensor readings
Risk score
Safety status
Vision results
Alerts
Environmental conditions
Monitoring information
Firebase data
🌍 Potential Applications

AI Mine Guardian can be further developed for:

Underground mine safety monitoring
Mine inspection
Environmental monitoring
Gas-hazard detection
Worker safety monitoring
Industrial IoT safety systems
Autonomous mine inspection
Remote mine monitoring
AI-assisted emergency response
📚 Learning and Research Areas

This project combines multiple engineering and computer-science domains:

Embedded Systems
Internet of Things
Sensors and Instrumentation
Computer Vision
Artificial Intelligence
Machine Learning
Object Detection
Risk Analysis
Cloud Databases
Web Development
Robotics
Autonomous Systems
🚀 Future Enhancements
Real-time video streaming from ESP32-CAM
Advanced mine hazard detection
Worker detection and monitoring
Automated emergency alerts
GPS-based location tracking
Mine mapping and navigation
SLAM-based rover navigation
WebSocket-based real-time telemetry
Improved multimodal AI risk prediction
Autonomous mine inspection rover
Cloud-based monitoring
Historical risk-data analysis
Predictive mine-safety analytics
Remote operator control
Emergency communication system
Multiple rover coordination
📊 Project Status
Prototype Development        ✅
ESP32 Integration             ✅
Environmental Monitoring      ✅
Sensor Simulation             ✅
YOLO Integration              ✅
OpenCV Integration            ✅
Risk Engine                   ✅
Firebase Integration          ✅
Web Dashboard                 ✅
Prototype Demonstration       ✅
🎯 Project Objective

The primary objective of AI Mine Guardian is to develop an intelligent monitoring platform that can assist in identifying potentially hazardous underground mine conditions by combining IoT sensing, computer vision, and AI-based risk analysis.

The project demonstrates how embedded systems and artificial intelligence can be integrated to build a smarter and more responsive mine-safety monitoring solution.

👨‍💻 Project

AI Mine Guardian

AI-Powered Underground Mine Safety, Monitoring and Rescue System

Developed as an IoT + AI solution for intelligent underground mine monitoring and safety.

The project integrates:

Embedded Systems
       +
IoT Sensors
       +
Computer Vision
       +
Artificial Intelligence
       +
Risk Analysis
       +
Firebase
       +
Web Dashboard
📜 License

This project is intended for educational, research, and prototype development purposes.
