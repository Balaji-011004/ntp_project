import speech_recognition as sr
import pyttsx3
import pandas as pd
from tensorflow.keras.models import load_model
import joblib
import numpy as np

# Initialize Text-to-Speech
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except:
        speak("Sorry, could not understand.")
        return ""

def predict_next_traffic():
    try:
        df = pd.read_csv("data/live_local_traffic.csv", parse_dates=['timestamp'])
        values = df['bytes_in'].tail(10).tolist()

        model = load_model("models/lstm_model.h5")
        scaler = joblib.load("data/processed/scaler.pkl")

        scaled = scaler.transform(np.array(values).reshape(-1, 1))
        seq = scaled[-10:].reshape(1, 10, 1)

        pred_scaled = model.predict(seq)[0][0]
        prediction = scaler.inverse_transform([[pred_scaled]])[0][0]

        speak(f"Predicted traffic for next interval is approximately {int(prediction)} bytes per minute.")
    except:
        speak("Model or data missing. Please train LSTM model first.")

def current_status():
    df = pd.read_csv("data/live_local_traffic.csv", parse_dates=['timestamp'])
    curr = df['bytes_in'].iloc[-1]
    speak(f"Current network traffic is {int(curr)} bytes per minute.")

def main():
    speak("Voice Assistant Activated. How can I help you?")

    while True:
        cmd = listen()

        if "predict" in cmd:
            predict_next_traffic()

        elif "status" in cmd or "current" in cmd:
            current_status()

        elif "hello" in cmd:
            speak("Hello! I am your traffic monitoring assistant.")

        elif "stop" in cmd or "exit" in cmd:
            speak("Goodbye! Have a great day.")
            break

        else:
            speak("You can say: Predict traffic, Current status, or Stop.")

if __name__ == "__main__":
    main()
