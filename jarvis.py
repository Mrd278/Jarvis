import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import roman

numbers = {'hundred':100, 'thousand':1000, 'lakh':100000}
a = {'':''}
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
    server.login('youremail.com', 'password')
    server.sendmail('youremail@gmail.com', to, content)
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
        r.energy_threshold = 1000
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
        if 'exit' in query:
            speak("Bye sir")
            print("Bye sir")
            break

        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    print(results)
                    speak(results)
                except Exception as e:
                    speak('sorry sir could not find any results')

        elif 'open youtube' in query:
            speak('opening Youtube')
            webbrowser.open("youtube.com")

        elif 'open course error' in query:
            speak('opening course era')
            webbrowser.open("coursera.com")

        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("google.com")

        elif 'hello' in query:
            speak("Hello Sir")

        elif 'open stackoverflow' in query:
            speak('opening stackoverflow')
            webbrowser.open('stackoverflow.com')

        elif ('play music' in query) or ('change music' in query):
            speak('Here are your favorites')
            music_dir = 'D:\My Music'
            songs = os.listdir(music_dir)
            n = random.randint(0, 27)
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir the time is %s" %strtime)
            print("Sir the time is %s" % strtime)

        elif 'the date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            speak("Sir today's date is %s" %strdate)
            print("Sir today's date is %s" %strdate)

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

        elif 'your name' in query:
            speak('myself Jarvis sir')


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
		
        elif "open python" in query:
            speak('opening python Ide')
            os.startfile('C:\\Users\\mridu\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.7\\IDLE (Python 3.7 64-bit)')

        elif 'open code blocks' in query:
            speak('opening Codeblocks')
            os.startfile("C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe")

        elif 'open anaconda' in query:
            speak('opening anaconda')
            os.startfile("C:\\Users\\mridu\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Anaconda Navigator")

        elif 'calculation' in query:
            sum = 0
            speak('Yes Sir, please tell the numbers')
            while True:
                query = takeCommand()
                if 'answer' in query:
                    speak('here is result'+str(sum))
                    print(sum)
                    break
                elif query:
                    if query == 'x**':
                        digit = 30
                    elif query in numbers:
                        digit = numbers[query]
                    elif 'x' in query:
                        query = query.upper()
                        digit = roman.fromRoman(query)
                    elif query.isdigit():
                        digit = int(query)
                    else:
                        digit = 0
                    sum += digit
