import requests
from pprint import pprint
import json

r_head = requests.head('http://example.com')
print(r_head.status_code)
print(r_head.text)
print(r_head.content)

print(r_head.headers)

print(r_head.headers['content-length'])

print(r_head.headers['content-type'])

