# https://fakerapi.it/api/v1/persons?_quantity=2&_gender=female&_birthday_start=2005-01-01

from django.test import TestCase
import requests
import json
import jsonschema
import re

class Testapi(TestCase):
    def setUp(self):
        self.base_url = 'https://fakerapi.it/'
        self.data_file = 'data.json'

    def test_json_response_validation(self):
        response = requests.get(self.base_url + f'api/v1/persons/')
        self.assertEqual(response.status_code, 200)

        with open(self.data_file, "r") as schema_file:
            schema = jsonschema.Draft7Validator(json.load(schema_file)) 

        json_content = response.json()
        self.assertTrue(schema.is_valid(json_content))

    def test_call_api_endpoint_and_response(self):
        p={'id':3}
        response = requests.get(url= self.base_url + f'api/v1/persons/', params=p)
        self.assertEqual(response.status_code, 200)

        response_json = response.json()
        self.assertIn("total", response_json)
        self.assertEqual(response_json["code"], 200)
        self.assertTrue(response_json["data"][0]['id'])

    def test_fields_types(self):
        response = requests.get(url= self.base_url + f'api/v1/persons/')
        self.assertEqual(response.status_code, 200)

        response_json = response.json()

        self.assertIsInstance(response_json.get("status"), str)
        self.assertIsInstance(response_json.get("code"), int)
        self.assertIsInstance(response_json.get("total"), int)

    def test_mandatory_field(self):
        response = requests.get(url= self.base_url + f'api/v1/persons/')
        self.assertEqual(response.status_code, 200)
        # print(response.headers)
        response_json = response.json()
        with open('data.json') as json_file:
            new_data = json.load(json_file)

        person_email = new_data['data'][0]['email']
        self.assertEqual(person_email, 'mertz.elfrieda@gmail.com')

        self.assertIn('data', response_json)

    def test_valid_email(self):
        with open('data.json') as json_file:
            new_data = json.load(json_file)

        person_email = new_data['data'][0]['email']
        print(person_email)
        regex_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        self.assertTrue(re.match(regex_pattern,person_email))

    def test_valid_phone_number(self):
        with open('data.json') as json_file:
            new_data = json.load(json_file)

        phone_number = new_data['data'][0]['phone']
        regex_pattern = r'^\+(?:\d[\d-]*){1,}$'
        self.assertTrue(re.match(regex_pattern, phone_number))

    def test_valid_url(self):
        with open('data.json') as json_file:
            new_data = json.load(json_file)
        url = new_data['data'][0]['website']
        print(url)
        regex_pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/?'
        self.assertTrue(re.match(regex_pattern, url))

    def test_response_header(self):
        response = requests.get(url= self.base_url + f'api/v1/persons/')
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertIn("X-RateLimit-Limit", response.headers)
        self.assertIn("X-RateLimit-Remaining", response.headers)

    def test_negative_response(self):
        response = requests.get(self.base_url + f"api/v2/persons")
        self.assertEqual(response.status_code, 404)

        error_message = response.json().get("message", "Endpoint not found")
        self.assertEqual(error_message, "Endpoint not found")

    # def test_unauthorized_request(self):
    #     response = requests.get(self.base_url + "api/v1/persons/")
        
    #     self.assertEqual(response.status_code, 401)
    #     error_message = response.json().get("message", "")
    #     self.assertEqual(error_message, "Unauthorized request")

    