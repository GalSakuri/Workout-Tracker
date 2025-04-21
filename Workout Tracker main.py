import os
import requests
from datetime import datetime

APP_ID = os.environ.get("EXERCISE_API_ID")
API_KEY = os.environ.get("EXERCISE_API_KEY")
USERNAME = os.environ.get("SHEET_USERNAME")
PASSWORD = os.environ.get("SHEET_PASSWORD")

GENDER = "YOUR_GENDER"  # int, number
WEIGHT_KG = "YOUR_WEIGHT"  # int, number
HEIGHT_CM = "YOUR_HEIGHT"  # int, number (example: 1.75)
AGE = "YOUR_AGE"  # int, number

Nutritionix_endpoint = "https://trackapi.nutritionix.com/"
exercise_endpoint = "v2/natural/exercise"
SHEETY_url_endpoint = os.environ.get("SHEET_ENDPOINT")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

params = {
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "query": input("Which exercises you did? : "),
}

response_exercise = requests.post(
    url=f"{Nutritionix_endpoint}/{exercise_endpoint}", json=params, headers=headers)
print(response_exercise.json())


today = datetime.now().strftime("%d/%m/%Y")
now = datetime.now().strftime("%X")

data = response_exercise.json()

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        url=SHEETY_url_endpoint,
        json=sheet_inputs,
        auth=(
            USERNAME,
            PASSWORD,
        )
    )

print(f"{sheet_response.text},{sheet_response.status_code}")
