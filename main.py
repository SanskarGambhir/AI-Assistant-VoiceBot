import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()  # load variables from .env into environment
api_key = os.getenv("GEMINI_API_KEY")

recognizer = sr.Recognizer() # "Recognizer" helps in speech recognizing functionality

engine = pyttsx3.init() # Initialize the engine

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # Setting the voice of Assistant as female voice(change the index to '0' for male voice)
 
def speak(text): # Created a function to speak the text
  engine.say(text)
  engine.runAndWait()

# Api of Gemini
def ai(command):
  genai.configure(api_key=api_key)
  model = genai.GenerativeModel("gemini-1.5-flash")
  response = model.generate_content(command)
  print(response.text)
  return response.text

def processCommand(c):
  print(c)
  if "open google" in c.strip().lower():
    webbrowser.open("https://google.com")
  elif "open github" in c.lower():
    webbrowser.open("https://github.com/SanskarGambhir")
  elif "open chat gpt" in c.lower():
    webbrowser.open("https://chatgpt.com/")
  elif "open youtube" in c.lower():
    webbrowser.open("https://www.youtube.com/")
  elif c.lower().startswith("play"):
    song = c.lower().split(" ")[1]
    songLink = musicLibrary.songs[song]
    webbrowser.open(songLink)
  else:
    output = ai(c)
    speak(output)



if __name__ == "__main__": # This ensures that the script runs only when executed directly, not when imported as a module.
  speak("Initializing Anaconda....")

  while True:
    try:
      # Obtain audio from microphone
      with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)

      # Recognize the audio
      word = recognizer.recognize_google(audio) # Using google recognizer to recoznize the audio
      if(word.lower() == "anaconda"):
        speak("Yeah")

        # Listen for the command
        with sr.Microphone() as source:
          print("Anaconda Active...")
          audio = recognizer.listen(source)
          command = recognizer.recognize_google(audio)
          
          processCommand(command)

    except Exception as e:
      print("Google error; {0}".format(e))