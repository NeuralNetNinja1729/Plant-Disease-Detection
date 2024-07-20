from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import os
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)

CLASS_NAMES = np.array(
    [
    "Apple - Apple scab", 
    "Apple - Black rot", 
    "Apple - Cedar apple rust", 
    "Apple - healthy", 
    "Blueberry - healthy", 
    "Cherry (including sour) - Powdery mildew", 
    "Cherry (including sour) - healthy", 
    "Corn (maize) - Cercospora leaf spot Gray leaf spot", 
    "Corn (maize) - Common rust", 
    "Corn (maize) - Northern Leaf Blight", 
    "Corn (maize) - healthy", 
    "Grape - Black rot", 
    "Grape - Esca (Black Measles)", 
    "Grape - Leaf blight (Isariopsis Leaf Spot)", 
    "Grape - healthy", 
    "Orange - Haunglongbing (Citrus greening)", 
    "Peach - Bacterial spot", 
    "Peach - healthy", 
    "Pepper, bell - Bacterial spot", 
    "Pepper, bell - healthy", 
    "Potato - Early blight", 
    "Potato - Late blight", 
    "Potato - healthy", 
    "Raspberry - healthy", 
    "Soybean - healthy", 
    "Squash - Powdery mildew", 
    "Strawberry - Leaf scorch", 
    "Strawberry - healthy", 
    "Tomato - Bacterial spot", 
    "Tomato - Early blight", 
    "Tomato - Late blight", 
    "Tomato - Leaf Mold", 
    "Tomato - Septoria leaf spot", 
    "Tomato - Spider mites Two-spotted spider mite", 
    "Tomato - Target Spot", 
    "Tomato - Tomato Yellow Leaf Curl Virus", 
    "Tomato - Tomato mosaic virus", 
    "Tomato - healthy"
    ]
)
    
model = load_model('model2/trained_plant_disease_model_2.h5')
def predict_one_image(img_path, model):
    img = tf.keras.utils.load_img(img_path, target_size=(128, 128))
    image = np.array([tf.keras.preprocessing.image.img_to_array(img)])
    predictions = model.predict(image)
    return CLASS_NAMES[np.argmax(predictions)], np.max(np.round(predictions, 2))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def upload():
    print(request.files)
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        if not os.path.exists('uploads'):
            os.makedirs('uploads')
        file_path = f'uploads/{file.filename}'
        file.save(file_path)
        pred_class, confidence = predict_one_image(file_path, model)
        return jsonify(prediction=f'{pred_class} | Confidence: {confidence}')
    
if __name__ == '__main__':
    app.run(debug=True)
    