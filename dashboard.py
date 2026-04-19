import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("data/processed/final.csv")

st.set_page_config(page_title="Climate Intelligence Dashboard", layout="wide")

st.title("🌍 Climate Intelligence Dashboard")

# Sidebar filters
city = st.sidebar.selectbox("Select City", df["city"].unique())

filtered_df = df[df["city"] == city]

# -------------------------
# 1. Temperature Trend
# -------------------------
st.subheader("🌡 Temperature Trend Over Time")

fig1 = px.line(
    filtered_df,
    x="date",
    y="temperature",
    title="Temperature Trend"
)

st.plotly_chart(fig1, use_container_width=True)

# -------------------------
# 2. Anomaly Detection
# -------------------------
st.subheader("⚠️ Climate Anomalies")

anomaly_df = filtered_df[filtered_df["anomaly"] == -1]

fig2 = px.scatter(
    filtered_df,
    x="date",
    y="temperature",
    color="anomaly",
    title="Anomaly Detection"
)

st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# 3. Statistics
# -------------------------
st.subheader("📊 Key Insights")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Temperature", round(filtered_df["temperature"].mean(), 2))
col2.metric("Max Temperature", round(filtered_df["temperature"].max(), 2))
col3.metric("Anomalies", len(anomaly_df))