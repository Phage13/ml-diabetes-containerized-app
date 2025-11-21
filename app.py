from flask import Flask, render_template, request
import joblib
import pandas as pd

# Create Flask app
app = Flask(__name__)

# Load trained model (make sure this file exists in /models)
model = joblib.load("models/best_diabetes_model.pkl")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract form inputs
        gender = int(request.form["gender"])
        age = float(request.form["age"])
        hypertension = int(request.form["hypertension"])
        heart_disease = int(request.form["heart_disease"])

        # Pass raw string for smoking_history (pipeline expects strings)
        smoking_history = request.form["smoking_history"]

        bmi = float(request.form["bmi"])
        HbA1c_level = float(request.form["HbA1c_level"])
        blood_glucose_level = float(request.form["blood_glucose_level"])

        # Build DataFrame with same column names used in training
        input_df = pd.DataFrame([{
            "gender": gender,
            "age": age,
            "hypertension": hypertension,
            "heart_disease": heart_disease,
            "smoking_history": smoking_history,
            "bmi": bmi,
            "HbA1c_level": HbA1c_level,
            "blood_glucose_level": blood_glucose_level
        }])

        # Debug logs to Heroku
        print("DEBUG input_df:", input_df.to_dict())
        print("DEBUG dtypes:", input_df.dtypes)

        # Make prediction
        prediction = model.predict(input_df)[0]

        # Updated output wording
        output = "High Risk" if prediction == 1 else "Normal Risk"

        return render_template("index.html", prediction_text=output)

    except Exception as e:
        print("ERROR in predict route:", str(e))
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
