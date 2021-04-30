import numpy as np
from sklearn.model_selection import train_test_split


from house_price_predictor.config import config
from house_price_predictor import pipeline
from house_price_predictor.data_management import data_io



def train() -> None:
    data = data_io.load_train_data()
    X_train, _, Y_train, _ = train_test_split(data[config.IMPORTANT_FEATURES], 
                                              data[config.TARGET], 
                                              test_size=0.1, random_state=0)
    
    Y_train = np.log(Y_train)
    
    housing_price_pipeline = pipeline.housing_price_pipeline
    housing_price_pipeline.fit(X_train[config.IMPORTANT_FEATURES], Y_train)
    
    data_io.save_pipeline(_pipeline=housing_price_pipeline)


if __name__ == '__main__':
    train()