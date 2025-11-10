import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
import cv2

# Load model
model = keras.models.load_model('Model.h5')

print("Model loaded successfully!")
print(f"Model input shape: {model.input_shape}")
print(f"Model output shape: {model.output_shape}")

# Test with a dummy image
dummy_img = np.random.randint(0, 255, (1, 224, 224, 3)).astype('float32')
prediction = model.predict(dummy_img, verbose=0)

print(f"\nTest prediction on random image:")
print(f"Raw output: {prediction[0]}")
print(f"Predicted class: {np.argmax(prediction[0])}")
print(f"Confidence: {prediction[0][np.argmax(prediction[0])] * 100:.2f}%")

# Model summary
print("\n" + "="*50)
print("Model Summary:")
print("="*50)
model.summary()
