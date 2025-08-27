import speech_recognition as sr
import musicLibrary
import subprocess
import webbrowser
import pyttsx3
import ctypes
import os
from google import genai



recognizer = sr.Recognizer()
client = genai.Client(api_key="AIzaSyCsUwqQIj7o9zt0hX8MQLQdBCawYR4hNrs")

# ---------------------- SPEAK FUNCTION
def speak(text):
    print(f"Vikram: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ------------------- GEMINI AI PROCESS
def aiProcess(command):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=command
        )
        return response.text
    except Exception as e:
        return f"Sorry, I couldn't process that. Error: {str(e)}"

# ------------------------ PROCESS COMMAND FUNCTION
def processCommand(c):
    c = c.lower()

    # ----- open websites
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open youtube" in c or "open you tube" in c:
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c or "open face book" in c:
        webbrowser.open("https://youtube.com")
    elif "open hackerrank" in c or "open hacker rank" in c:
        webbrowser.open("https://www.hackerrank.com/dashboard")
    elif "open code chef" in c or "open codechef" in c:
        webbrowser.open("https://www.codechef.com/users/bikramghosh")
    elif "open chat gpt" in c or "open chargpt" in c:
        webbrowser.open("https://chatgpt.com/?model=auto")
    elif "open deep seek" in c or "open deepseek" in c:
        webbrowser.open("https://chat.deepseek.com/")


    # ----- system apps
    elif "open notepad" in c:
        os.system("notepad")
    elif "open calculator" in c:
        subprocess.Popen("calc.exe")
    elif "open cmd" in c or "open command prompt" in c:
        os.system("start cmd")
    elif "open task manager" in c:
        os.system("taskmgr")
    elif "open camera" in c:
        os.system("start microsoft.windows.camera:")
    elif "open chrome" in c:
        subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    elif "open brave" in c:
        subprocess.Popen(r"C:\Users\bikra\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe")
    elif "open settings" in c:
        os.system("start ms-settings:")
    elif "open vs code" in c or "open visual studio code" in c:
        subprocess.Popen([r"C:\Users\bikra\AppData\Local\Programs\Microsoft VS Code\Code.exe"])


    # ----- system control
    elif "shutdown system" in c or "shut down system" in c:
        os.system("shutdown /s /t 1")   
    elif "restart system" in c:
        os.system("shutdown /r /t 1")
    elif "lock system" in c:
        ctypes.windll.user32.LockWorkStation()

    # ------- play music
    elif c.lower().startswith("play"):
            try:
                song = c.replace("play", "", 1).strip()
                if song in musicLibrary.music:
                        link = musicLibrary.music[song]
                        webbrowser.open(link)
                        speak(f"Playing {song}")
            except Exception:
                speak("Sorry, I could not find that song.")

    # ------- use AI
    else:
        speak(aiProcess(c))

# ---------------------------- MAIN LOOP
if __name__ == "__main__":
    speak("Initializing Vikram.....")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word.....")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
            word = recognizer.recognize_google(audio)

            if word.lower() == "vikram":
                speak("Yes Sir!")
                
                with sr.Microphone() as source:
                    print("Vikram Active, listening for command.....")
                    audio = recognizer.listen(source, timeout=6, phrase_time_limit=6)
                    command = recognizer.recognize_google(audio)
                    print(f"Command received: {command}")
                    processCommand(command)

        except Exception as e:
            print(f"Error: {e}")
