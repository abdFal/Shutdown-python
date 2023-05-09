#pip install pyttsx3
import pyttsx3
import os

sec = 10
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# select female voice, for male voice change to [0]
engine.setProperty('voice', voices[1].id)

os.system(f'shutdown /s /t {sec}')
engine.say(f'shutting down in {sec} seconds')
engine.runAndWait