import tensorflow as tf
import numpy as np

# Load the trained model
model = tf.keras.models.load_model("gesture_model.keras")

# Gesture labels
gesture_labels = {0: "Swipe Left", 1: "Swipe Right", 2: "Fist", 3: "Thumbs Up", 4: "Open Palm"}

def classify_gesture(landmarks):
    """Classifies the hand gesture using the trained model."""
    prediction = model.predict(landmarks)
    predicted_index = np.argmax(prediction)
    return gesture_labels.get(predicted_index, "Unknown")
