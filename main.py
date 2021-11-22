#.\env\Scripts\activate

import pyttsx3
import speech_recognition as sr
#import pyaudio
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)  # change id for  changing  voice


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("user said: {query}")
    except Exception as e:
        speak("Say that again please...")
        return 'none'


if __name__ == "__main__":
    takecommand()
    speak("Hello Sir  Jarvis is reporting sir...")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
