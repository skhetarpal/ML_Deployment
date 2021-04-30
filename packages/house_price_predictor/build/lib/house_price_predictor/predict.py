import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import logging

from house_price_predictor.config import config
from house_price_predictor.data_management import data_io
from house_price_predictor.data_management import filter_data

from house_price_predictor import __version__


_logger = logging.getLogger(name=config.LOGGER_NAME)


def pipeline_predict(data: pd.DataFrame) -> np.ndarray:
    
    housing_price_pipeline = data_io.load_pipeline()
    return np.exp(housing_price_pipeline.predict(data))


def predict_json(*, input_json: str) -> dict:
    
    data = pd.read_json(input_json)[config.IMPORTANT_FEATURES]
    data = filter_data._filter(data=data)
    preds = pipeline_predict(data=data)
    
    _logger.info(
        f'Predicting using pipeline version: {__version__}. '
        f'Input data: {data} '
        f'Predictions: {preds}'
        )
    
    response = {'predictions': preds}
    return response


def test_model():
    
    data = data_io.load_train_data()
    _, X_test, _, Y_test = train_test_split(data[config.IMPORTANT_FEATURES], 
                                              data[config.TARGET], 
                                              test_size=0.1, random_state=0)
    
    preds = pipeline_predict(X_test)
    
    print('test data mean_squared_error is:', mean_squared_error(Y_test, preds))
    print('test data r2_score is:', r2_score(Y_test, preds))
    
    