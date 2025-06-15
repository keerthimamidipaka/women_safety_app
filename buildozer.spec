[app]
title = Women Safety App
package.name = safety
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = kivy, geocoder, twilio, SpeechRecognition, pyaudio, python-dotenv
orientation = portrait
fullscreen = 1
android.permissions = INTERNET, RECORD_AUDIO, SEND_SMS, ACCESS_FINE_LOCATION
android.api = 30
android.minapi = 21
android.sdk = 30
android.ndk = 21b
android.private_storage = 1