import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import pyaudio
import smtplib

print("Initializing Atom")

MASTER="Teju"
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

#Speak funtion will pronounce the string which is passed
def speak(text):
    engine.say(text)
    engine.runAndWait()
#speak("Teju is a good girl")

#This funtion will wishyou as per the current time
def wishMe():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning"+ MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon"+ MASTER)
    
    else:
        speak("Good Evening"+ MASTER)

    speak("I am Atom. How may i help you?")

#This function will take command from microphone
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f'user said:{query}\n')
    except Exception as e:
        print("Say that again please")
        query=None
    return query

#this is smtp server and the port number is 587,to send emails we need to write this
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com",'password')
    server.sendmail('receiver@gmail.com',to,content)
    server.close()

def main():
    speak("Initializing Atom...")
    wishMe()
    query=takeCommand()

    #logic for executing tasts as per the query
    if 'wikipedia' in query.lower():
        speak("Searching wikipedia...")
        query=query.replace("wikipedia"," ")
        results=wikipedia.summary(query,sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        #webbrowser.open("youtube.com")
        url='youtube.com'
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        #webbrowser.open("google.com")
        url='google.com'
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open codechef' in query.lower():
        #webbrowser.open("codechef.com")
        url='codechef.com'
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open github' in query.lower():
        #webbrowser.open("github.com")
        url='github.com'
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open linkedin' in query.lower():
        #webbrowser.open("linkedin.com")
        url='linkedin.com'
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        songs_dir="C:\\Users\\M\\Music\\song"
        songs=os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir,songs[0]))

    elif 'time' in query.lower():
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f'{MASTER} The time is {strTime}')

    elif 'open code' in query.lower():
        codePath="C:\\Users\\M\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'email to teju' in query.lower():
        try:
            speak('what should I send?')
            content=takeCommand()
            to = 'receiver@gmail.com'
            sendEmail(to,content)
            speak('Email has been sent succesfully')
        except Exception as e:
            print(e)

main()