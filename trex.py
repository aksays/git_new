import requests

test = requests.get("https://www.example.com")
print(test.status_code)