print("Script is starting...")

# Importing necessary modules
try:
    from playsound import playsound
    import speech_recognition as sr
    from googletrans import Translator
    from gtts import gTTS
    import os
    import mysql.connector
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    print("All imports successful")
except Exception as e:
    print(f"Import error: {e}")
    exit()

print("Script started")

# Load language dictionary
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="11491149@Ni",
        database="linguabridge"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT language_name, language_code FROM languages")
    lang_dict = tuple(item for sublist in cursor.fetchall() for item in sublist)
    print(f"Loaded {len(lang_dict) // 2} languages from MySQL.")
except Exception as e:
    print(f"Database error: {e}")
    lang_dict = ()

def get_lang_code(language_name):
    try:
        index = lang_dict.index(language_name.lower())
        return lang_dict[index + 1]
    except ValueError:
        return None

# Capture voice
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... (speak now)")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5)
            print("Processing...")
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
            return "None"
        except Exception as e:
            print(f"Microphone error: {e}")
            return "None"

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
    except Exception as e:
        print(f"Speech recognition error: {e}")
    return "None"

# Translate and speak
def translate_and_speak(query, target_language):
    to_lang_code = get_lang_code(target_language)
    if not to_lang_code:
        print(f"Language '{target_language}' not found.")
        print("Available languages:", ", ".join(lang_dict[::2]))
        return