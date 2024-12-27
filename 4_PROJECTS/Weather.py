# Weather App by Akash Halder
import requests
import json
import win32com.client as wincom

API_KEY = "dc5799ac63574ee9a66182700230807"
speak = wincom.Dispatch( "SAPI.SpVoice" )
print("Hello there! Welcome to Akash's Weather App  🌦️")
# print( "============ Welcome to Akash's Weather App (version=1.1.1) ===========" )
speak.Speak("Hello there!Welcome to Akash's Weather App")
# speak.Speak( "Enter the name of your city:" )


while True:

    try:
        print("=================== Akash's Weather App (version=1.1.1) ==================")
        print("🌡️  To know the temperature of your  city please enter the name of your  city: \n")
        print( "To Exit the weather app type 'exit' in input:" )
        speak.Speak("To know the temperature of your city please enter the name of your  city:")
        city = str(input("Enter the name of your country / city: \n"))



        url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"


        if (city == "exit"):
            print("Bye Bye my friend 👋 \nThanks for using  the Weather App.")
            speak.Speak("Bye Bye my friend. \nThanks for using  the Weather App.")
            break
        r = requests.get(url)
        wdic = json.loads(r.text)
        w = (wdic["current"]["temp_c"])

        print(f"The current temperature in {city} is {w} degrees Celsius")
        speak.Speak(f"The current temperature in{city} is {w} degrees Celsius")

    except:
        print("Sorry!Something went wrong... try again 🔃",)
        speak.Speak("Sorry!Something went wrong... try again")

# This app is built by Akash using Pure Python Only...Not any other extensions excluding modules