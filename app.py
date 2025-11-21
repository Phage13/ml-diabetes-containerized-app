from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load your trained model
model = joblib.load("models/best_diabetes_model.pkl")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Example: collect form inputs
    data = [float(x) for x in request.form.values()]
    prediction = model.predict([np.array(data)])
    return render_template("index.html", prediction=prediction[0])

if __name__ == "__main__":
    app.run(debug=True)
