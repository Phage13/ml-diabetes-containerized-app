@app.route("/predict", methods=["POST"])
def predict():
    try:
        gender = int(request.form["gender"])
        age = float(request.form["age"])
        hypertension = int(request.form["hypertension"])
        heart_disease = int(request.form["heart_disease"])

        smoking_map = {
            "No Info": 0,
            "never": 1,
            "former": 2,
            "current": 3,
            "not current": 4,
            "ever": 5
        }
        smoking_history = smoking_map.get(request.form["smoking_history"], 0)

        bmi = float(request.form["bmi"])
        HbA1c_level = float(request.form["HbA1c_level"])
        blood_glucose_level = float(request.form["blood_glucose_level"])

        # Build DataFrame with enforced numeric types
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

        # Force all columns to numeric
        input_df = input_df.apply(pd.to_numeric, errors="coerce")

        print("DEBUG input_df:", input_df.to_dict())
        print("DEBUG dtypes:", input_df.dtypes)

        prediction = model.predict(input_df)[0]
        output = "Diabetes Detected" if prediction == 1 else "No Diabetes"

        return render_template("index.html", prediction_text=output)

    except Exception as e:
        print("ERROR in predict route:", str(e))
        return render_template("index.html", prediction_text=f"Error: {str(e)}")
