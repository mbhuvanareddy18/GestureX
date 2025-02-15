import streamlit as st
import cv2
import numpy as np
from gestures import detect_gesture, perform_action
from audio_feedback import speak  # Import speech function

st.title("🤖 Irha: AI Gesture Assistant")
st.write("👋 Wave at Irha to say hi! 👍 Give a thumbs-up for 'Done' and ✊ make a fist to say 'Bye'.")

# Use Streamlit session state to prevent multiple greetings
if "greeted" not in st.session_state:
    speak("Hello! I am Irha, your AI assistant. How can I help you?")
    st.session_state.greeted = True  # Set flag so it only runs once

# Open webcam inside Streamlit
cap = cv2.VideoCapture(0)
frame_placeholder = st.empty()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    detected_gesture = detect_gesture(rgb_frame)

    if detected_gesture:
        perform_action(detected_gesture)

    # Display webcam feed in Streamlit
    frame_placeholder.image(rgb_frame, channels="RGB")

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
