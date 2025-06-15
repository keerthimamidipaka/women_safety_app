import geocoder
import time
import speech_recognition as sr
from twilio.rest import Client
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

# Load from .env (you would normally use os.getenv here, but credentials are omitted)
account_sid = "your_twilio_sid"
auth_token = "your_twilio_token"
twilio_number = "your_twilio_number"
emergency_contact = "+91xxxxxxxxxx"

def get_location():
    try:
        g = geocoder.ip('me')
        return f"Location: {g.latlng[0]}, {g.latlng[1]}\nMap: https://maps.google.com/?q={g.latlng[0]},{g.latlng[1]}"
    except Exception:
        return "Location not found"

def send_sms(message):
    client = Client(account_sid, auth_token)
    client.messages.create(
        body=message,
        from_=twilio_number,
        to=emergency_contact
    )
    print("Emergency SMS sent!")

def emergency_trigger():
    print("Emergency Triggered")
    location = get_location()
    alert_message = f"🚨 EMERGENCY ALERT 🚨\nPlease help! I'm in danger.\n{location}"
    send_sms(alert_message)

class EmergencyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn = Button(text="Trigger Emergency")
        btn.bind(on_press=lambda x: emergency_trigger())
        layout.add_widget(btn)
        return layout

if __name__ == "__main__":
    EmergencyApp().run()