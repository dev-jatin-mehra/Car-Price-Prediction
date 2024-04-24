# Car Price Predictor

## Overview

This is a car price predictor application built using machine learning techniques. It predicts the price of a car based on various features such as brand, model, year, kms_driven and fuel_type.

## Files

- **app.py**: This file contains the Flask web application that serves as the interface for users to input car details and get price predictions.
- **car_price_predictor.ipynb**: This Jupyter Notebook contains the code for data preprocessing, model training, and evaluation. It also includes visualizations and explanations of the model's performance.
- **templates/**: This directory contains HTML templates used by the Flask application for rendering web pages.
- **static/css/**: This directory contains CSS files for styling the web application.
- **Model.pkl**: This is the trained machine learning model serialized using pickle. It is used by the Flask application to make price predictions.

## Installation

1. Clone this repository to your local machine:

    ```cmd
    git clone https://github.com/yourusername/car-price-predictor.git
    ```

2. Navigate to the project directory:

    ```cmd
    cd Car-Price-Prediction
    ```

3. Install the required dependencies:

    ```cmd
    pip install -r requirements.txt
    ```

## Usage

1. Run the `app.py` script to start the Flask web application:

    ```cmd
    python app.py
    ```

2. Open your web browser and go to `http://localhost:abcd` to access the application.
3. Input the car details for which you want to predict the price and submit the form to get the prediction.

## Model Training

If you want to train the model on your own dataset or retrain the existing model, follow these steps:

1. Open and run the `car_price_predictor.ipynb` Jupyter Notebook to preprocess data, train the model, and evaluate its performance.
2. Modify the `app.py` script to load the trained model (Model.pkl) and use it for making predictions in the web application.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create a GitHub issue or submit a pull request.

## Acknowledgements

campusX
