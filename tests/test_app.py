import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app, get_advice

VALID = {"prev_cgpa": 4.5, "study_hours": 30, "attendance": 95,
         "courses_failed": 0, "sleep_hours": 8}


def test_home_page():
    r = app.test_client().get("/")
    assert r.status_code == 200


def test_predict_api():
    r = app.test_client().post("/predict", json=VALID)
    assert r.status_code == 200
    assert r.get_json()["standing"] in ["At Risk", "Average", "Excellent"]


def test_predict_form():
    r = app.test_client().post("/predict", data=VALID)
    assert r.status_code == 200
    assert b"Predicted standing" in r.data


def test_missing_field_returns_400():
    r = app.test_client().post("/predict", json={"prev_cgpa": 3})
    assert r.status_code == 400


def test_advice_rules():
    tips = get_advice({"attendance": 50, "study_hours": 5,
                       "courses_failed": 2, "sleep_hours": 4}, "At Risk")
    assert len(tips) == 4
