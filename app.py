from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('linear_regression_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    experience = float(request.form['experience'])

    # Make prediction
    prediction = model.predict(np.array([[age, experience]]))[0]
    prediction = round(prediction, 2)

    return render_template('index.html', prediction_text=f'Predicted Income: ${prediction}')

if __name__ == '__main__':
    app.run(debug=True)
