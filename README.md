
# Plant Disease Detection Model

This project provides a web application for detecting plant diseases using a machine learning model. The app allows users to upload images of plant leaves, and it predicts the disease category based on the uploaded image. It displays the predicted category along with the top 5 possible categories and their confidence levels.





## Features

- **Image Upload**: Users can upload an image of a plant leaf.

- **Prediction**: The model predicts the disease category of the plant leaf.

- **Top 5 Predictions**: The app displays the top 5 categories with their confidence levels.

- **Image Preview**: Shows a preview of the uploaded image.

## Technologies

- **Flask**: For creating the web application.

- **TensorFlow/Keras**: For loading and running the machine learning model.

- **HTML/CSS/JavaScript**: For building the front-end interface.

## Setup

### Requirements

- Python 3.7+

- Flask

- TensorFlow

- Keras

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/plant-disease-detection.git
   cd plant-disease-detection
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use \`venv\Scripts\activate\`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   Ensure `requirements.txt` includes:
   ```
   Flask
   tensorflow
   ```

4. **Place Your Model and JSON Files**

   - Save your trained model as `model.h5` in the project directory.

   - Create a JSON file (`categories.json`) with category labels in the project directory.

   Example `categories.json`:
   ```json
   {
       "categories": {
           "0": "Apple Scab",
           "1": "Apple Black Rot",
           "2": "Cedar Apple Rust",
           "3": "Healthy"
       }
   }
   ```

### Running the Application

1. **Start the Flask App**

   ```bash
   python app.py
   ```

2. **Access the Web Application**

   Open your web browser and go to `http://127.0.0.1:5000/.

## Usage

1. **Upload an Image**: Use the "Choose File" button to select an image of a plant leaf from your computer.

2. **Predict**: Click the "Upload and Predict" button to send the image for prediction.

3. **View Results**: The app will display the uploaded image, predicted disease category, and the top 5 predictions with confidence levels.

## Example

- **Image Upload**: Upload an image like `AppleCedarRust1.JPG`.

- **Predicted Category**: "Cedar Apple Rust"

- **Top 5 Predictions**:
  - Category: "Cedar Apple Rust", Probability: 45.6%
  - Category: "Apple Scab", Probability: 25.3%
  - Category: "Apple Black Rot", Probability: 15.2%
  - Category: "Healthy", Probability: 10.8%
  - (Other category if any)

## Troubleshooting

- **Error Loading JSON File**: Ensure `categories.json` is correctly formatted and placed in the project directory.

- **Model Prediction Issues**: Ensure the model is correctly loaded and compatible with the input image dimensions.

## Contributing

Feel free to fork the repository and submit pull requests for improvements. If you encounter any issues, please open an issue on GitHub.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
