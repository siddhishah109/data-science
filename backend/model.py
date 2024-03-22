import statsmodels.api as sm
import pandas as pd

def train_arima_model(data, order=(1, 1, 1)):
    arima_model = sm.tsa.ARIMA(data, order=order).fit()
    return arima_model

def train_sarima_model(data, order=(1, 1, 1), seasonal_order=(0, 1, 1, 12)):
    sarima_model = sm.tsa.SARIMAX(data, order=order, seasonal_order=seasonal_order).fit()
    return sarima_model


def calculate_autocorrelation(data, lags):
    try:
        data_series = pd.Series(data)
        
        autocorr = [data_series.autocorr(lag) for lag in range(lags)]
        
        return autocorr
    except Exception as e:
        return None