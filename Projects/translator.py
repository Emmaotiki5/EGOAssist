import speech_recognition as sr
from googletrans import LANGUAGES, Translator
import pyttsx3

engine = pyttsx3.init()


def exit():
    talk("Would you like to exit the translator?")
    end = input(": ").lower()
    if end == "no":
        return main()  # Start a new translation session
    elif end == "yes":
        return True  # Exit the translator
    else:
        talk("Invalid Command")
        return exit()


def talk(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def get_language_code(language_name):
    for code, name in LANGUAGES.items():
        if name.lower() == language_name.lower():
            return code
    return None


def translate_and_speak(text, target_language):
    # Translate the text
    translator = Translator(service_urls=['translate.google.com'])
    translated_text = translator.translate(text, dest=target_language).text

    # Speak the translation
    talk(translated_text)


def main():
    # Initialize speech recognition engine
    recognizer = sr.Recognizer()

    while True:
        # Ask the user for the source language
        talk("Please enter the source language.")
        source_language = input("Source Language: ").lower()

        # Check if the source language is supported
        source_language_code = get_language_code(source_language)
        if not source_language_code:
            talk("Invalid source language. Please try again.")
            continue

        # Ask the user for the target language
        talk("Please enter the language to be translated into.")
        target_language = input("Target Language: ").lower()

        # Check if the target language is supported
        target_language_code = get_language_code(target_language)
        if not target_language_code:
            talk("Invalid target language. Please try again.")
            continue

        break

    while True:
        # Capture audio input using speech recognition
        with sr.Microphone() as source:
            print("Speak now...")
            try:
                audio = recognizer.listen(source, timeout=5)
            except sr.WaitTimeoutError:
                print("Timeout. Please speak again.")
                continue
            except Exception as e:
                print("Error occurred during speech recognition:", str(e))
                continue

        # Perform speech recognition on the captured audio
        try:
            text = recognizer.recognize_google(audio, language=source_language_code)
            print("Recognized:", text)
        except Exception as e:
            print("Unable to recognize speech:", str(e))
            continue

        # Translate the recognized text and speak the translation
        translate_and_speak(text, target_language_code)

        # Ask if the user wants to exit the translator
        if exit():
            break


if __name__ == '__main__':
    main()
