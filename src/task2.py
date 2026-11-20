#Task2

#Creating Json file

import csv
import json

with open("data/employee18.csv", "r") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

with open("data/employees.json", "w") as file:
    json.dump(employees, file, indent=4)

high_earners = [
    emp for emp in employees 
    if int(emp["salary"]) > 50000
]

with open("data/high_earners.csv", "w", newline="") as file:
    fieldnames = employees[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(high_earners)

print("Rows read:", len(employees))
print("High earners:", len(high_earners))

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
print("API key loaded:", api_key is not None)

#Get API request

import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    users = response.json()
    for user in users[:3]:
        print("ID:", user["id"])
        print("Name:", user["name"])
        print("Email:", user["email"])
        print()

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/9999",
        timeout=5
    )
    response.raise_for_status()

except requests.exceptions.HTTPError:
    print("/users/9999 -> 404 Not found")

#Extract Nested Json field

import requests
import json

response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    timeout=5
)

users = response.json()
user_details = []
for user in users:
    details = {
        "id": user.get("id"),
        "name": user.get("name"),
        "email": user.get("email"),
        "city": user.get("address", {}).get("city"),
        "company": user.get("company", {}).get("name")
    }
    user_details.append(details)

with open("data/users.json", "w") as file:
    json.dump(user_details, file, indent=4)

print("User details saved successfully")