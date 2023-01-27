import requests
from datetime import datetime
import os

APP_ID = os.environ["ENV_APP_ID"]
API_KEY = os.environ["ENV_API_KEY"]

Query_text = input("Tell me which exercises you did: ")
Gender = "Male"
Weight_kg = 56
Height_cm = 170
Age = 24

url_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {"x-app-id": APP_ID,
          "x-app-key": API_KEY}

params = {
    "query": Query_text,
    "gender": Gender,
    "weight_kg": Weight_kg,
    "height_cm": Height_cm,
    "age": Age
}
response = requests.post(url=url_endpoint, json=params, headers=header)
result = response.json()
print(result)


################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m%Y")
now_time = datetime.now().strftime("%X")
sheet_endpoint = os.environ["ENV_sheet_endpoint"]

# Basic Authentication
basic = os.environ["ENV_basic"]
Authorization_Header = {'Authorization': 'Basic ' + basic}
# Bearer Authentication
Bearer = os.environ["ENV_Bearer"]
Authorization_Bearer_Header = {'Authorization': 'Bearer ' + Bearer}
for exercise in result["exercises"]:
    let_body = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=let_body, headers=Authorization_Bearer_Header)
    print(sheet_response.text)