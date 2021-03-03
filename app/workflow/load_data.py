import os
from urllib.request import urlretrieve

import pandas as pd
import numpy as np


def get_data(filename, url, force_download=False):
    """Download and cache the heart data
    Parameters
    ----------
    filename : string (optional)
        location to save the data
    url : string (optional)
        web location of the data
    force_download : bool (optional)
        if True, force re download of data
    Returns
    -------
    data : pandas.DataFrame
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)

        # Read CSV into DataFrame & replace fields contains '?' with NaN
        data = pd.read_csv(url, na_values='?')

        # Set the column names
        data.columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak',
                        'slope', 'ca', 'thal', 'target']
        return data
