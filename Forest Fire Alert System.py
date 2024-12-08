import pandas as pd
import numpy as np
import time
from datetime import datetime
from smtplib import SMTP

# Step 1: Simulate data ingestion
def generate_sensor_data():
    """Simulates sensor data like temperature, humidity, and smoke levels"""
    # Simulating random data for temperature, humidity, and smoke
    temperature = np.random.uniform(30, 50)  # Temperature in Celsius
    humidity = np.random.uniform(10, 90)  # Humidity percentage
    smoke_level = np.random.uniform(0, 100)  # Smoke level as a percentage
    return {
        'timestamp': datetime.now(),
        'temperature': temperature,
        'humidity': humidity,
        'smoke_level': smoke_level
    }

# Step 2: Data preprocessing (cleaning and transformation)
def preprocess_data(data):
    """Preprocess and clean the data (e.g., handle missing values)"""
    # In this case, we will just handle missing data by replacing with zeros
    cleaned_data = {key: 0 if value is None else value for key, value in data.items()}
    return cleaned_data

# Step 3: Fire detection logic based on sensor data thresholds
def detect_fire(data):
    """Detect fire based on temperature, humidity, and smoke level"""
    temperature_threshold = 45  # High temperature (°C) indicating fire risk
    smoke_threshold = 70  # Smoke level above which fire is suspected
    humidity_threshold = 30  # Low humidity indicating high fire risk

    if data['temperature'] > temperature_threshold and data['smoke_level'] > smoke_threshold and data['humidity'] < humidity_threshold:
        return True
    return False

# Step 4: Alerting system (sending email alert)
def send_alert(data):
    """Send an email alert when a fire is detected"""
    alert_message = f"Forest Fire Alert!\n\nTimestamp: {data['timestamp']}\nTemperature: {data['temperature']}°C\nHumidity: {data['humidity']}%\nSmoke Level: {data['smoke_level']}%\n\nFire detected! Please take action immediately."

    # Setup the email
    to_email = "alert@example.com"
    from_email = "fire-alert-system@example.com"
    subject = "Forest Fire Alert"
    message = f"Subject: {subject}\n\n{alert_message}"

    # Send email (this requires SMTP server settings)
    try:
        with SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login("your-email@example.com", "your-password")
            server.sendmail(from_email, to_email, message)
            print("Alert sent to:", to_email)
    except Exception as e:
        print(f"Error sending email: {e}")

# Step 5: Simulating the pipeline and running the system
def run_pipeline():
    while True:
        print("\nChecking sensor data...")
        sensor_data = generate_sensor_data()
        print(f"Generated Data: {sensor_data}")
        
        # Preprocess the data
        processed_data = preprocess_data(sensor_data)
        print(f"Processed Data: {processed_data}")
        
        # Check for fire detection
        if detect_fire(processed_data):
            print("Fire detected! Sending alert...")
            send_alert(processed_data)
        else:
            print("No fire detected.")
        
        # Simulate real-time data collection (wait for 5 seconds before next reading)
        time.sleep(5)

# Start the pipeline
if __name__ == "__main__":
    run_pipeline()
