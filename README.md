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
