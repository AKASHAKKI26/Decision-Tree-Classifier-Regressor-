# Machine Learning Projects – Decision Tree Classifier & Decision Tree Regressor

## Deployment Link

### Decision Tree Regressor Streamlit App

🔗 [https://decisiontreereg.streamlit.app/](https://decisiontreereg.streamlit.app/)

---

# Project 1: Decision Tree Classifier

## **Problem Statement**

The objective of this project is to build a Machine Learning classification model using the Decision Tree Classifier algorithm to predict categorical outcomes based on input features. The project demonstrates the complete machine learning workflow including:

* Data preprocessing
* Feature selection
* Model training
* Model evaluation
* Visualization of decision tree
* Prediction using trained model

This project helps in understanding how classification algorithms work and how decision trees make predictions using feature-based splitting.

---

## Libraries Used

```python
numpy
pandas
matplotlib
seaborn
scikit-learn
pickle
```

---

## Algorithm Used

* Decision Tree Classifier

---

## Workflow

1. Import dataset
2. Data preprocessing
3. Split dataset into training and testing data
4. Train Decision Tree Classifier
5. Evaluate model performance
6. Visualize decision tree
7. Save model using pickle

---

## Metrics Used

* Accuracy Score
* Confusion Matrix
* Classification Report

---

## Model Accuracy

The classifier model was evaluated using testing data and achieved good classification performance.

### Accuracy Details

* Training Accuracy: High
* Testing Accuracy: Good
* Confusion Matrix used for performance evaluation
* Classification report used to analyze:

  * Precision
  * Recall
  * F1-score

The model successfully classifies data based on learned decision rules.

---

## Advantages

* Easy to understand
* Fast training
* Handles categorical and numerical data
* Visualization support

---

## Limitations

* Can overfit on training data
* Sensitive to small data changes
* High variance

---

# Project 2: Decision Tree Regressor

## **Problem Statement**

The objective of this project is to build a Machine Learning regression model using the Decision Tree Regressor algorithm to predict continuous numerical values. The project predicts California housing prices based on housing-related features.

The project demonstrates:

* Regression model building
* Data preprocessing
* Outlier handling
* Hyperparameter tuning
* Model deployment using Streamlit

---

## Dataset Used

* California Housing Dataset

### Features

* MedInc
* HouseAge
* AveRooms
* AveBedrms
* Population
* AveOccup
* Latitude
* Longitude

### Target Variable

* House Price

---

## Libraries Used

```python
numpy
pandas
matplotlib
seaborn
scikit-learn
streamlit
pickle
```

---

## Algorithm Used

* Decision Tree Regressor

---

## Workflow

1. Import California Housing dataset
2. Data preprocessing
3. Outlier detection and handling
4. Train-test split
5. Train Decision Tree Regressor
6. Hyperparameter tuning using GridSearchCV
7. Evaluate regression model
8. Save model using pickle
9. Deploy model using Streamlit

---

## Metrics Used

* MAE (Mean Absolute Error)
* MSE (Mean Squared Error)
* RMSE (Root Mean Squared Error)
* R2 Score

---

## Model Performance

### Regression Metrics

| Metric   | Value |
| -------- | ----- |
| MAE      | 0.445 |
| MSE      | 0.425 |
| RMSE     | 0.652 |
| R2 Score | 0.676 |

### Interpretation

* MAE indicates low average prediction error.
* MSE shows reduced squared prediction loss.
* RMSE indicates improved prediction performance.
* R2 Score of 0.676 shows the model explains approximately 67.6% of the variance in the dataset.
* The regression model performance improved after preprocessing, tuning, and optimization.

---

## Streamlit Deployment

The trained regression model was deployed using Streamlit for real-time house price prediction.

### Features of Web App

* User-friendly interface
* Real-time predictions
* Interactive input fields
* Fast prediction generation

### Deployment Link

🔗 [https://decisiontreereg.streamlit.app/](https://decisiontreereg.streamlit.app/)

---

## Advantages

* Easy implementation
* Handles non-linear relationships
* No feature scaling required
* Supports real-time prediction

---

## Limitations

* Can overfit for deep trees
* Lower generalization compared to ensemble models
* Sensitive to noisy data

---

# Technologies Used

* Python
* Scikit-learn
* Streamlit
* Pandas
* NumPy
* Matplotlib
* Pickle

---

# Conclusion

These projects demonstrate both classification and regression machine learning workflows using Decision Tree algorithms. The projects include model training, evaluation, preprocessing, visualization, model saving, and deployment using Streamlit.

The projects provide practical understanding of:

* Supervised Machine Learning
* Classification
* Regression
* Model evaluation
* Hyperparameter tuning
* Deployment of ML models
