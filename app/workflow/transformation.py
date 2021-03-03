from sklearn.base import BaseEstimator, TransformerMixin


class selectColumns(BaseEstimator, TransformerMixin):
    """
    A transformer allowing to select columns passed in parameters (names)
    """
    def __init__(self, names):
        
        self.names = names
    
    def fit(self, X,y=None):
        
        return self
    
    def transform(self, X):
        
        return X[self.names]
    
    def get_feature_names(self):
        return X[self.names].columns.tolist()
