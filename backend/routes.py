from flask import Flask, request, jsonify
import pandas as pd
from model import train_arima_model, train_sarima_model

app = Flask(__name__)

@app.route('/forecast/arima', methods=['POST'])
def forecast_arima():
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

@app.route('/forecast/sarima', methods=['POST'])
def forecast_sarima():
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

if __name__ == '__main__':
    app.run(debug=True)
