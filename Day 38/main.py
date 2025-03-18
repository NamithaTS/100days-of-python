
import requests

GENDER = "Female"
WEIGHT_KG = 50
HEIGHT_CM = 152
AGE = 21

APP_ID="0da7185a"
API_KEY="254ffc6f93afd2a509dc71ab9d645c25"



exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)