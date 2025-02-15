import cv2
import mediapipe as mp
import pyautogui
import streamlit as st
from audio_feedback import speak

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Improve hand tracking sensitivity
hands = mp_hands.Hands(
    min_detection_confidence=0.5,  # Lower threshold to detect more hands
    min_tracking_confidence=0.5,
    max_num_hands=1  # Ensure only one hand is detected for efficiency
)

def detect_gesture(frame):
    """Detects hand gestures from a webcam frame."""
    results = hands.process(frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Convert landmarks to a list of (x, y) coordinates
            landmarks = [(lm.x, lm.y) for lm in hand_landmarks.landmark]

            # Gesture Mapping
            if landmarks[0][1] < landmarks[9][1]:  # Open Palm (Waving Hi)
                return "Wave"
            elif landmarks[4][0] > landmarks[3][0]:  # Thumbs Up
                return "Thumbs Up"
            elif landmarks[4][0] < landmarks[3][0]:  # Thumbs Down
                return "Thumbs Down"
            elif landmarks[0][1] > landmarks[9][1]:  # Fist Gesture (Bye)
                return "Bye"
    
    return None  # No gesture detected

def perform_action(gesture):
    """Performs system actions based on detected gestures."""
    if gesture == "Wave":
        speak("Hi! How can I help you?")
        st.success("👋 Irha: Hi! How can I help you?")
    elif gesture == "Thumbs Up":
        speak("Done!")
        st.success("👍 Irha: Done!")
    elif gesture == "Bye":
        speak("Bye! See you soon!")
        st.success("✋ Irha: Bye! See you soon!")
        exit()
