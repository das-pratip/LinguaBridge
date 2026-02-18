# 🌐 LinguaBridge

**LinguaBridge** is a real-time voice translation app that converts spoken language into another using speech recognition, Google Translate, and text-to-speech. It supports dynamic language selection via MySQL and provides audio playback of translated text.

> Developed with ❤️ by **Pratip Das,Asutosh Ranjan**

---

## ✨ Features

- 🎤 **Speech Recognition**: Captures voice input using `speech_recognition`.
- 🌐 **Live Translation**: Uses `googletrans` to translate the spoken text into a target language.
- 🔊 **Text-to-Speech**: Converts the translated text to speech using `gTTS` and plays it using `playsound`.
- 🗃️ **Dynamic Language Support**: Loads supported languages and their codes from a `MySQL` database.
- ⌨️ **Fallback Input Option**: Users can type their query if voice input fails.
- ✅ **Error Handling**: Gracefully handles microphone errors, translation failures, or unknown language inputs.

---

## 🛠️ Tech Stack

- Python 3
- MySQL
- speech_recognition
- googletrans
- gTTS (Google Text-to-Speech)
- playsound
- Tkinter

---

## 📁 Project Structure

LinguaBridge/
├── main.py # Core logic for voice recognition and translation
├── requirements.txt # Python dependencies
├── data.sql # Sample SQL file to populate languages table
├── README.md # Project documentation

---

## ⚙️ Setup Instructions

### 🔧 Backend (Python)

1. **Clone the Repository**
   `git clone https://github.com/your-username/linguabridge.git`
   `cd linguabridge`

2. **Install Python Dependencies**
   `pip install -r requirements.txt`

3. **Set Up MySQL Database**
- Start your MySQL server.
- Create a database named linguabridge.
- Import the data.sql file:
   `SOURCE path/to/data.sql;`

4. **Update MySQL credentials in main.py to match your configuration:**
   `mysql.connector.connect(
       host="localhost",
       user="your_mysql_user",
       password="your_mysql_password",
       database="linguabridge"
   )`

5. **Run the Application**
   `python main.py`
   
🖥️ **Frontend (Tkinter GUI)**

*The application uses Tkinter for its graphical user interface. No separate setup is required for a web frontend.*

Steps:

- Ensure all dependencies are installed:
   `pip install -r requirements.txt`
  
- Run the GUI application directly:
   `python gui.py`
  
*The GUI allows users to register, log in, select languages, speak input, or type manually for translation.*

📦 **Example Usage**

- Launch the script.
- Speak your input when prompted.
- Select the target language by voice (e.g., "Spanish", "French").
- The translated text will be displayed and spoken aloud.
- If voice input fails, use the fallback text input field.

📚 **Use Cases**

- Real-time translation for travelers
- Language learning and pronunciation
- Multilingual conversations
- Accessibility for non-native speakers

👤 **Developer**
Developed with ❤️ by Pratip Das, Asutosh Ranjan

Feel free to fork, contribute, or connect!
