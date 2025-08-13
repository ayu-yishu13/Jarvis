import pyttsx3
import speech_recognition as sr
import eel
import time

#voice speak
def speak(text):
    
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150) 
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()

#text-takecommand
def takecommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening....")
        eel.DisplayMessage("Listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)
        
    try:
        print("Recognizing.....")
        eel.DisplayMessage("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query} ")
        eel.DisplayMessage(query)
        time.sleep(2)
        
        
    except Exception as e:
        return " "
    
    return query.lower()

@eel.expose
def allCommands():
    
    try:
        query = takecommand()
        print(query)
    
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        
        elif "on youtube":
            from engine.features import PlayYoutube
            PlayYoutube(query)
        
        else:
            print("I not run")
        
        eel.ShowHood()
        
    except:
        print("error")
        