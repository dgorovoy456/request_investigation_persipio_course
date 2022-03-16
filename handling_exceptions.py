import requests
from pprint import pprint
from requests import exceptions

try:
    requests.get('http://nonexistent.com/')

except exceptions.ConnectionError:
    print('Error: Connection error')

try:
    resp = requests.get('http://github.com', timeout=0.001)
except exceptions.ConnectTimeout:
    print('Error: Timeout error')
