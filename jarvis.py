import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib


a = {'mridul':'mridul27gupta@gmail.com'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

'''
Speak Function is used to speak a sentence
'''
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
'''
Sends email to person
'''
def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('med6hmaasm@gmail.com', 'hmaasm12345')
    server.sendmail('med6hmaasm@gmail.com', to, content)
    server.close()

'''
Wishes the customer and introduce itself
'''
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning Mridul!")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon Mridul!")
    else:
        speak("Good Evening Mridul!")
    speak("Myself Jarvis! How may I help you sir")

'''
Takes command from the user and returns it as a string
'''
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query, "\n")
    except Exception as e:
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'quit' in query:
            speak("Bye sir")
            print("Bye sir")
            break

        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                speak("searching wikipedia")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'hello' in query:
            speak("Hello Sir")

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif ('play music' in query) or ('change music' in query):
            music_dir = 'D:\My Music'
            songs = os.listdir(music_dir)
            n = random.randint(0, 27)
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir the time is %s" %strtime)
            print("Sir the time is %s" % strtime)

        elif 'thank you' in query:
            speak("Welcome Sir")

        elif 'can you do for me' in query:
            speak('I can do multiple tasks for you sir. tell me whatever you want to perform sir')

        elif 'old are you' in query:
            speak('I am 19 years old')

        elif 'open media player' in query:
            speak("opening V L C media player")
            path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(path)

        elif 'open pycharm' in query:
            speak("Opening Pycharm")
            path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2018.3.2\\bin\\pycharm64.exe"
            os.startfile(path)

        elif 'open chrome' in query:
            speak("Opening Google Chrome")
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)

        elif 'email to me' in query:
            try:
                speak('what should I say')
                content = takeCommand()
                to = a['mridul']
                sendemail(to, content)
                speak('Email has been sent!')

            except Exception as e:
                print(e)
                speak('Sorry! I was not able to send this email')
b = input()