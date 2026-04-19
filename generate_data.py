import pandas as pd
import numpy as np

def generate_data():
    dates = pd.date_range(start="2015-01-01", periods=2000)

    cities = ["Pune", "Mumbai", "Delhi"]
    data = []

    for city in cities:
        base_temp = {"Pune": 25, "Mumbai": 28, "Delhi": 30}[city]

        for i, date in enumerate(dates):
            temp = base_temp + np.sin(i/365)*10 + np.random.normal(0,2)
            rain = np.random.uniform(0,100)

            data.append([date, city, temp, rain])

    df = pd.DataFrame(data, columns=["date","city","temperature","rainfall"])
    df.to_csv("data/raw/climate_data.csv", index=False)

    print("✅ Climate dataset generated!")

if __name__ == "__main__":
    generate_data()