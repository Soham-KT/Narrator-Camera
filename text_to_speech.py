import pyttsx3

def tts_llm(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
