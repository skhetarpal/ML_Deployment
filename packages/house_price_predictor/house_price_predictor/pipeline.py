#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 08:14:12 2021

@author: surajkhetarpal
"""

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import Lasso

from house_price_predictor.config import config
import house_price_predictor.data_management.preprocessing as pre

housing_price_pipeline = Pipeline(
    [
     ('impute_numerical', pre.Impute_Numerical(numerical_features=config.NUMERICAL_FEATURES)),
     ('impute_categorical', pre.Impute_Categorical(categorical_features=config.CATEGORICAL_FEATURES)),
     ('log_transform', pre.LogTransform(log_features=config.LOG_FEATURES)),
     ('transform_rare', pre.Transform_Rare(categorical_features=config.CATEGORICAL_FEATURES, threshold=0.01)),
     ('categorical_to_ordinal', pre.Categorical_To_Ordinal(categorical_features=config.CATEGORICAL_FEATURES)),
     ('transform_temporal', pre.TransformTemporal(temporal_feature=config.TEMPORAL_FEATURE, reference_feature=config.REFERENCE_FEATURE)),
     ('delete_feature', pre.Delete_Feature(reference_feature=config.REFERENCE_FEATURE)),
     ('scale', MinMaxScaler()),
     ('lin_reg_with_L1', Lasso(alpha=0.005, random_state=0))
    ]
    )