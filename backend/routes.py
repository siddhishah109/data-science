# backend/routes.py

from flask import Blueprint, jsonify, request
import pandas as pd
from model import train_arima_model, train_sarima_model

forecast_arima = Blueprint('forecast_arima', __name__)

@forecast_arima.route('/forecast/arima', methods=['POST'])
def forecast_arima_route():
    data = request.json.get('data')
    if data is None:
        return jsonify({'error': 'No data provided'}), 400

    # Convert data to pandas Series or DataFrame if necessary
    data = pd.Series(data)

    # Extract parameters from request
    params = request.json.get('params', {})
    order = params.get('order', (1, 1, 1))
    steps = params.get('steps', 5)

    # Train ARIMA model with custom parameters
    arima_model = train_arima_model(data, order=order)

    # Generate forecast with custom number of steps
    forecast_result = arima_model.forecast(steps=steps)

    return jsonify({'forecast': forecast_result.tolist()})


forecast_sarima = Blueprint('forecast_sarima', __name__)

@forecast_sarima.route('/forecast/sarima', methods=['POST'])
def forecast_sarima_route():
    data = request.json.get('data')
    if data is None:
        return jsonify({'error': 'No data provided'}), 400

    # Convert data to pandas Series or DataFrame if necessary
    data = pd.Series(data)

    # Extract parameters from request
    params = request.json.get('params', {})
    order = params.get('order', (1, 1, 1))
    seasonal_order = params.get('seasonal_order', (0, 1, 1, 12))
    steps = params.get('steps', 5)

    # Train SARIMA model with custom parameters
    sarima_model = train_sarima_model(data, order=order, seasonal_order=seasonal_order)

    # Generate forecast with custom number of steps
    forecast_result = sarima_model.forecast(steps=steps)

    return jsonify({'forecast': forecast_result.tolist()})
