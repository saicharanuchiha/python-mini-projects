import os
import json
import requests
from datetime import datetime

USERNAME = os.environ.get("PIXELA_USERNAME")
TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = "workout-time"

pixela_endpoint = "https://pixe.la/v1/users"
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()

headers = {
    "X-USER-TOKEN": TOKEN
}

workout_duration = input("How many minutes did the workout last? ")
workout_variation = input("What is the workout variation? ")

post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": workout_duration,
    "optionalData": json.dumps({"workout": workout_variation}),
}

response = requests.post(
    url=pixel_creation_endpoint,
    json=post_config,
    headers=headers
)
print(response.text)