# Devanagari Character Recognition

## Overview

This project is an interactive web application that recognizes Devanagari script characters using machine learning. The system allows users to either upload images of Devanagari characters or draw them directly on a canvas. The application then processes these inputs and predicts which character they represent.

Built with a sleek, modern interface featuring an interactive 3D background created with Spline, this tool combines cutting-edge machine learning with an engaging user experience.

## Features

- **Dual Input Methods**: Upload image files or draw characters directly on the canvas
- **Real-time Recognition**: Instantly process and identify Devanagari characters
- **Interactive 3D Background**: Visually engaging environment created with Spline
- **Confidence Scoring**: View the model's confidence level for each prediction
- **Responsive Design**: Works across desktop and mobile devices
- **Touch Support**: Draw characters on touch-enabled devices

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Machine Learning**: TensorFlow/Keras CNN model
- **3D Graphics**: Spline for interactive background
- **Image Processing**: PIL/Pillow for image manipulation

## How It Works

1. **Data Collection**: The model was trained on a comprehensive dataset of Devanagari characters
2. **Preprocessing**: Images are normalized and resized to 64x64 pixels
3. **Model Architecture**: Convolutional Neural Network (CNN) designed specifically for character recognition
4. **Prediction**: The model analyzes the input and returns the most likely character along with a confidence score

## Installation and Setup

# Clone the repository
- git clone-https://github.com/yourusername/devanagari-recognition.git
- cd devanagari-recognition

# Create and activate virtual environment
- python -m venv venv
- source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
- pip install -r requirements.txt

# Run the application
- python app.py

## Demo
![view](https://github.com/user-attachments/assets/29b843dc-23df-4f1c-a9e1-ea81d685e318)


## Usage

1. Access the application at `http://127.0.0.1:5000/`
2. Choose either:
   - **Upload an Image**: Select a file containing a Devanagari character
   - **Draw a Character**: Use the canvas to draw a character with your mouse or finger
3. Click "Recognize Character" to see the prediction
4. View the predicted character and confidence score

## Model Training

The Convolutional Neural Network was trained on a dataset of Devanagari characters with various writing styles and variations. The model architecture includes:

- Multiple convolutional layers for feature extraction
- Max pooling layers for dimensionality reduction
- Dropout layers to prevent overfitting
- Dense layers for classification

## Future Enhancements

- Word-level recognition for complete Devanagari text
- Support for additional Indic scripts
- Mobile application development
- Integration with document digitization tools
- Improved accuracy through model refinement

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgments

- The dataset used was from Kaggle (https://www.kaggle.com/datasets/rishianand/devanagari-character-set)
- Spline for the interactive 3D background capabilities
- The open-source community for various libraries and tools used in this project

---

Made with ❤️ for Devanagari script and machine learning
