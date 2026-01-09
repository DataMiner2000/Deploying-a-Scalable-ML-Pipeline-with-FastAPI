# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This model was developed by DataMiner2000, with template code provided by Udacity.

Model Date: `01/08/2025`

Model Version: `0.0.1`

Model Type: Logistic Regression with `n=500` iterations

Training Time: Under a minute in most cases.

Upstream Repository: https://github.com/udacity/Deploying-a-Scalable-ML-Pipeline-with-FastAPI

License: Copyright © 2012 - 2020, Udacity, Inc.

Should you have any questions or comments about the model, please open an issue at this Github repository.

## Intended Use

This model is primarily intended for determining whether a person's income is above or below 50K based on demographic data. This particular model has a very fast training time, making it particularly useful for rapid deployment.

## Training Data

This model trains on an 80% slice of the 1994 US Census data, stored in `/data/census.csv`. The data is cleaned and preprocessed in `ml/data.py`.

## Evaluation Data

The other 20% slice of the US Census data is separated to be our evaluation data and is used for verifying the model's accuracy. This data has also been cleaned and preprocessed in `ml/data.py`.

## Metrics
Precision: 0.7113 | Recall: 0.5709 | F1: 0.6334

The model shows high precision, but lower recall. A full analysis of the model metrics can be found in `slice_output.txt`.

## Ethical Considerations

Risks & Harms: It should be noted that because this is trained on older data, the model reflects various historical and systemic biases, leading to lower predicted income levels for individuals belonging to historically marginalized or underrepresented demographic groups.

Data: The data does not contain any PII and is publically available.

Usecases: This model is best suited for educational demonstrations of supervised machine learning workflows, or rapid testing of ML pipelines due to it's fast training time. This model should not be used to predict income in a real-world scenario.

## Caveats and Recommendations

Because the data is drawn entirely from the 1994 US Census, this model would likely be highly inaccurate for predicting income levels today. For real-world use, this model should be retrained on more recent census data.
