import jsonpath
import requests
import json


url = 'https://reqres.in/api/users'

file = open('D:\\pythonProject\\PythonAPIAutomation\\Create_User.json', 'r')
json_payload = file.read()
request_payload = json.loads(json_payload)

response = requests.post(url, request_payload)
json_response = json.loads(response.text)
id = jsonpath.jsonpath(json_response, 'id')
print(id[0])
assert response.status_code == 201
