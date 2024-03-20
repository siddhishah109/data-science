from flask import Flask ,jsonify
from routes import forecast_arima, forecast_sarima

app = Flask(__name__)

# Register routes
app.register_blueprint(forecast_arima)
app.register_blueprint(forecast_sarima)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the time series forecasting API!'})

if __name__ == '__main__':
    app.run(debug=True)
