# Forest Fire Detection System

This project simulates a pipeline for real-time forest fire detection using sensor data for temperature, humidity, and smoke levels. If thresholds indicating a fire risk are exceeded, an email alert is sent.

## Features
1. **Simulated Data Ingestion**: Randomly generates sensor data.
2. **Data Preprocessing**: Handles missing values and cleans data.
3. **Fire Detection**: Uses thresholds for temperature, humidity, and smoke levels.
4. **Alerting System**: Sends email notifications when fire is detected.

## Technologies Used
- **Python**: Core programming language.
- **NumPy & Pandas**: For data manipulation and processing.
- **SMTP**: For sending email alerts.

## How It Works
1. **Ingestion**: Generates sensor data for temperature, humidity, and smoke levels.
2. **Preprocessing**: Cleans and preprocesses data.
3. **Detection**: Checks if sensor values exceed fire thresholds.
4. **Alerting**: Sends an email alert if fire is detected.

## Prerequisites
- Python 3.7 or higher installed.
- Access to an SMTP server for sending email alerts.
- Optional: Install dependencies (NumPy, Pandas).

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
