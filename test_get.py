import requests
from pprint import pprint
import json

print(requests.__version__)
print(requests.__copyright__)

r_get = requests.get(
    'https://www.metaweather.com/api/location/2487956/2018/11/28')
print(r_get.status_code)
print(type(r_get))
print(r_get.headers)
pprint(r_get.headers)
data = json.loads(r_get.text)
pprint(data)
pprint(r_get.text)
print(r_get.is_redirect)

###########################################

f_get = requests.get('http://swapi.co/api/planets/3')
print(f_get.status_code)
print(f_get.headers)
print()
print(f_get.text)
pprint(f_get.text)


