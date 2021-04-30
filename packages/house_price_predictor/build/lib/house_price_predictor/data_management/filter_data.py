import pandas as pd
from house_price_predictor.config import config

def _filter(*, data: pd.DataFrame) -> pd.DataFrame:
    
    # filter rows that will cause errors during the log transformations
    data = data.copy()
    bad_rows = ~(data[config.LOG_FEATURES]<=0).any(axis=1)
    data = data[bad_rows]
    
    return data