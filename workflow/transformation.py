from sklearn.base import BaseEstimator, TransformerMixin


class selectColumns(BaseEstimator, TransformerMixin):
    """
    Un transformer permetant de sélectionner  des colonnes passées en paramètres (names)
    """
    def __init__(self, names):
        
        self.names = names
    
    def fit(self, X,y=None):
        
        return self
    
    def transform(self, X):
        
        return X[self.names]
    
    def get_feature_names(self):
        return X[self.names].columns.tolist()
