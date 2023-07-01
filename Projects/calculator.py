import pyttsx3
import random
import speech_recognition as sr

engine = pyttsx3.init(driverName='sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
r = sr.Recognizer()


def talk(text):
    engine.say(text)
    engine.runAndWait()


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


def add(number1, number2):
    summation = number1 + number2
    return summation


def subtraction(number1, number2):
    difference = number1 - number2
    return difference


def multiply(number1, number2):
    product = number1 * number2
    return product


def invalid():
    talk("Do you want to exit calculator")
    redo = listen()
    if redo == "Yes" or redo == "yes":
        talk("What else do you need")
        return False
    elif redo == "no" or redo == "No":
        return True
    else:
        talk("Invalid Command")
        return invalid()


def calculate():
    while True:
        num1 = input("First Number:")
        sign = input("sign:")
        num2 = input("Second Number:")
        no1 = int(num1)
        no2 = int(num2)

        if sign == "+":
            answer = add(no1, no2)
            print(answer)
            if not invalid():
                break

        elif sign == "-":
            answer = subtraction(no1, no2)
            print(answer)
            if not invalid():
                break

        elif sign == "*":
            answer = multiply(no1, no2)
            print(answer)
            if not invalid():
                break



