print("Script is starting...")
# Importing necessary modules required 
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
    exit()  # Stop script if imports fail

print("Script started")

try:
    conn = mysql.connector.connect(
    host="localhost",      
    user="root",  
    password="11491149@Ni",  
    database="linguabridge"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT language_name, language_code FROM languages")
    #lang_dict = {name.lower(): code for name, code in cursor.fetchall()}
    # lang_dict = tuple((name.lower(), code) for name, code in cursor.fetchall())
    # print(lang_dict)
    # print(f"Loaded {len(lang_dict)} languages from MySQL.")
    lang_dict = tuple(item for sublist in cursor.fetchall() for item in sublist)
    print(f"Loaded {len(lang_dict) // 2} languagesfromMySQL.")
except Exception as e:
    print(f"Database error: {e}")
    

  
# Capture Voice 
def takecommand():   
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        print("Listening... (speak now)") 
        r.adjust_for_ambient_noise(source)  # Reduce background noise
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5)  # Timeout after 5 seconds
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
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        return "None"
    except Exception as e: 
        print(f"Speech recognition error: {e}")
        return "None"
    return query 
  
# Input from user 
query = takecommand() 
while query == "None": 
    print("Try again or type your query below:")
    query = input("Type here: ") if input("Press 'T' to type or any key to retry: ").lower() == 't' else takecommand()
  
def destination_language(): 
    print("Speak the target language (e.g., 'French'):") 
    to_lang = takecommand() 
    while to_lang == "None": 
        to_lang = takecommand() 
    return to_lang.lower()
  
to_lang = destination_language() 
  
# Mapping it with the code 
while to_lang not in lang_dict: 
    print(f"'{to_lang}' not found. Available languages:")
    print(", ".join(lang_dict[::2]))  # Show only language names
    to_lang = destination_language() 
  
to_lang = lang_dict[lang_dict.index(to_lang) + 1]  # Get ISO code
  
# Translator 
translator = Translator() 
try:
    text_to_translate = translator.translate(query, dest=to_lang) 
    text = text_to_translate.text 
    print(f"Translation: {text}")
except Exception as e:
    print(f"Translation error: {e}")
    exit()
  
# Speak translated text
try:
    speak = gTTS(text=text, lang=to_lang, slow=False) 
    speak.save("translation.mp3") 
    playsound('translation.mp3') 
    os.remove('translation.mp3') 
except Exception as e:
    print(f"Audio error: {e}")