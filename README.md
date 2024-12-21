# Aniruddha: Personal AI Assistant 🤖

Aniruddha is a voice-controlled personal AI assistant designed to make daily tasks easier and more interactive. Built with Python, it integrates text-to-speech, speech recognition, and various APIs to deliver a personalized experience.

## ✨ Features

### General Functionality
- **Introduces Itself:**  
  Responds to "What is your name?" with "My name is Aniruddha."
- **Personalized Details:**  
  Shares its creation date and creator’s name, and explains why it’s different from other assistants.

### Task-Specific Features
- **Joke Telling:**  
  Responds to "Tell me a joke" with a random programming-related joke.
- **Website Navigation:**  
  Opens popular websites:
  - YouTube: `"Open YouTube"`
  - LinkedIn: `"Open LinkedIn"`
  - GitHub: `"Open GitHub"`
- **Voice-Controlled Interaction:**  
  Listens for commands using the wake word: `"Hey Aniruddha"`.
- **Graceful Exit:**  
  Ends the session when `"exit"` is spoken.

---

## 🚀 How to Run

### Prerequisites
1. **Install Python 3.9 or above.**  
2. **Install required libraries:**  
   ```bash
   pip install pyttsx3 pyjokes speechrecognition
   ```

### Running the Assistant
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/aniruddha-ai-assistant.git
   cd aniruddha-ai-assistant
   ```
2. Run the Python script:
   ```bash
   python assistant.py
   ```
3. Speak commands like:
   - `"Hey Aniruddha"`
   - `"Tell me a joke"`
   - `"Open YouTube"`

---

## 🎙️ Example Commands

- **Activation:**  
  - Command: `"Hey Aniruddha"`  
  - Response: `"Yes, Sir. How can I assist you?"`

- **Joke:**  
  - Command: `"Tell me a joke"`  
  - Response: `"Why do programmers prefer dark mode? Because light attracts bugs!"`

- **Website Navigation:**  
  - Command: `"Open YouTube"`  
  - Response: Opens YouTube in your default browser.

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **Libraries:**
  - `speechrecognition`: For capturing and processing voice input.
  - `pyttsx3`: For converting text to speech.
  - `pyjokes`: For generating random jokes.
  - `webbrowser`: For opening websites.

---

## 🔮 Future Enhancements
- Integration with weather APIs for live weather updates.  
- Adding a to-do list or task manager.  
- Support for more commands and languages.  
- Integration with AI models for conversational abilities.

---

## 👤 Creator
- **Owner:** Prayag  
- **Assistant Name:** Aniruddha  
- **Creation Date:** 21st December 2024  

---

**Disclaimer:** This project is a work in progress and is built for learning purposes. Contributions are welcome!  
