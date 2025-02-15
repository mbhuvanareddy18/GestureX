# Irha: The Gesture-Based Kiosk Interaction System

This project implements a real-time gesture-based human-computer interaction system that allows users to navigate kiosks and interact with digital interfaces without physical touch.

## Technology Stack

- Programming Language: Python
- Computer Vision: OpenCV, MediaPipe
- AI Model for Gesture Recognition: TensorFlow/Keras
- Frontend Interface: Streamlit
- Speech Feedback: pyttsx3
- Cloud & Deployment: Streamlit Sharing / Flask

## Core Features & Functionalities

1. **Real-Time Gesture Recognition System**
   - Hand Tracking & Gesture Recognition using OpenCV and MediaPipe.
   - Predefined gestures: Swipe, Fist Clench, Pointing, OK Sign, Thumbs Up.
   - Customizable gestures using AI models (TensorFlow/Keras).

2. **Touchless Kiosk Interface (Streamlit UI)**
   - Dynamic UI Navigation: Users can navigate menus with hand gestures.
   - Real-time visual feedback: Display detected gestures on the screen.
   - Voice Assistance using pyttsx3 for accessibility.
   - Multilingual support for gesture recognition in different languages.

3. **Accessibility & Inclusivity Features**
   - Custom gesture mapping for differently-abled users.
   - Support for gestures from different cultures and languages.
   - Adjustable gesture sensitivity for varying hand mobility.

4. **Hygiene & Public Safety Enhancement**
   - Eliminates the need for touchscreen interactions.
   - Ideal for airports, museums, hospitals, and malls to reduce germ spread.

5. **Integration with Business Systems**
   - Can be embedded into existing kiosks with minimal hardware changes.
   - Supports cloud-based updates to improve functionality.
   - API-ready for integration with existing software and digital signage.

## Setup and Deployment

1. Clone the repository:
