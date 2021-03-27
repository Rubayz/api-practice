import requests
calling_api = requests.get("https://cat-fact.herokuapp.com")
finding_status = calling_api.status_code
print(finding_status)