from flask import Flask, render_template, request
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load the trained model once at startup
model = joblib.load("heartDiseasePredction.pkl")

# Features used during training
feature_names = [
    "age", "Sex_male", "cigsPerDay", "BPMeds",
    "diabetes", "BMI", "totChol", "sysBP", "glucose"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Extract inputs from form
            input_data = []
            for feat in feature_names:
                val = request.form.get(feat)
                if val is None or val.strip() == '':
                    return render_template('predict.html', error=f"Missing value for {feat}")
                input_data.append(float(val))

            # Prepare DataFrame for prediction
            input_df = pd.DataFrame([input_data], columns=feature_names)

            # Predict and get probability
            prediction = model.predict(input_df)[0]
            proba = model.predict_proba(input_df)[0][1]

            label = "Heart Disease Risk" if prediction == 1 else "No Heart Disease Risk"

            return render_template(
                'predict.html',
                prediction=label,
                probability=f"{proba:.2f}"
            )
        except Exception as e:
            return render_template('predict.html', error=str(e))
    else:
        # GET request: show form
        return render_template('predict.html')

if __name__ == '__main__':
    port = int(os.getenv("PORT", 7860))  # Hugging Face provides PORT env var
    app.run(debug=False, host="0.0.0.0", port=port)
