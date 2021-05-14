This repo contains two packages:

  Package 1: house_price_predictor
  
  Package 2: api

The house_price_predictor package contains a end-to-end machine learning pipeline that concludes with a lasso regression model for performing house price prediction.  Testing is done with Tox and PyTest.  A wheel distribution is created using setuptools.

The api package uses Flask to create an endpoint that can used to post house data and receive a response containing the prediction from a trained house_price_predictor model.
