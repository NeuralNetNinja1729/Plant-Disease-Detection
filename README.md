# Plant Disease Detection

This project is a web application that uses machine learning to detect diseases in plants from uploaded images. The backend is built using **Flask**, a lightweight and powerful Python web framework.

## Project Structure

```
PLANT DISEASE DETECTION/
├── model/
│   ├── trained_plant_disease_model.h5
│   └── plantDisease-2.ipynb
├── templates/
│   ├── index.html
│   └── index2.html
├── test/
│   └── test/
├── app_final.py
├── LICENSE
├── plots.py
├── requirements.txt
└── README.md
```

## Features

- Detects diseases in 38 different classes of plants and plant diseases
- Uses a trained deep learning model (TensorFlow/Keras)
- **Flask-powered backend** for efficient request handling and routing
- Web interface for easy image upload and prediction
- Jupyter notebook for model development and training

## Backend Framework

This project uses **Flask** as the backend framework. Flask is chosen for its simplicity, flexibility, and robustness in creating web applications. It handles:

- Routing of web requests
- Serving of HTML templates
- Processing of image uploads
- Integration with the machine learning model for predictions

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```
   python app_final.py
   ```
2. Open a web browser and navigate to `http://localhost:5000`
3. Upload an image of a plant leaf through the web interface
4. Get the prediction for the plant disease

## Model Development

The `model/plantDisease-2.ipynb` Jupyter notebook contains the code for developing and training the plant disease detection model. This notebook includes:

- Data loading and preprocessing
- Model architecture definition
- Training process
- Evaluation metrics
- Visualization of training results

You can use this notebook to understand the model's development process, make improvements, or retrain the model with new data.

## Model Architecture

The model uses a Convolutional Neural Network (CNN) with the following architecture:

- Multiple convolutional layers with increasing filter sizes (32, 64, 128, 256, 512)
- Max pooling layers
- Dropout layers for regularization
- Flatten layer
- Dense layers with ReLU activation
- Final dense layer with softmax activation for 38 class outputs

## Training Process

- The model was trained on the "New Plant Diseases Dataset(Augmented)" from Kaggle
- Image size: 128x128 pixels
- Optimizer: Adam with learning rate 0.0001
- Loss function: Categorical Cross-Entropy
- Trained for 10 epochs with a batch size of 128

## Files

- `app_final.py`: Main Flask application containing the backend logic
- `plots.py`: (Purpose not specified, likely for generating plots or visualizations)
- `templates/index.html` and `templates/index2.html`: HTML templates for the web interface
- `model/trained_plant_disease_model.h5`: Trained model file
- `model/plantDisease-2.ipynb`: Jupyter notebook for model development and training
- `requirements.txt`: List of Python dependencies

## License

See the `LICENSE` file for details.

## Acknowledgments

- Dataset source: [New Plant Diseases Dataset on Kaggle](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)
- Flask: [Flask Documentation](https://flask.palletsprojects.com/)
