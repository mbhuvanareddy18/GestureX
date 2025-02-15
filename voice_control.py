import speech_recognition as sr

recognizer = sr.Recognizer()

def recognize_voice():
    """Recognizes user voice and converts it into text."""
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=10)
            command = recognizer.recognize_google(audio)
            return command.lower()
        except sr.WaitTimeoutError:
            print("⏳ No speech detected.")
        except sr.UnknownValueError:
            print("🔇 Could not understand.")
        except sr.RequestError:
            print("❌ No internet connection.")
    return None
