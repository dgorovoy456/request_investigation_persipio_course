import requests

r_put = requests.put('http://httpbin.org/put', data={'key': 'value'})
print(r_put.status_code)
print(type(r_put))
print(r_put.text)


r_option = requests.options('https://httpbin.org/get')
print(type(r_option))
print(r_option.text)
print(r_option.headers)


r_delete = requests.delete('http://httpbin.org/delete')
print(r_delete.status_code)
print(type(r_delete))
print(r_delete.text)
print(r_delete.headers)


