import json
import numpy as np
import pandas as pd

from house_price_predictor.data_management import data_io
from house_price_predictor.config import config

def test_connection(test_client_fixture):
    
    response = test_client_fixture.get('/ping')
    assert response.status_code == 200


def test_single_prediction(test_client_fixture):
    
    data = data_io.load_dataset(file_name=config.TESTING_DATA_FILE_NAME)
    single_datapoint = data[0:1].to_json()
    
    response = test_client_fixture.post('/v1/predict_house_price', json=single_datapoint)
    pred = json.loads(response.data)['predictions'][0]
    
    assert np.round(pred) == 112476.0