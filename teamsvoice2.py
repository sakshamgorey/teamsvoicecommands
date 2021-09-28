import speech_recognition as sr
import time
import pyttsx3
import pyautogui
from PIL import Image
from datetime import datetime
i=0
from pywinauto.application import Application
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speak(query):
    engine.say(query)
    engine.runAndWait()

def recognize_speech():
    with microphone as source:
        recognizer.pause_threshold=1
        recognizer.adjust_for_ambient_noise(source)
        recognizer.energy_threshold = 50
        recognizer.dynamic_energy_threshold = False
        audio = recognizer.listen(source, phrase_time_limit=5)
    response = ""
    
    try:
        response = recognizer.recognize_google(audio,language='en-in')
    except:
        response = "pass"
    return response
#app = Application(backend="uia").start(r'C:\Users\SaGo\AppData\Local\Microsoft\Teams\Update.exe --processStart "Teams.exe" --process-start-args "--profile=AAD"') 
speak("Script Activated")

while True:
    
    voice = recognize_speech().lower()
    print(voice)
    if 'join meeting' in voice:
        speak('yes')  
    elif 'mic' in voice:
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('shift')
        pyautogui.press('m')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shift')
    elif 'attendance' in voice:
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('shift')
        pyautogui.press('m')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shift')
        time.sleep(3)
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('shift')
        pyautogui.press('m')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shift')
    elif 'yeh hath mujhe dede thakur' in voice:
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('shift')
        pyautogui.press('k')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shift')
    elif 'yah hath mujhe nahin chahie' in voice:
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('shift')
        pyautogui.press('k')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shift')    
    elif 'leave' in voice:
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('shift')
        pyautogui.press('b')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shift')
    elif 'screenshot' in voice:
     now = datetime.now()
     dt_string = now.strftime("%d%m%Y%H%M%S")
     pyautogui.screenshot(r"C:\Users\SaGo\Pictures\Teams\teams"+str(i)+dt_string+".jpeg")
     i+=1
    elif 'terminate' in voice:
        speak('Goodbye')
        break
    
    