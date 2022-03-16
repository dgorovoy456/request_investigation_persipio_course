import requests
from pprint import pprint
import json

resp_obj = requests.get('https://swapi.dev/api/vehicles/4/')
print(resp_obj.status_code)
print(resp_obj.json())
pprint(resp_obj.json())
print('\n', resp_obj.headers['content-type'])

resp_obj = requests.get('https://swapi.dev/api/vehicles/4/', stream=True)
print(resp_obj.status_code)
print(resp_obj.raw)
print(resp_obj.raw.read(10))
pprint(resp_obj.raw.read(10))

with requests.get('https://swapi.dev/api/vehicles/4/', stream=True) as response:
    with open('raw_file.txt', 'wb') as b:
        for chunk in response.iter_content(1000):
            b.write(chunk)
