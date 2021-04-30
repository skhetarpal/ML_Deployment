import pandas as pd
from house_price_predictor.data_management import filter_data


def test_filter_small(data_to_filter_fixture):
    
    data = pd.read_json(data_to_filter_fixture)
    
    assert len(data) == 2
    
    data = filter_data._filter(data=data)
    
    assert len(data) == 1


def test_filter_large(entire_test_set_fixture):
    
    data = pd.read_json(entire_test_set_fixture)
    data = filter_data._filter(data=data)
    
    assert len(data) == 1459