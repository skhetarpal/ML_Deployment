#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 11:49:28 2021

@author: surajkhetarpal
"""
import os

PACKAGE_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
TRAINED_MODEL_DIR = os.path.join(PACKAGE_ROOT, 'trained_models/')
DATASET_DIR = os.path.join(PACKAGE_ROOT, 'datasets/')


TRAINING_DATA_FILE_NAME = "train.csv"
TESTING_DATA_FILE_NAME = "test.csv"
PIPELINE_FILE_NAME_ROOT = "house_price_prediction_pipeline"
 
IMPORTANT_FEATURES = ['MSSubClass', 'MSZoning', 'Neighborhood',
            'OverallQual', 'OverallCond', 'YearRemodAdd',
            'RoofStyle', 'MasVnrType', 'BsmtQual', 'BsmtExposure',
            'HeatingQC', 'CentralAir', '1stFlrSF', 'GrLivArea',
            'BsmtFullBath', 'KitchenQual', 'Fireplaces', 'FireplaceQu',
            'GarageType', 'GarageFinish', 'GarageCars', 'PavedDrive',
            'LotFrontage', 'YrSold']

# numerical variables with NA in train set
NUMERICAL_FEATURES = ['MSSubClass', 'OverallQual', 'OverallCond', 'YearRemodAdd',
                  '1stFlrSF', 'GrLivArea', 'BsmtFullBath', 'Fireplaces', 
                  'GarageCars', 'LotFrontage']

# categorical variables with NA in train set
CATEGORICAL_FEATURES = ['MSZoning', 'Neighborhood', 'RoofStyle', 'MasVnrType', 
                    'BsmtQual', 'BsmtExposure','HeatingQC', 'CentralAir', 
                    'KitchenQual', 'FireplaceQu', 'GarageType', 
                    'GarageFinish', 'PavedDrive']

# variables to log transform
LOG_FEATURES = ['LotFrontage', '1stFlrSF', 'GrLivArea']


TEMPORAL_FEATURE = 'YearRemodAdd'

REFERENCE_FEATURE = 'YrSold'

TARGET = 'SalePrice'


LOGGER_NAME = 'house_price_predictor'
