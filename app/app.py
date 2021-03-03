from flask import Flask, request
import joblib
import pandas as pd
from pandas.io.json import json_normalize
import json
import logging
import os

logging.basicConfig(level=logging.INFO)


def create_app():
    app = Flask(__name__)
    livrable = joblib.load('../data/deliverable')

    @app.route('/predict', methods=['POST'])
    def predict():
        logging.info('predict request')
        data = pd.DataFrame.from_dict(json_normalize(request.get_json(force=True)), orient='columns')
        logging.info(data.shape[0])

        return data.\
            join(pd.DataFrame(livrable['pipeline']
                              .predict_proba(data)))\
            .to_json(orient='records')

    @app.route('/info', methods=['GET'])
    def how_to_consume_model():
        logging.info('Info request ')
        return json.dumps(livrable['schema'])

    return app
