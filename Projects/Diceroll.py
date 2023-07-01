import random
import pyttsx3
import speech_recognition as sr






engine = pyttsx3.init(driverName='sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
r = sr.Recognizer()

def talk(text):
    
    engine.say(text)
    engine.runAndWait()
    engine.stop()
dicedrawing = {
    1: {
        " ____________ "
        "|            |"
        "|            |"
        "|      1     |"
        "|            |"
        " ____________ "
    },
    2: {
        " ____________ "
        "|            |"
        "|            |"
        "|      2     |"
        "|            |"
        " ____________ "
    },
    3: {
        " ____________ "
        "|            |"
        "|            |"
        "|      3     |"
        "|            |"
        " ____________ "
    },
    4: {
        " ____________ "
        "|            |"
        "|            |"
        "|      4     |"
        "|            |"
        " ____________ "
    },
    5: {
        " ____________ "
        "|            |"
        "|            |"
        "|      5     |"
        "|            |"
        " ____________ "
    },
    6: {
        " ____________ "
        "|            |"
        "|            |"
        "|      6     |"
        "|            |"
        " ____________ "
    }
}
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

        
def retry(): 
    talk("Do you want to roll again")
    text = listen()
    
    if "no" in text or "not " in text:
        talk("What else do you need")
        chris = False
        return chris
        
        
        
    elif "yes" in text:
        
        return True
    else:
        talk("Invalid Command")
        retry()


def roll_dice():
    count = 1
    while True:
        talk("Ready to roll?")
        response = listen()

        if "yes" in response:
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)

            print("Dice rolled: {} and {}".format(dice1, dice2))
            talk("Your dice values are {} and {}".format(dice1, dice2))

            print("\n".join(dicedrawing[dice1]))
            print("\n".join(dicedrawing[dice2]))
            print(count)
            count = count + 1

            if not retry():
                break
        elif "no" in response:
            talk("What else do you need?")
            break
        else:
            talk("Invalid Command")
        

