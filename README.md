# AI Academic Advisor

CSC 303 assignment: an academic advisor that combines an AI technique (Random Forest
classification) with standard software engineering practice (Git, GitHub, tests, Flask web app).

A student enters their previous CGPA, weekly study hours, attendance, number of failed
courses and nightly sleep hours. The model predicts their standing (**At Risk**, **Average**
or **Excellent**) and rule-based logic adds personalised advice.

> The training data is **synthetic**, generated for demonstration. A real deployment would
> use actual student records.

## Project structure
```
ai-academic-advisor/
├── app.py                      Flask app (loads the .pkl)
├── requirements.txt
├── data/student_data.csv       Training data (synthetic)
├── model/advisor_model.pkl     Trained Random Forest
├── notebooks/train_advisor_model.ipynb   Google Colab training notebook
├── templates/index.html
├── tests/test_app.py
└── .vscode/                    Python-optimised VS Code settings
```

## Setup
```bash
python -m venv venv
venv\Scripts\activate          # Windows (Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
```

## Run
```bash
python app.py                   # open http://127.0.0.1:5000
pytest                          # run tests
```

## Retrain the model
Open `notebooks/train_advisor_model.ipynb` in Google Colab, run all cells, and replace
`model/advisor_model.pkl` with the downloaded file.

## Git and GitHub
```bash
git init
git add .
git commit -m "Initial commit: AI academic advisor"
git branch -M main
git remote add origin https://github.com/<your-username>/ai-academic-advisor.git
git push -u origin main
```
