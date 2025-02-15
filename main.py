import cv2
import mediapipe as mp
import numpy as np
import json
from gesture_model import classify_gesture
from audio_feedback import speak

# Load gesture configurations
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Initialize MediaPipe Hand Tracking
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Start Video Capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # Convert to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract landmark coordinates
            landmarks = [(lm.x, lm.y) for lm in hand_landmarks.landmark]
            landmarks = np.array(landmarks).flatten().reshape(1, -1)

            # Classify the gesture
            gesture = classify_gesture(landmarks)
            if gesture in config["gestures"]:
                action = config["gestures"][gesture]
                speak(f"Action recognized: {action}")

                # Display the action on UI
                cv2.putText(frame, action, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Gesture Control", frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
