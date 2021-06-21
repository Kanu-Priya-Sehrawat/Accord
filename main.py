import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio

print("Initializing Accord ....")

MASTER = "Kanu Priya"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

# This function will wish you as per the current time
def wishMe():
    hour = (datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour<12:
        speak("Good Morning " + MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon " + MASTER)
    
    else:
        speak("Good Evening " + MASTER)

    speak("I am Accord. How may I help you?")

# This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("Listening....")
        r.energy_threshold = 4000
        audio = r.listen(source)
    
    try: 
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        print("Say that again please")
        query = None
    return query

# This function will take command and write the email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourusername@gmail.com', 'password')
    server.sendmail("yourusername@gmail.com", to, content)
    server.close()

# Main Program starts here...
speak("Initializing Accord ....")
wishMe()
query = takeCommand()

# Logic for executing tasks as per the query

if 'wikipedia' in query.lower():
    speak("Searching wikipedia....")
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results) 

elif 'open youtube' in query.lower():
    # webbrowser.open("youtube.com ")
    url = "youtube.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open google' in query.lower():
    # webbrowser.open("youtube.com ")
    url = "google.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open reddit' in query.lower():
    url = "reddit.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url) 

elif 'play music' in query.lower():
    songs_dir = "C:\\Users\\dell\\Music"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))

elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is {strTime}")

elif 'open code' in query.lower():
    codePath = "C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath) 

elif 'email to kp' in query.lower():
    try:
        speak("What should I send")
        content = takeCommand()
        to = "priyakanu1116@gmail.com"
        sendEmail(to, content)
        speak("Email send to kanu successfully")

    except Exception as e:
        print(e)