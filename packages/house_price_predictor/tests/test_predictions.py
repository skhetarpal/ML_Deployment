import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

from house_price_predictor.config import config
from house_price_predictor import predict


def test_single_datapoint(single_datapoint_fixture):
    
    pred = predict.predict_json(input_json=single_datapoint_fixture)
    
    assert np.round(pred['predictions'][0]) == 112476.0

