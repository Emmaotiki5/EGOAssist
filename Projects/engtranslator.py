import speech_recognition as sr
from translate import Translator
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

def main():
    # Initialize speech recognition engine
    recognizer = sr.Recognizer()

    # Set the source and target languages
    source_language = 'en'  # English
    target_language = 'ja'  # Japanese

    # Initialize the translator
    translator = Translator(to_lang=source_language)

    # Capture audio input using speech recognition
    with sr.Microphone() as source:
        print("Speak now...")
        audio = recognizer.listen(source)

    # Perform speech recognition on the captured audio
    try:
        text = recognizer.recognize_google(audio, language=source_language)
        print("Recognized:", text)
    except sr.UnknownValueError:
        print("Unable to recognize speech.")
        exit()

    # Translate the recognized text to English
    translated_text = translator.translate(text)

    # Print the translated text
    print("Translated:", translated_text)

if __name__ == '__main__':
    main()
