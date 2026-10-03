import argparse
import pickle
from pathlib import Path
import pandas as pd


def predict_csv(data, output_file=None):
    model_file = Path(__file__).resolve().parent / 'model.pkl'
    with model_file.open('rb') as file:
        model = pickle.load(file)

    # features = list(model.feature_names_in_)
    # missing = set(features) - set(data.columns)
    # if missing:
    #     raise ValueError(f'Missing model features: {sorted(missing)}')

    data['prediction'] = model.predict(data)
    # data['sticky_probability'] = model.predict_proba(data[features])[:, list(model.classes_).index(1)]

    # output_file = Path(output_file) if output_file else input_file.with_name(input_file.stem + '_predictions.csv')
    # data.to_csv(output_file, index=False)
    return output_file
