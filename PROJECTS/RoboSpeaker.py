import win32com.client as wincom #Install this library using => pip install pywin32

speak = wincom.Dispatch( "SAPI.SpVoice" )

if __name__ == '__main__':
    while (True):
        print("=================== 🤖 Welcome to RoboSpeaker v-1.1 created by AKASH 🤖  ====================================")
        print("Press \"q \" to stop the program")
        x = input("Enter what you want me to speak: ")
        command = speak.Speak(f"{x}")
        if x == "q":
            speak.Speak("Bye Bye my Friend...I will miss you ")
            break
    
