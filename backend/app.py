from flask import Flask ,jsonify
from routes import forecast_arima, forecast_sarima , autocorrelation ,pacf ,acf
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# Register routes
app.register_blueprint(forecast_arima)
app.register_blueprint(forecast_sarima)
app.register_blueprint(autocorrelation)
app.register_blueprint(pacf)
app.register_blueprint(acf)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the time series forecasting API!'})

if __name__ == '__main__':
    app.run(debug=True)
