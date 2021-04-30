import pytest

from house_price_predictor.data_management import data_io
from house_price_predictor.config import config


@pytest.fixture
def single_datapoint_fixture():
    
    data = data_io.load_dataset(file_name='test.csv')
    single_datapoint = data[0:1].to_json()
    
    return single_datapoint

@pytest.fixture
def data_to_filter_fixture():
    
    data = data_io.load_dataset(file_name='test.csv')
    data = data[0:2]
    data.loc[0, config.LOG_FEATURES[0]] = 0
    data = data.to_json()
    
    return data

@pytest.fixture
def entire_test_set_fixture():
    
    data = data_io.load_dataset(file_name='test.csv')
    data = data.to_json()
    
    return data