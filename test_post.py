import requests
from pprint import pprint

r_post = requests.post('https://en.wikipedia.org/w/index.php', data={'search': 'Sli;soft'})
print(r_post.status_code)
print(type(r_post))
pprint(r_post.text)

with open('skillsoft.html', 'wb') as f:
    for chunk in r_post.iter_content(chunk_size=1000):
        f.write(chunk)
