import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import pyautogui
import random

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)
    print(f"The current time is {Time}")

def date():
    Date = datetime.datetime.now().strftime("%d %B %Y")
    speak("The current date is")
    speak(Date)
    print(f"The current date is {Date}")

def wishme():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good Morning Sir!!")
        print("Good Morning Sir!!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!!")
        print("Good Afternoon Sir!!")
    elif 18 <= hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        speak("Good Night Sir!!")
        print("Good Night Sir!!")
    speak("Jarvis at your service sir, please tell me how may I help you.")

def screenshot():
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("~\\Pictures\\ss.png")
    img.save(img_path)
    print(f"Screenshot saved at {img_path}")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
    except Exception as e:
        print(e)
        speak("Please say that again.")
        return "Try Again"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "who are you" in query:
            speak("I'm JARVIS created by Mr. Kishan and I'm a desktop voice assistant.")
            print("I'm JARVIS created by Mr. Kishan and I'm a desktop voice assistant.")
        elif "how are you" in query:
            speak("I'm fine sir, What about you?")
            print("I'm fine sir, What about you?")
        elif "fine" in query or "good" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")
        elif "wikipedia" in query:
            try:
                speak("Ok wait sir, I'm searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else.")
        elif "open youtube" in query:
            wb.open("youtube.com")
        elif "open google" in query:
            wb.open("google.com")
        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")
        elif "play music" in query:
            song_dir = os.path.expanduser("~\\Music")
            songs = os.listdir(song_dir)
            if songs:
                song = random.choice(songs)
                os.startfile(os.path.join(song_dir, song))
            else:
                speak("No music files found in your Music folder.")
        elif "open chrome" in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)
        elif "search on chrome" in query:
            try:
                speak("What should I search?")
                search = takecommand()
                chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                wb.get(chromePath).open_new_tab(search)
                print(search)
            except Exception as e:
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")
        elif "remember that" in query:
            speak("What should I remember?")
            data = takecommand()
            speak(f"You told me to remember that: {data}")
            print(f"You told me to remember that: {data}")
            with open("data.txt", "w") as remember:
                remember.write(data)
        elif "do you remember anything" in query:
            try:
                with open("data.txt", "r") as remember:
                    data = remember.read()
                    speak(f"You told me to remember that: {data}")
                    print(f"You told me to remember that: {data}")
            except FileNotFoundError:
                speak("I don't remember anything yet.")
                print("I don't remember anything yet.")
        elif "screenshot" in query:
            screenshot()
            speak("I've taken the screenshot, please check it.")
        elif "offline" in query:
            speak("Going offline. Goodbye, sir!")
            quit()
