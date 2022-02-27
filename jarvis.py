from math import e
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# this take your voice as a command input and output is text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        print("Listining...")
        r.pause_threshold = 1
        audio = r.listen(sourse,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    
    except Exception as e:
        speak("say that again please...")
        return "none"
    return query

#wish function
def wish():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning sir")
    elif hour>12 and hour<18:
        speak("good evining sir")
    else:
        speak("good evining")
    speak("hii i am edith sir. Please tell me how can i help you")
    
if __name__ == "__main__":
    wish()
    # speak("hello nitish")
    while True:
    # if 1:
        

        query = takecommand().lower()

        #logics or command for tasks
        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
        
        elif "open adobe reader" in query:
            apath ="C:\\Program Files (x86)\\Adobe\Reader 11.0\\Reader\\AcroRd32.exe"
            os.startfile(apath)
        
        elif "open command prompt" in query:
            os.system("start cmd")
        
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img= cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        
        elif "play music" in query:
            music_dir = "E:\\manish\\guru geeta"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            for song in songs:
                if song.endswith(".mp3"):
                    os.startfile(os.path.join(music_dir,songs[0]))
                  

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP adress is {ip}")
        
        elif "wikipedia" in query:
            speak("searching wikipidia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("acording to wikipedia")
            speak(results)
            # print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
        
        elif "open gmail" in query:
            webbrowser.open("www.gmail.com")
        
        elif "open spotify" in query:
            webbrowser.open("www.spotify.com")

        elif "open google" in query:
            speak("sir, what are you looking for")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
        
        elif "send message" in query:
            kit.sendwhatmsg("+918252351746","hello",1,59)
        
        elif "play song on youtube" in query:
            speak("please let me know the name of the song")
            yc = takecommand().lower()
            kit.playonyt(f"{yc}")
        
        elif "no thanks" in query:
            speak("thanks for using me sir,have a good day. ")
            sys.exit()
        

        speak("sir, do you have any other works")