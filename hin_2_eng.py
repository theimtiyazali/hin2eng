import speech_recognition as sr
from googletrans import Translator
from datetime import datetime, time

def get_current_time():
    return datetime.now().time()

def is_within_time_window():
    start_time = time(18, 0)  # 6 PM
    end_time = time(23, 59)   # Midnight
    current_time = get_current_time()
    return start_time <= current_time <= end_time

def translate_to_hindi(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='hi')
    return translated.text

def process_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")

        if not is_within_time_window():
            print("Please try after 6 PM IST.")
            return

        if text.startswith(('M', 'O')):
            print(f"Translation skipped for words starting with 'M' or 'O'. You said: {text}")
        else:
            hindi_translation = translate_to_hindi(text)
            print(f"Translated to Hindi: {hindi_translation}")

    except sr.UnknownValueError:
        print("Sorry, I did not understand the audio. Please repeat.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

if __name__ == "__main__":
    while True:
        process_audio()
        user_input = input("Do you want to translate another word? (yes/no): ").strip().lower()
        if user_input != 'yes':
            break
