# 🛡️ Women Safety App

A Python + Kivy-based emergency alert system that triggers with a button or voice command and sends SMS alerts with your live location.

## 🚀 Features
- 🎤 Voice command activation ("help")
- 🖱️ GUI with emergency button (Kivy)
- 📍 Live location detection using IP
- 📩 Sends emergency SMS using Twilio API

## 📦 Technologies
- Python
- Kivy (for GUI)
- Geocoder (for location)
- SpeechRecognition (for voice trigger)
- Twilio (for SMS)

## ⚙️ Setup Instructions

1. Clone this repo
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your Twilio credentials inside the script or use a `.env` file
4. Run the app:

```bash
python women_safety_kivy.py
```

## ⚠️ Note
This is a demo project. Do not publish real credentials. Always secure your `.env` file.