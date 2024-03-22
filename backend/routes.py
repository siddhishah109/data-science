# backend/routes.py

from flask import Blueprint, jsonify, request
import pandas as pd
from model import train_arima_model, train_sarima_model , calculate_autocorrelation

forecast_arima = Blueprint('forecast_arima', __name__)

@forecast_arima.route('/forecast/arima', methods=['POST'])
def forecast_arima_route():
    data = request.json.get('data')
    if data is None:
        return jsonify({'error': 'No data provided'}), 400

    data = pd.Series(data)

    params = request.json.get('params', {})
    order = params.get('order', (1, 1, 1))
    steps = params.get('steps', 5)

  
    arima_model = train_arima_model(data, order=order)

 
    forecast_result = arima_model.forecast(steps=steps)

    return jsonify({'forecast': forecast_result.tolist()})


forecast_sarima = Blueprint('forecast_sarima', __name__)

@forecast_sarima.route('/forecast/sarima', methods=['POST'])
def forecast_sarima_route():
    data = request.json.get('data')
    if data is None:
        return jsonify({'error': 'No data provided'}), 400

    data = pd.Series(data)

    params = request.json.get('params', {})
    order = params.get('order', (1, 1, 1))
    seasonal_order = params.get('seasonal_order', (0, 1, 1, 12))
    steps = params.get('steps', 5)

    sarima_model = train_sarima_model(data, order=order, seasonal_order=seasonal_order)


    forecast_result = sarima_model.forecast(steps=steps)

    return jsonify({'forecast': forecast_result.tolist()})



autocorrelation = Blueprint('autocorrelation', __name__)

@autocorrelation.route('/autocorrelation', methods=['POST'])

def autocorrelation_route():
    data = request.json.get('data')
    if data is None:
        return jsonify({'error': 'No data provided'}), 400

    data_series = pd.Series(data)

    lags = request.json.get('lags', 10)

    autocorr = calculate_autocorrelation(data_series, lags)

    if autocorr is not None:
        return jsonify({'autocorrelation': autocorr})
    else:
        return jsonify({'error': 'Failed to calculate autocorrelation.'}), 500