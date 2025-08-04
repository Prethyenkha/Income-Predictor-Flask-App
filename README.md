# 💼 Income Predictor Web App

This is a simple Flask web application that uses a trained Linear Regression model to predict income based on a user's **age** and **years of experience**.

## 🚀 Features
- Trained using `scikit-learn`
- Flask web interface with colorful Bootstrap UI
- Interactive input form
- Model serialized using `joblib` (`.pkl` file)

## 📁 Project Structure
```
Linear Regression/
├── app.py
├── linear_regression_model.pkl
├── requirements.txt
├── templates/
│   └── index.html
└── README.md
```

## 🧰 Requirements
```bash
pip install -r requirements.txt
```

## 🖥️ How to Run
```bash
cd "your/project/path"
python app.py
```

## 📦 Model Info
Trained on features: `age`, `experience` to predict `income`.

## 🔒 License
Free to use for learning and education.
