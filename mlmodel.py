import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

def run_forecast(file):
    df = pd.read_csv(file)

    # assume second column is value
    series = df.iloc[:, 1]

    # ARIMA ML model
    model = ARIMA(series, order=(2,1,2))
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=5)

    # plot
    plt.figure()
    plt.plot(series, label="Actual")
    plt.plot(range(len(series), len(series)+5), forecast, label="Forecast")
    plt.legend()
    plt.savefig("static/plot.png")
    plt.close()

    return forecast.tolist()
