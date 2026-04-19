import matplotlib.pyplot as plt
import seaborn as sns

def plot_trends(df):
    plt.figure(figsize=(12,5))

    sns.lineplot(data=df, x="date", y="temperature", label="Temperature")

    plt.title("🌡 Climate Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature")

    plt.show()


def plot_anomalies(df):
    plt.figure(figsize=(12,5))

    normal = df[df['anomaly'] == 1]
    anomaly = df[df['anomaly'] == -1]

    plt.scatter(normal['date'], normal['temperature'], label="Normal", s=10)
    plt.scatter(anomaly['date'], anomaly['temperature'], label="Anomaly", color="red")

    plt.legend()
    plt.title("⚠️ Climate Anomalies")
    plt.show()