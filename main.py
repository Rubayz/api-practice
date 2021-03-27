import requests
calling_api = requests.get("https://cat-fact.herokuapp.com/facts")
print(calling_api.status_code)
print(calling_api.json())