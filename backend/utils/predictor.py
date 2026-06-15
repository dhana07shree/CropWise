# backend/utils/predictor.py
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

CLASS_NAMES = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 
    'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
    'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight',
    'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy',
    'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy',
    'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight',
    'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

# Locate where your model file lives relative to this script
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../models/best_plant_model.keras')

def predict_disease(image_path: str):
    """
    Loads the trained local Keras model, processes an incoming leaf image,
    and returns the clean plant type, disease condition, and confidence score.
    """
    if not os.path.exists(MODEL_PATH):
        return {"error": f"Model file not found at {MODEL_PATH}"}

    # 1. Load the model brain
    model = tf.keras.models.load_model(MODEL_PATH)
    
    # 2. Preprocess the image to match MobileNetV2 inputs exactly (224x224)
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Make it a batch of 1
    img_array = img_array / 255.0                  # Normalize pixel scaling
    
    # 3. Predict
    predictions = model.predict(img_array)
    highest_idx = np.argmax(predictions[0])
    confidence = float(predictions[0][highest_idx])
    
    raw_class = CLASS_NAMES[highest_idx]
    
    # 4. Clean up the folder text strings into nice user layout tokens
    if "___" in raw_class:
        plant, condition = raw_class.split("___", 1)
    else:
        plant, condition = " ", raw_class
        
    return {
        "plant": plant.replace("_", " ").title(),
        "condition": condition.replace("_", " ").replace("  ", " ").strip(),
        "confidence": round(confidence * 100, 2)
    }

