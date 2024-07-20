import time
from plyer import notification
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

speak.Speak("Enter the hours interval you want to drink water")
time_hour = float(input("Enter the hours interval you want to drink water: "))

while True:
    time.sleep(3600 * time_hour)
    notification.notify(
        title="Water",
        message="Akash!! It's Time to drink water",
        timeout=10
    )
    speak.Speak("Akash!! It's Time to drink water")
