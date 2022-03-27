import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis Maam. Please tell me how may I help you!")
    
def takeCommand(): # It takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        #audio=r.listen(source)
        audio=r.listen(source,timeout=8,phrase_time_limit=8)
    try:
        print('Recognizing...')
        query=r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print(e)
        print('Say that again please...')
        return "None"
    return query

if __name__=="__main__":
    speak("Hello Sadhana")
    WishMe()
    if 1:
        query=takeCommand().lower()
    
    # Logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query, sentences=2)
        speak("Accordig to wikipedia")
        print(results)
        speak(results)
    
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'play music' in query:
        music_dir="C:\\Python\\Jarvis-Music"
        songs=os.listdir(music_dir)
        print(songs)
        q=random.randint(0,4)
        os.startfile(os.path.join(music_dir, songs[q]))


        
