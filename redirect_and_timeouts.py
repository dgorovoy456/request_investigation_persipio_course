import requests
from pprint import pprint

response = requests.get('http://gmail.com')
print(response.history)
print(response.status_code)
print(response.url)

if response.history:
    print('Redirect history:')
    for resp in response.history:
        print(resp.status_code, resp.url)
    print('\nFinal destination:')
    print(response.status_code, response.url)
else:
    print('Request was not redirected')

print(response.is_redirect)
print(response.is_permanent_redirect)
print(response.history[0].is_redirect)

response = requests.get('http://google.com', allow_redirects=False)
print(response.status_code)
print(response.raise_for_status())
print(response.history)

response = requests.get('http://google.com', allow_redirects=True)
print(response.status_code)
print(response.raise_for_status())
print(response.history)

if response.history:
    print('Redirect history:')
    for resp in response.history:
        print(resp.status_code, resp.url)
    print('\nFinal destination:')
    print(response.status_code, response.url)
else:
    print('Request was not redirected')

print(response.is_redirect)
print(response.is_permanent_redirect)
print(response.history[0].is_redirect)

# resp = requests.get('http://github.com', timeout=0.001)
# print(resp.status_code)

resp = requests.get('http://github.com', timeout=(5, 18))
print('\n', resp.status_code)

resp = requests.get('http://github.com', timeout=None)
print('\n', resp.status_code)
