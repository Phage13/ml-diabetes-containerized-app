@app.route("/predict", methods=["POST"])
def predict():
    try:
        gender = int(request.form["gender"])
        age = float(request.form["age"])
        hypertension = int(request.form["hypertension"])
        heart_disease = int(request.form["heart_disease"])

        # Encode categorical smoking history
        smoking_map = {
            "No Info": 0,
            "never": 1,
            "former": 2,
            "current": 3,
            "not current": 4,
            "ever": 5
        }
        smoking_history = smoking_map[request.form["smoking_history"]]

        bmi = float(request.form["bmi"])
        HbA1c_level = float(request.form["HbA1c_level"])
        blood_glucose_level = float(request.form["blood_glucose_level"])

        # Arrange features in the same order your model was trained on
        features = [[gender, age, hypertension, heart_disease,
                     smoking_history, bmi, HbA1c_level, blood_glucose_level]]

        print("DEBUG features:", features)  # shows up in Heroku logs

        prediction = model.predict(features)[0]
        output = "Diabetes Detected" if prediction == 1 else "No Diabetes"

        return render_template("index.html", prediction_text=output)

    except Exception as e:
        print("ERROR in predict route:", str(e))
        return render_template("index.html", prediction_text=f"Error: {str(e)}")
