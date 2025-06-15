# 👩‍🦺 Women Safety Kivy App

A voice-activated emergency alert app built using Python, Kivy, and Twilio. This app listens for the word "help" and sends your live location via SMS to an emergency contact.

## 🚀 Features
- Voice detection for the keyword **"help"**
- Sends GPS location using **geocoder**
- Sends SMS alerts using **Twilio**
- Designed with **Kivy** for cross-platform (Android-ready)
- Compatible with **Buildozer** for Android packaging

## 🛠️ Requirements

Install dependencies with:

```
pip install -r requirements.txt
```

You also need to install `pyaudio` (may require system packages):

```
# For Linux (Debian/Ubuntu)
sudo apt-get install portaudio19-dev python3-pyaudio
```

## 🔐 Environment Variables

Create a `.env` file with your credentials:

```
TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE=your_twilio_phone_number
```

## 📱 Build Android APK

Using Buildozer:

```
buildozer init
# (Edit buildozer.spec as needed)
buildozer -v android debug
```

> Permissions required: `INTERNET`, `RECORD_AUDIO`, `SEND_SMS`, `ACCESS_FINE_LOCATION`

## 📂 File Structure

```
.
├── women_safety_kivy.py     # Main Python app
├── requirements.txt         # Python dependencies
├── .env.example             # Sample environment file
└── buildozer.spec           # Android build configuration
```

## 💡 Future Enhancements

- Add camera/panic button
- Store emergency contacts in file or DB
- UI improvements

---

👨‍💻 Developed with 💖 using Python & Kivy