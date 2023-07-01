import speech_recognition as sr
import pyttsx3
import emailSplicer
import calculator
import time
import Diceroll
import translator

engine = pyttsx3.init(driverName='sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()


    

def start():
    
    while True:
        r = sr.Recognizer()
        

        def listen():
            with sr.Microphone() as source:
                
                print("Listening...")
                audio = r.listen(source)
                
                try:
                    text = r.recognize_google(audio)
                    print("Recognized:", text)
                    return text
                except sr.UnknownValueError:
                    print("Could not understand audio.")
                except sr.RequestError as e:
                    print("Error:", str(e))
            return ""

        
        text = listen()

        if "hello" in text:
            talk("Hello, How can I assist you today?")
        elif "split" and "email" in text:
            emailSplicer.main()
        elif ("calculate" in text) or (("start" in text) and ("calculator" in text) and ("program" in text)):
            calculator.calculate()
        elif (("roll" in text) and ("dice" in text)):
            Diceroll.roll_dice()
        elif "translate" or "Translate" in text:
            translator.main()
            
            
            
        else:
            
          talk("Sorry, I didn't catch that.")

          
def main():
    

    talk("Hello, I am EGO, your Personal Assistant. What do you need?")
    
    start()

main()
