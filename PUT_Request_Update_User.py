import jsonpath
import requests
import json

url = 'https://reqres.in/api/users/2'

file = open('D:\\pythonProject\\PythonAPIAutomation\\Update_User.json', 'r')
json_payload = file.read()
request_payload = json.loads(json_payload)

response = requests.put(url, request_payload)
json_response = json.loads(response.text)
print(json_response)
updated_at = jsonpath.jsonpath(json_response, 'updatedAt')

print(updated_at[0])
assert response.status_code == 200
