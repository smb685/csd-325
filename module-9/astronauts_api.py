import requests
import json

# Test the connection
url = "http://api.open-notify.org/astros.json"
response = requests.get(url)

print("Connection status to astronaut API:", response.status_code)

# Print raw JSON response
print("\nRaw JSON Response:")
print(response.text)

# Formatted output
print("\nFormatted Astronaut Data:")
data = response.json()
print("Number of people in space:", data['number'])
for person in data['people']:
    print(f"Name: {person['name']} - Craft: {person['craft']}")
