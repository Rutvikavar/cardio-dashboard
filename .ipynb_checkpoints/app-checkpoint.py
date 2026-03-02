from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = int(request.form['age'])
        gender = int(request.form['gender'])
        height = int(request.form['height'])
        weight = int(request.form['weight'])
        ap_hi = int(request.form['ap_hi'])
        ap_lo = int(request.form['ap_lo'])
        cholesterol = int(request.form['cholesterol'])
        gluc = int(request.form['gluc'])
        smoke = int(request.form['smoke'])
        alco = int(request.form['alco'])
        active = int(request.form['active'])

        bmi = weight / ((height/100) ** 2)

        input_data = np.array([[
            age, gender, height, weight,
            ap_hi, ap_lo, cholesterol,
            gluc, smoke, alco, active, bmi
        ]])

        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)

        result = "⚠ Cardiovascular Disease Detected" if prediction[0] == 1 else "✅ No Cardiovascular Disease"

        return render_template("index.html", prediction_text=result)

    except:
        return render_template("index.html", prediction_text="❌ Invalid Input")

if __name__ == "__main__":
    app.run(debug=True)
