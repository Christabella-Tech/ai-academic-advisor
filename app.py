"""AI Academic Advisor - Flask web app serving a Random Forest model (.pkl)."""
import os
import joblib
import pandas as pd
from flask import Flask, request, render_template, jsonify

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
model = joblib.load(os.path.join(BASE_DIR, "model", "advisor_model.pkl"))

FEATURES = ["prev_cgpa", "study_hours", "attendance", "courses_failed", "sleep_hours"]
LABELS = {0: "At Risk", 1: "Average", 2: "Excellent"}


def get_advice(d, label):
    """Rule-based advice layered on top of the ML prediction."""
    tips = []
    if d["attendance"] < 75:
        tips.append("Raise your attendance above 75% to qualify for exams.")
    if d["study_hours"] < 15:
        tips.append("Aim for at least 15-20 study hours per week.")
    if d["courses_failed"] > 0:
        tips.append("Register carryover courses early and seek tutoring.")
    if d["sleep_hours"] < 6:
        tips.append("Get 6-8 hours of sleep to improve retention.")
    if label == "Excellent" and not tips:
        tips.append("Great work! Keep your routine and consider mentoring peers.")
    return tips or ["Stay consistent and meet your course advisor each semester."]


def run_prediction(data):
    values = {f: float(data[f]) for f in FEATURES}
    row = pd.DataFrame([values])
    label = LABELS[int(model.predict(row)[0])]
    return label, get_advice(values, label)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or request.form
    try:
        label, tips = run_prediction(data)
    except (KeyError, ValueError):
        msg = "Please provide valid numbers for all fields."
        if request.is_json:
            return jsonify({"error": msg}), 400
        return render_template("index.html", error=msg), 400
    if request.is_json:
        return jsonify({"standing": label, "advice": tips})
    return render_template("index.html", standing=label, advice=tips)


if __name__ == "__main__":
    app.run(debug=True)
