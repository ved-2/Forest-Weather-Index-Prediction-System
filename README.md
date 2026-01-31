# Forest Weather Index (FWI) Prediction System

A **Machine Learning–powered web application** that predicts the **Forest Weather Index (FWI)** using weather and environmental parameters. The project evaluates multiple regression models and deploys the **best-performing Ridge Regression model** via a Flask web app for real-time predictions.

## Overview

Forest fires are heavily influenced by weather conditions. The **Forest Weather Index (FWI)** is a widely used indicator to estimate fire intensity and risk. This project leverages machine learning to predict FWI based on real-world meteorological inputs and exposes the model through a simple, user-friendly web interface.

---

## Features

* Comparison of multiple regression models
* Robust preprocessing with `StandardScaler`
* Secure prediction using HTTP POST
* Clean Flask architecture with templates

---

## Machine Learning Approach

### Models Evaluated

The following regression models were trained and evaluated:

* Linear Regression
* Ridge Regression
* Lasso Regression
* ElasticNet Regression
* RidgeCV
* LassoCV

### Model Selection

> **Ridge Regression** was selected as the final model based on **higher accuracy, better generalization, and stable performance** on unseen data.

**Why Ridge?**

* Handles multicollinearity effectively
* Provides a better bias–variance trade-off
* Produces more stable coefficients compared to Lasso and ElasticNet

---

## Input Features

The model predicts FWI using the following features:

* Temperature
* Relative Humidity (RH)
* Wind Speed (Ws)
* Rain
* FFMC
* DMC
* DC
* ISI
* BUI

**Target Variable:** Forest Weather Index (FWI)

---

## Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS
* **Machine Learning:** Scikit-learn
* **Data Processing:** NumPy, Pandas
* **Model Serialization:** Pickle

---

## Project Structure

```
project/
│── app.py
│── README.md
│
├── models/
│   ├── ridge.pkl
│   └── scaler.pkl
│
└── templates/
    ├── index.html
    └── home.html
```

---

## Setup & Installation

### 1️ Clone the Repository

```bash
git clone <repository-url>
cd project
```

### 2️ Install Dependencies

```bash
pip install flask numpy pandas scikit-learn
```

### 3️ Run the Application

```bash
python app.py
```

### 4️ Open in Browser

```
http://127.0.0.1:5000/
```

---

## How It Works

1. User opens the **index page**
2. Navigates to the prediction form
3. Enters weather parameters
4. Data is sent via a **POST request**
5. Inputs are scaled using the trained `StandardScaler`
6. Ridge Regression model predicts FWI
7. Result is displayed on the UI



---
