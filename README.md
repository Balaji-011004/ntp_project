# 🚦 Network Traffic Prediction System

A Machine Learning based application that predicts network traffic using time series analysis and deep learning (LSTM).  
The project also includes an interactive **Streamlit dashboard** to visualize predictions and traffic trends.

---

## 📌 Project Overview

Network traffic prediction helps network administrators:

- Predict congestion
- Optimize bandwidth usage
- Improve network reliability
- Detect abnormal traffic patterns

This project implements **ARIMA and LSTM models** to forecast network traffic.

---

## 🧠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Streamlit | Interactive web dashboard |
| TensorFlow / Keras | Deep learning model (LSTM) |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Scikit-learn | Data preprocessing |
| Matplotlib | Visualization |
| Folium | Interactive maps |

---

## 📂 Project Structure
ntp_project
│
├── src/ # Source code
│ ├── app_streamlit.py # Streamlit dashboard
│ ├── preprocess.py # Data preprocessing
│ ├── train_lstm.py # Model training
│
├── data/ # Dataset
├── models/ # Saved models
├── requirements.txt # Python dependencies
├── README.md # Project documentation

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/ntp_project.git
cd ntp_project
## ⚙️ Setup Instructions

Follow the steps below to run the project locally.

### 1️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 2️⃣ Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### 1️⃣ Generate Dataset and Preprocess Data

```bash
python src/preprocess.py --generate
```

This step generates the dataset and performs preprocessing required for model training.

---

### 2️⃣ Train the LSTM Model

```bash
python src/train_lstm.py
```

This script trains the **LSTM model** using the preprocessed traffic data.

---

### 3️⃣ Run the Streamlit Dashboard

```bash
streamlit run src/app_streamlit.py
```

This will start the **Streamlit dashboard** where you can visualize traffic predictions.

Open your browser and go to:

```
http://localhost:8501
```
