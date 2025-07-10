# Karachi Smart City Analytics Platform
# ✅ Manual data simulation button
# ✅ Tabs for Traffic / AQI / Safety
# ✅ Anomaly detection + CSV export

import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime, timedelta
from sklearn.ensemble import IsolationForest

# 1️⃣ DATABASE SETUP
def init_db():
    conn = sqlite3.connect('karachi_city.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS traffic (
                    timestamp TEXT, location TEXT, traffic_volume INTEGER, avg_speed REAL)''')
    conn.commit()
    return conn

# 2️⃣ SIMULATION FUNCTION (Traffic Example)
def simulate_traffic_data():
    areas = ['Saddar', 'Clifton', 'Gulshan', 'Defence']
    now = datetime.now()
    data = []
    for area in areas:
        traffic_volume = np.random.randint(20, 100)
        avg_speed = max(5, 40 - traffic_volume * 0.3)
        data.append((now.isoformat(), area, traffic_volume, avg_speed))
    return data

# 3️⃣ DATA SAVING
def save_traffic_to_db(conn, data):
    c = conn.cursor()
    c.executemany("INSERT INTO traffic VALUES (?, ?, ?, ?)", data)
    conn.commit()

# 4️⃣ LOAD DATA
def load_traffic(conn, hours=1):
    c = conn.cursor()
    cutoff = datetime.now() - timedelta(hours=hours)
    df = pd.read_sql_query("SELECT * FROM traffic WHERE timestamp >= ?", conn, params=[cutoff.isoformat()])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

# 5️⃣ ANOMALY DETECTION
def detect_anomalies(df):
    if df.empty:
        return pd.DataFrame()
    model = IsolationForest(contamination=0.1)
    df['anomaly'] = model.fit_predict(df[['traffic_volume', 'avg_speed']])
    return df[df['anomaly'] == -1]

# 6️⃣ STREAMLIT UI
def main():
    st.set_page_config("Karachi Smart City", layout="wide")
    st.title("🏙️ Karachi Smart City Dashboard")

    conn = init_db()

    # Manual Simulation Button
    if st.sidebar.button("🔁 Simulate New Traffic Data"):
        new_data = simulate_traffic_data()
        save_traffic_to_db(conn, new_data)
        st.success("New traffic data simulated and saved!")

    # Tabs
    tab1, tab2, tab3 = st.tabs(["📊 Traffic", "🌫️ Air Quality (Coming Soon)", "⚠️ Safety (Coming Soon)"])

    with tab1:
        st.sidebar.header("Control Panel")
        hours = st.sidebar.slider("Time range (hours)", 1, 24, 6)

        df = load_traffic(conn, hours)

        if df.empty:
            st.warning("No data available.")
            return

        st.metric("Average Traffic Volume", f"{df['traffic_volume'].mean():.1f}%")
        st.metric("Average Speed", f"{df['avg_speed'].mean():.1f} km/h")

        st.line_chart(df.pivot(index='timestamp', columns='location', values='traffic_volume'))

        st.subheader("🚨 Traffic Anomalies")
        anomalies = detect_anomalies(df)
        if not anomalies.empty:
            st.dataframe(anomalies)

            # Download as CSV
            csv = anomalies.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download Anomaly Report as CSV", data=csv, file_name="anomalies.csv", mime="text/csv")
        else:
            st.success("No anomalies detected!")

if __name__ == '__main__':
    main()
