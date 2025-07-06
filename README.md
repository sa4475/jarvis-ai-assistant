# 🤖 Jarvis AI Assistant

A smart and customizable desktop voice assistant built using **Python**, **Eel**, **HTML/CSS**, and **JavaScript**. Jarvis helps you control your PC and mobile with simple **voice** or **typed commands**.

From launching apps to making calls and chatting, Jarvis brings AI and automation to your fingertips.

---

## ✨ Features

- 🎙️ **Voice & Text Control** - Control your system with voice commands or typing
- 🔐 **Face Authentication** - Secure access with facial recognition
- 📞 **Phone Integration** - Make and manage phone calls via mobile (Android)
- 💻 **Application Launcher** - Launch desktop applications with voice commands
- 🌐 **Web Navigation** - Open your favorite URLs and websites
- 📔 **Contact Management** - Built-in phone book and contact storage
- 🙋 **Personal Details** - Store and use your personal information
- 🤖 **AI Chat** - Interactive chat capabilities
- 🎵 **Media Control** - Play videos/songs on YouTube & Spotify
- 🌤️ **Weather Updates** - Get real-time weather information
- 🎯 **System Control** - Control various system functions

---

## 🛠️ Tech Stack

- **Python** – Core logic and AI processing
- **Eel** – Web-Python integration framework
- **HTML/CSS/JavaScript** – Interactive web frontend
- **OpenCV** – Face recognition and computer vision
- **Speech Recognition** – Voice command processing
- **Text-to-Speech** – Voice response system

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sa4475/jarvis-ai-assistant.git
cd jarvis-ai-assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Face Recognition (Optional)

If you want to use face authentication:

1. Navigate to `engine/auth/samples/`
2. Add your face images (multiple angles recommended)
3. Run the training script:
   ```bash
   python engine/auth/trainer.py
   ```

### 4. Run Jarvis

```bash
python run.py
```

---

## 🚀 Usage

1. **Start the Application**: Run `python run.py`
2. **Face Authentication**: Complete face recognition setup
3. **Voice Commands**: Use voice commands to interact with Jarvis
4. **Web Interface**: Access the web interface at `http://localhost:8000`

### Example Voice Commands

- "Open Chrome"
- "What's the weather?"
- "Play music on Spotify"
- "Make a phone call"
- "What time is it?"

---

## 📁 Project Structure

```
jarvis-ai-assistant/
├── engine/
│   ├── auth/           # Face recognition system
│   ├── command.py      # Command processing
│   ├── config.py       # Configuration settings
│   ├── db.py          # Database operations
│   ├── features.py     # Core features
│   └── helper.py      # Helper functions
├── www/               # Web interface files
├── main.py           # Main application entry
├── run.py            # Application runner
└── requirements.txt   # Python dependencies
```

---

## 🔧 Configuration

- **Voice Settings**: Modify voice parameters in `engine/config.py`
- **Face Recognition**: Configure face detection in `engine/auth/`
- **Web Interface**: Customize UI in `www/` directory
