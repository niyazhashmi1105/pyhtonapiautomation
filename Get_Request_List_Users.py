import requests
import json
import jsonpath

url = 'https://reqres.in/api/users?page=2'

response = requests.get(url)
#print(response.json())
#print("Response Content: ", response.content)
#print("Response Headers: ", response.headers)

#Using Jsonpath for response parsing
json_response = json.loads(response.text)
print(json_response)

pages = jsonpath.jsonpath(json_response, 'total_pages')
#print(pages[0])

for i in range(0, 6):
    first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print(first_name)

