import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Input
from tensorflow.keras.optimizers import Adam

# Dummy dataset (Replace with real gesture data)
X_train = np.random.rand(1000, 21, 2)  # 1000 samples, 21 landmarks, (x, y)
y_train = np.random.randint(0, 5, 1000)  # 5 gesture classes

# Define the model
model = Sequential([
    Input(shape=(21, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(5, activation='softmax')  # 5 gesture classes
])

# Compile the model
model.compile(optimizer=Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, validation_split=0.2)

# Save the model in the correct format
import os
os.makedirs("models", exist_ok=True)  # ✅ Ensures 'models/' exists before saving
model.save("models/gesture_model.keras")

print("✅ Model trained and saved as 'gesture_model.keras'.")
