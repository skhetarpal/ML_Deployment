This repo contains two packages that together create and deploy a machine learning pipeline.  The ML pipeline is accessed using a Flask API, and it is distributed using using setuptools.  The pipeline implements a house price prediction model that was trained on a dataset taken from kaggle.

Package 1: The house_price_predictor package contains a end-to-end machine learning pipeline that concludes with a lasso regression model for performing house price prediction.  Testing is done with Tox and PyTest.  The package includes logging and version control.

Package 2: The API package uses Flask to create an endpoint that can used to post house data and receive a response containing the prediction from a trained house_price_predictor model.
