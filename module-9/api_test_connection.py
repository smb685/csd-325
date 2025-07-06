import requests

response = requests.get('http://www.google.com')
print("Connection status to Google:", response.status_code)