from statsmodels.tsa.statespace.sarimax import SARIMAX
import pandas as pd

def forecast_temperature(df):
    # Use only one city for forecasting (example: Pune)
    city_df = df[df['city'] == 'Pune'].copy()

    city_df = city_df.sort_values(by='date')

    model = SARIMAX(
        city_df['temperature'],
        order=(1, 1, 1),
        seasonal_order=(1, 1, 1, 12)
    )

    result = model.fit(disp=False)

    forecast = result.forecast(steps=30)

    print("📈 Forecast for next 30 days:")
    print(forecast)

    return forecast