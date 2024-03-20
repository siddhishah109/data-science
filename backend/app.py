from flask import Flask ,jsonify
from routes import forecast_arima, forecast_sarima

app = Flask(__name__)

# Register routes
app.register_blueprint(forecast_arima)
app.register_blueprint(forecast_sarima)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the time series forecasting API!'})

def handler(request):
    # Convert incoming Vercel request to Flask request
    environ = request.__dict__["__serverless_req__"]["__origin__"]
    with app.request_context(environ):
        # Dispatch the request to Flask app
        response = app.full_dispatch_request()
        # Convert Flask response to Vercel response
        return response.response

if __name__ == '__main__':
    app.run(debug=True)
