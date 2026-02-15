import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def forecast_timeseries(file):
    df = pd.read_csv(file)

    data = df.iloc[:, 1]  # second column values

    model = ARIMA(data, order=(2,1,2))
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=5)
    return forecast.tolist()
