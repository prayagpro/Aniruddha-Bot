import speech_recognition as sr
import pyttsx3
import pyjokes
import webbrowser

# Initialize the text-to-speech engine
def speechtxt(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

# Listen for user input via microphone
def sptext():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening for your command...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                print("Recognizing...")
                data = recognizer.recognize_google(audio)
                data = data.lower()
                print(f"You said: {data}")
                return data
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand what you said.")
                return None
    except Exception as e:
        print(f"An error occurred with the microphone: {e}")
        return None

# Get a joke
def tell_joke():
    return pyjokes.get_joke()

if __name__ == "__main__":
    assistant_name = "Aniruddha"
    assistant_age = "I was created just today."
    creation_date = "21st December 2024."
    owner = "Prayag"
    difference = "I am smarter than most other assistants."

    print(f"{assistant_name} is now active. Say 'Hey {assistant_name}' to start.")
    while True:
        command = sptext()
        if command and f"hey {assistant_name.lower()}" in command:
            speechtxt(f"Yes, Sir. How can I assist you?")
            while True:
                task = sptext()
                if task:
                    if "your name" in task:
                        speechtxt(f"My name is {assistant_name}.")
                    elif "your age" in task:
                        speechtxt(f"{assistant_age}")
                    elif "tell me a joke" in task:
                        joke = tell_joke()
                        speechtxt(joke)
                    elif "when were you created" in task:
                        speechtxt(f"I was created on {creation_date}.")
                    elif "who created you" in task or "your owner" in task:
                        speechtxt(f"I was created by {owner}.")
                    elif "how are you different" in task:
                        speechtxt(f"{difference}")
                    elif "open youtube" in task:
                        speechtxt("Opening YouTube.")
                        webbrowser.open("https://www.youtube.com")
                    elif "open linkedin" in task:
                        speechtxt("Opening LinkedIn.")
                        webbrowser.open("https://www.linkedin.com")
                    elif "open github" in task:
                        speechtxt("Opening GitHub.")
                        webbrowser.open("https://www.github.com")
                    elif "exit" in task:
                        speechtxt("Goodbye, Sir. Have a great day!")
                        exit()
                    else:
                        speechtxt("I did not understand that. Could you please repeat?")
                else:
                    speechtxt("I didn't catch that. Please try again.")