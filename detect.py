from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    model = IsolationForest(contamination=0.05, random_state=42)

    df['anomaly'] = model.fit_predict(df[['temperature']])

    print("✅ Anomalies detected!")

    return df