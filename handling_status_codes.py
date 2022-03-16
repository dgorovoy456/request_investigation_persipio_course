import requests
from pprint import pprint

ok_resp = requests.get('http://example.com')
print(type(ok_resp.headers))
print(ok_resp.headers)
print(ok_resp.status_code)
print(ok_resp.ok)

bad_resp = requests.get('https://yahoo.com/fsdgfdgdgf')
print(bad_resp.headers)
print(bad_resp.status_code)
print(bad_resp.ok)
print(bad_resp.raise_for_status())

