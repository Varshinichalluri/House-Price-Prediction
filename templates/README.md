# House Price Prediction

## Project Overview

This project predicts house prices using Machine Learning and Flask. The application takes housing features as input and predicts the estimated house price using a trained Random Forest Regression model.

## Problem Statement

The objective of this project is to predict house prices based on housing characteristics such as crime rate, number of rooms, tax rate, pollution level, and other important factors.

## Dataset

Boston Housing Dataset

## Features Used

* CRIM
* ZN
* INDUS
* CHAS
* NOX
* RM
* AGE
* DIS
* RAD
* TAX
* PTRATIO
* B
* LSTAT

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Flask
* HTML
* CSS

## Machine Learning Model

Random Forest Regressor

## Model Performance

* R² Score: 0.89
* Mean Squared Error (MSE): 7.90

## Project Structure

House Price Prediction/
├── app.py
├── Boston-housing-dataset.csv
├── Boston-housing-dataset.ipynb
├── regmodel.pkl
├── requirements.txt
├── README.md
├── static/
│   └── style.css
└── templates/
└── home.html

## Output

The application accepts user inputs and predicts the house price using a trained Random Forest model.

## Future Enhancements

* Better UI Design
* Cloud Deployment
* Model Comparison Dashboard
* Real Estate Analytics Features
