from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
import os
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('devanagari_character_model.h5')

# Map class indices to character names
class_mapping = {
    0: "character_01_ka",
    1: "character_02_kha",
    2: "character_03_ga",
    3: "character_04_gha",
    4: "character_05_kna",
    # Add all your character mappings here
    # ...
}

# Get readable character names
def get_readable_name(folder_name):
    # Extract the character name from folder name (e.g., "character_01_ka" -> "का (ka)")
    parts = folder_name.split('_')
    if len(parts) >= 3:
        return f"{parts[2]} ({parts[1]})"
    return folder_name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    # Process the image - convert to RGB to match model's expected input
    img = Image.open(file).convert('RGB')  # Convert to RGB
    img = img.resize((64, 64))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    
    # Make prediction
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    confidence = float(predictions[0][predicted_class] * 100)
    
    # Get character name
    character_folder = class_mapping.get(predicted_class, f"Unknown ({predicted_class})")
    character_name = get_readable_name(character_folder)
    
    return jsonify({
        'character': character_name,
        'confidence': round(confidence, 2)
    })

@app.route('/predict-drawing', methods=['POST'])
def predict_drawing():
    data = request.json
    if not data or 'image' not in data:
        return jsonify({'error': 'No image data'})
    
    # Process the base64 image
    image_data = data['image'].split(',')[1]
    img = Image.open(BytesIO(base64.b64decode(image_data)))
    
    # Convert to RGB and resize
    img = img.convert('RGB')
    img = img.resize((64, 64))
    
    # Prepare for model
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    
    # Make prediction
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    confidence = float(predictions[0][predicted_class] * 100)
    
    # Get character name
    character_folder = class_mapping.get(predicted_class, f"Unknown ({predicted_class})")
    character_name = get_readable_name(character_folder)
    
    return jsonify({
        'character': character_name,
        'confidence': round(confidence, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
