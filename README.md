# 🚦 Smart Traffic Monitoring & Prediction System

An **AI-powered Smart Traffic Monitoring and Prediction System** that analyzes traffic patterns and predicts future traffic conditions using **Machine Learning and Deep Learning models**.
The project also provides an **interactive Streamlit dashboard** for real-time visualization and traffic insights.

---

# 📌 Project Overview

Traffic congestion is a major problem in modern cities. This project aims to build an intelligent system that can:

* Analyze historical traffic data
* Predict traffic congestion
* Visualize traffic patterns
* Assist in better traffic management

The system uses **Machine Learning algorithms and LSTM neural networks** to forecast traffic flow and provide insights through an interactive dashboard.

---

# 🎯 Objectives

* Predict future traffic congestion using AI
* Analyze historical traffic flow patterns
* Visualize traffic data interactively
* Provide a user-friendly dashboard for monitoring traffic

---

# 🧠 Technologies Used

| Technology         | Purpose                    |
| ------------------ | -------------------------- |
| Python             | Core programming language  |
| Pandas             | Data analysis              |
| NumPy              | Numerical computations     |
| Scikit-learn       | Machine learning models    |
| TensorFlow / Keras | Deep learning (LSTM model) |
| XGBoost            | Traffic prediction model   |
| Streamlit          | Interactive dashboard      |
| Matplotlib         | Data visualization         |
| Folium             | Map visualization          |

---

# 🏗 Project Architecture

```
Traffic Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Feature Engineering
      │
      ▼
Model Training
(Random Forest / XGBoost / LSTM)
      │
      ▼
Traffic Prediction
      │
      ▼
Streamlit Dashboard
      │
      ▼
Traffic Visualization & Insights
```

---

# 📂 Project Structure

```
ntp_project
│
├── data/
│   └── traffic_dataset.csv
│
├── models/
│   └── lstm_model.pkl
│
├── src/
│   ├── preprocess.py
│   ├── train_lstm.py
│   └── app_streamlit.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```
git clone https://github.com/Balaji-011004/ntp_project.git
cd ntp_project
```

---

## 2️⃣ Create Virtual Environment

```
python -m venv venv
```

### Activate Environment

Windows

```
venv\Scripts\activate
```

Linux / Mac

```
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

# ▶️ Running the Project

## Step 1: Generate Dataset & Preprocess

```
python src/preprocess.py --generate
```

This step:

* Generates the traffic dataset
* Cleans and preprocesses the data

---

## Step 2: Train the LSTM Model

```
python src/train_lstm.py
```

This will:

* Train the deep learning model
* Save the trained model in the **models/** folder

---

## Step 3: Run the Streamlit Dashboard

```
streamlit run src/app_streamlit.py
```

The dashboard will open in your browser.

---

# 📊 Features

✔ Traffic congestion prediction
✔ Machine learning based forecasting
✔ Deep learning (LSTM) model
✔ Interactive data visualization
✔ Streamlit web dashboard
✔ Traffic hotspot analysis
✔ Map-based visualization

---

# 📸 Dashboard Preview

Features available in the dashboard:

* Traffic prediction charts
* Congestion level analysis
* Historical traffic patterns
* Interactive visualizations
* Map-based traffic monitoring

---

# 🚀 Deployment

The project can be deployed using:

* **Streamlit Cloud**
* **Vercel (Frontend)**
* **Docker**
* **AWS / GCP**

For Streamlit deployment:

1. Push project to GitHub
2. Connect repository to Streamlit Cloud
3. Select:

```
src/app_streamlit.py
```

as the main file.

---

# 🔮 Future Improvements

* Real-time traffic data integration
* IoT sensor data support
* Smart traffic signal control
* Mobile application interface
* Advanced deep learning models
* Real-time map traffic monitoring

---

# 🤝 Contributing

Contributions are welcome!

Steps:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Balaji**

AI & Data Science Enthusiast
Machine Learning | Deep Learning | Data Analytics

---

⭐ If you like this project, please **star the repository**!
