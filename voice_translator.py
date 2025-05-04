import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from googletrans import Translator
import os
import mysql.connector
from config import DB_CONFIG

def load_languages():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT language_name, language_code FROM languages")
        lang_dict = {name.lower(): code for name, code in cursor.fetchall()}
        conn.close()
        return lang_dict
    except Exception as e:
        print(f"[DB Error] Failed to load languages: {e}")
        return {}

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=5)
            print("Processing voice...")
            return r.recognize_google(audio, language='en-in')
        except sr.WaitTimeoutError:
            print("Timeout: No voice detected.")
        except sr.UnknownValueError:
            print("Speech not recognized.")
        except Exception as e:
            print(f"[Speech Error] {e}")
    return "None"

def translate_and_speak(text, to_lang_code):
    try:
        translator = Translator()
        translated = translator.translate(text, dest=to_lang_code).text
        print(f"Translated Text: {translated}")

        speak = gTTS(text=translated, lang=to_lang_code)
        filename = "translation.mp3"
        speak.save(filename)
        playsound(filename)
    except Exception as e:
        print(f"[Translation Error] {e}")
        return "Translation failed."
    finally:
        try:
            if os.path.exists("translation.mp3"):
                os.remove("translation.mp3")
        except Exception as e:
            print(f"[Cleanup Error] Failed to remove translation.mp3: {e}")
    return translated