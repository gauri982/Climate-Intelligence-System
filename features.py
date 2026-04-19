def add_features(df):
    # Rolling average (7-day)
    df['rolling_temp'] = df['temperature'].rolling(7).mean()

    # Month extraction
    df['month'] = df['date'].dt.month

    print("✅ Features added!")

    return df