
```markdown
# 🏙️ Karachi Smart City Analytics Platform

A real-time AI-powered urban analytics dashboard for Karachi 🇵🇰  Built with Streamlit, SQLite, and machine learning —
this platform simulates and visualizes traffic data,detects anomalies, and sets the foundation for AQI and safety
monitoring.



## 🧠 Features

### ✅ Functional
- 🔁 Manual Simulation Button: Simulate and inject fresh traffic data
- 📊 Traffic Monitoring: View volume and speed trends by area
- 🧠 Anomaly Detection: Uses Isolation Forest to flag unusual traffic patterns
- 📥 Export to CSV: Download anomaly logs for external use
- 📌 Time Range Filter: Choose how many hours of data to display

### 🚧 In Progress
- 🌫️ Air Quality Monitoring (Coming soon)
- ⚠️ Safety Incident Tracking (Coming soon)

---

## 🏗️ Tech Stack

| Category      | Stack                                      |
|---------------|---------------------------------------------|
| UI            | Streamlit                                  |
| Data Handling | Pandas, NumPy                              |
| Database      | SQLite (lightweight local DB)              |
| ML Model      | Scikit-learn (Isolation Forest)            |
| Visualization | Streamlit Charts, Metrics, Tabs            |
| Dev           | Python 3.9+                                |

---

---

## 🔧 Setup Instructions

### ✅ 1. Clone the Repo

```bash
git clone https://github.com/your-username/karachi-smart-city.git
cd karachi-smart-city
````

### ✅ Install Requirements

```bash
pip install -r requirements.txt
```

### ✅ Run the Application

```bash
streamlit run karachi_smart_city.py
```

Then open: `http://localhost:8501` in your browser.

---

## 💻 How It Works

* 🧪 On each manual simulation, data is generated for 4 key Karachi areas (Saddar, Clifton, Gulshan, Defence)
* 📦 Data is stored in `karachi_city.db`
* 📊 Visuals update dynamically based on selected time range
* 🚨 Anomalies are detected using Isolation Forest on traffic volume + speed
* 📥 Users can export detected anomalies as a `.csv` file

---

## 🧪 Sample Visuals

<img width="1916" height="808" alt="image" src="https://github.com/user-attachments/assets/0bf7c5e8-b132-4dd7-81e1-062ad4f3b063" />
<img width="1515" height="428" alt="image" src="https://github.com/user-attachments/assets/afda2072-71bd-489b-a4e7-40691fa53523" />


---



## 🔮 Future Roadmap

* 🌫️ Real-time AQI data with OpenAQ API or simulations
* 🛡️ Karachi-specific safety alerts (snatching, fire, power outage)
* 📲 Push notifications (Twilio/Telegram)
* 🔐 Role-based access (admin vs. public)
* ☁️ REST API backend (FastAPI) for mobile clients
* 📈 Historical trends with interactive filters

---

## 👤 Author

**Hafiza Aliza Mustafa**
🎓 BSc Artificial Intelligence @ SZABIST
📬 Email: [aleezamustafa11@gmail.com](mailto:aleezamustafa11@gmail.com)
📍 Karachi, Pakistan

---

## 🌟 Show Your Support

If you found this useful or cool, drop a ⭐ on the repo and share it with your network!

---

## 📝 License

This project is licensed under the MIT License - feel free to use, remix, and deploy for non-commercial or academic use!

```

```
