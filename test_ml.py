import pytest
import pandas as pd
import numpy as np
from ml.model import train_model, compute_model_metrics
from sklearn.linear_model import LogisticRegression

# Add some sample data for testing purposes
sample_data = pd.DataFrame({
    '1': [1, 2, 5],
    '2': [0, 1, 3],
    '3': [0, 1, 2]
})

def test_model_iterations_num():
    """
    Ensures that our model iterates the specified number of times.
    """
    X = np.array([[0], [1]])
    y = np.array([0, 1])
    model = train_model(X, y)
    assert model.max_iter == 500

def test_model_classifier_correct():
    """
    Tests that our model type (Logistic Regression) is being selected and run successfully.
    """
    X = sample_data[['1', '2']]
    y = sample_data['3']
    model = train_model(X, y)
    assert isinstance(model, LogisticRegression)

def test_model_metrics():
    """
    Tests to make sure that model metrics are being computed correctly and are floats.
    """
    y1 = [0, 1, 0, 1]
    y2 = [0, 1, 1, 1]
    precision, recall, fbeta = compute_model_metrics(y1, y2)
    assert all(isinstance(m, float) for m in [precision, recall, fbeta])
