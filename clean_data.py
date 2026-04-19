import pandas as pd

def clean_data(path):
    df = pd.read_csv(path)

    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(by='date')

    # Updated for latest pandas
    df = df.ffill()

    print("✅ Data cleaned successfully!")

    return df