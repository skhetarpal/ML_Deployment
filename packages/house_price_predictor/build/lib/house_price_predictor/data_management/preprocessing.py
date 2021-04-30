#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 16:19:09 2021

@author: surajkhetarpal
"""

import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin



class Impute_Numerical(BaseEstimator, TransformerMixin):
    
    def __init__(self, numerical_features):
        self.features = numerical_features
        self.mode_dict = {}
        
    def fit(self, X, Y=None):
        
        for feature in self.features:
            mode = X[feature].mode()[0]
            self.mode_dict[feature] = mode
        return self
    
    def transform(self, X):
        X = X.copy()
        for feature in self.features:
            X[feature] = X[feature].fillna(self.mode_dict[feature])
        
        return X


class Impute_Categorical(BaseEstimator, TransformerMixin):
    
    def __init__(self, categorical_features):
        self.features = categorical_features
        
    def fit(self, X, Y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        for feature in self.features:
            X[feature] = X[feature].fillna('Missing')
        
        return X
    
    
class LogTransform(BaseEstimator, TransformerMixin):
    
    def __init__(self, log_features):
        if not isinstance(log_features, list): log_features = [log_features]
        self.features = log_features
        
    def fit(self, X, Y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        for feature in self.features:
            X[feature] = np.log(X[feature])
        
        return X
    

class Transform_Rare(BaseEstimator, TransformerMixin):
    
    def __init__(self, categorical_features, threshold):
        self.features = categorical_features
        self.threshold = threshold
        self.freq_cat_dict = {}
        
    def fit(self, X, Y=None):
        
        for feature in self.features:
            counts = X[feature].value_counts(normalize=True)
            freq_labels = counts.index[counts > self.threshold]
            self.freq_cat_dict[feature] = freq_labels.to_list()
        return self
    
    def transform(self, X):
        X = X.copy()
        for feature in self.features:
            X[feature] = np.where(X[feature].isin(self.freq_cat_dict[feature]), 
                                  X[feature], 'Rare')
        
        return X
    

class Categorical_To_Ordinal(BaseEstimator, TransformerMixin):
    
    def __init__(self, categorical_features):
        self.features = categorical_features
        self.sorted_cat_dict = {}
        
    def fit(self, X, Y=None):
        
        X = X.copy()
        X['target'] = Y
        
        for feature in self.features:
            sorted_categories = X.groupby(feature)['target'].mean().sort_values().index
            self.sorted_cat_dict[feature] = {c:i for i,c in enumerate(sorted_categories)}
        return self
    
    def transform(self, X):
        X = X.copy()
        for feature in self.features:
            X[feature] = X[feature].map(self.sorted_cat_dict[feature])
        
        return X


class TransformTemporal(BaseEstimator, TransformerMixin):
    
    def __init__(self, temporal_feature, reference_feature):
        self.feature = temporal_feature
        self.reference_feature = reference_feature
        
    def fit(self, X, Y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X[self.feature] = X[self.reference_feature] - X[self.feature]
        
        return X
    
    
class Delete_Feature(BaseEstimator, TransformerMixin):
    
    def __init__(self, reference_feature):
        self.feature = reference_feature
        
    def fit(self, X, Y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X = X.drop(self.feature, axis=1)
        
        return X
