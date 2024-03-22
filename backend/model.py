import statsmodels.api as sm
import pandas as pd
from statsmodels.tsa.stattools import pacf, acf

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
    
def calculate_pacf(data, lags):
    try:
        data_series = pd.Series(data)
        print("Data series:", data_series)
        print("Number of lags:", lags)
     
        pacf_values = pacf(data_series, nlags=lags, method='ols')
        print("PACF values:", pacf_values)
        
        return pacf_values.tolist()
    except Exception as e:
        print("Error:", e)
        return None
 

def calculate_acf(data, lags):
    try:
        data_series = pd.Series(data)
        
        # Calculate ACF
        acf_values = acf(data_series, nlags=lags)
        
        return acf_values.tolist()
    except Exception as e:
        return None
