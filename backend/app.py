from flask import Flask
from routes import forecast_arima, forecast_sarima

app = Flask(__name__)

# Register routes
app.register_blueprint(forecast_arima)
app.register_blueprint(forecast_sarima)

if __name__ == '__main__':
    app.run(debug=True)
