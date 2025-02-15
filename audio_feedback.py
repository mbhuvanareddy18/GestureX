from gtts import gTTS
import pyttsx3
import os
import time

def speak(text):
    """Speaks text aloud using gTTS (online) or pyttsx3 (offline)."""
    try:
        print(f"🗣 Irha says: {text}")  # Debugging: See if the function runs

        # Try gTTS first
        filename = f"audio_{int(time.time())}.mp3"
        tts = gTTS(text=text, lang="en", slow=False)
        tts.save(filename)

        # Play the generated speech
        os.system(f"start {filename}")  # Windows audio playback
        time.sleep(3)  # Wait for the speech to finish
        os.remove(filename)  # Clean up
    except Exception as e:
        print(f"⚠️ gTTS failed! Using offline TTS: {e}")
        
        # Use offline pyttsx3
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
