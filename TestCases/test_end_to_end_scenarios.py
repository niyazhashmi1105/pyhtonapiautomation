import requests
import json
import jsonpath

BASE_URL = 'https://reqres.in/api'


def test_get_list_users():
    url = BASE_URL + '/users?page=2'
    response = requests.get(url)
    json_response = json.loads(response.text)
    assert response.status_code == 200
    pages = jsonpath.jsonpath(json_response, 'total_pages')
    assert pages[0] == 2


def test_create_user():
    url = BASE_URL + '/users'
    file = open('D:\\pythonProject\\PythonAPIAutomation\\Create_User.json', 'r')
    json_payload = file.read()
    request_payload = json.loads(json_payload)
    response = requests.post(url, request_payload)
    assert response.status_code == 201
    json_response = json.loads(response.text)
    name = jsonpath.jsonpath(json_response, 'name')
    assert name[0] == 'morpheus'


def test_update_user():
    url = BASE_URL + '/users/2'
    file = open('D:\\pythonProject\\PythonAPIAutomation\\Update_User.json', 'r')
    json_payload = file.read()
    request_payload = json.loads(json_payload)
    response = requests.put(url, request_payload)
    json_response = json.loads(response.text)
    updated_at = jsonpath.jsonpath(json_response, 'updatedAt')
    assert response.status_code == 200


def test_delete_user():
    url = BASE_URL + '/users/2'
    response = requests.delete(url)
    assert response.status_code == 204
