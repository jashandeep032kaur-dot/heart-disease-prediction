from flask import Flask, render_template, request
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load the trained model
model_path = "heartDiseasePredction.pkl"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}")
model = joblib.load(model_path)

# Features used in the model
feature_names = ['age', 'Sex_male', 'cigsPerDay', 'BPMeds', 'diabetes',
                 'BMI', 'totChol', 'sysBP', 'glucose']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Extract input values from form
            input_data = []
            for feat in feature_names:
                val = request.form.get(feat)
                if val is None or val.strip() == '':
                    return render_template('predict.html', error=f"Missing value for {feat}")
                input_data.append(float(val))
            
            # Prepare DataFrame for model
            input_df = pd.DataFrame([input_data], columns=feature_names)
            
            # Make prediction
            prediction_val = model.predict(input_df)[0]
            probability_val = model.predict_proba(input_df)[0][1]
            
            label = "Heart Disease Risk" if prediction_val == 1 else "No Heart Disease Risk"
            
            return render_template('predict.html', prediction=label, probability=f"{probability_val:.2f}")
        except Exception as e:
            return render_template('predict.html', error=str(e))
    else:
        # GET request: render the form
        return render_template('predict.html')

if __name__ == '__main__':
    # Hugging Face Spaces automatically sets PORT
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port)
