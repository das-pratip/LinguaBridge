# LinguaBridge
LinguaBridge is a real-time voice translation app that converts spoken language into another using speech recognition, Google Translate, and text-to-speech. It supports dynamic language selection via MySQL and provides audio playback of translated text.
Developed by **Pratip Das**

---

## ✨ Features

- 🎤 **Speech Recognition**: Captures voice input using `speech_recognition`.
- 🌐 **Live Translation**: Uses `googletrans` to translate the spoken text into a target language.
- 🔊 **Text-to-Speech**: Converts the translated text to speech using `gTTS` and plays it using `playsound`.
- 🗃️ **Dynamic Language Support**: Loads supported languages and their codes from a MySQL database.
- ⌨️ **Fallback Input Option**: Users can type their query if voice input fails.
- ✅ **Error Handling**: Gracefully handles issues like microphone errors, translation failures, or unknown language inputs.

---

## 🛠️ Tech Stack

- **Python 3**
- **MySQL**
- **speech_recognition**
- **googletrans**
- **gTTS (Google Text-to-Speech)**
- **playsound**
- **ReactJS**

---

## 📁 Project Structure

LinguaBridge/
├── main.py # Core logic for voice recognition and translation
├── requirements.txt # Python dependencies
├── data.sql # Sample SQL file to populate languages table
├── README.md # Project documentation
├── frontend/ #  React-based UI 
│ └── ...

---

## ⚙️ Setup Instructions

### 🔧 Backend (Python)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/linguabridge.git
   cd linguabridge
Install Python dependencies:


pip install -r requirements.txt
Set up MySQL database:

Start your MySQL server.

Create a database named linguabridge.

Import the data.sql file using your SQL client or command line:
SOURCE path/to/data.sql;
Update the credentials in main.py to match your MySQL configuration.

Run the app:
python main.py
🖥️ Frontend
Navigate to the frontend folder:
cd frontend
Install dependencies and start the React app:

npm install
npm start
📦 Example Usage
Launch the script.

Speak your input when prompted.

Select the target language by voice (e.g., "Spanish", "French").

The translated text will be displayed and spoken aloud.

If no voice is detected, use the fallback text input.

📚 Use Cases
Real-time translation for travelers

Language learning and pronunciation

Multilingual conversations

Accessibility for non-native speakers

📜 License
This project is licensed under the MIT License.

👤 Developer
Developed with ❤️ by Pratip Das

Feel free to fork, contribute, or connect!


---

Let me know your name so I can finalize it for you!







