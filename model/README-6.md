# Plant Disease Detection

This project is a web application that uses machine learning to detect diseases in plants from uploaded images.

## Project Structure

```
PLANT DISEASE DETECTION/
├── model/
│   └── trained_plant_disease_model.h5
├── templates/
│   ├── index.html
│   └── index2.html
├── test/
│   └── test/
├── app_final.py
├── LICENSE
├── plots.py
└── README.md
```

## Features

- Detects diseases in 38 different classes of plants and plant diseases
- Uses a trained deep learning model (TensorFlow/Keras)
- Web interface for easy image upload and prediction

## Installation

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install flask tensorflow numpy matplotlib
   ```

## Usage

1. Run the Flask application:
   ```
   python app_final.py
   ```
2. Open a web browser and navigate to `http://localhost:5000`
3. Upload an image of a plant leaf through the web interface
4. Get the prediction for the plant disease

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

- `app_final.py`: Main Flask application
- `plots.py`: (Purpose not specified, likely for generating plots or visualizations)
- `templates/index.html` and `templates/index2.html`: HTML templates for the web interface
- `trained_plant_disease_model.h5`: Trained model file

## License

See the `LICENSE` file for details.

## Contributing

Instructions for how to contribute to this project. (Add specific guidelines if available)

## Contact

Your contact information or how to reach out for questions and support.

## Acknowledgments

- Dataset source: [New Plant Diseases Dataset on Kaggle](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)
