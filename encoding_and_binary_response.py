import PIL.JpegImagePlugin
import requests
from PIL import Image
from io import BytesIO
from pprint import pprint

# resp_obj = requests.get('http://httpbin.org')
# print(resp_obj.status_code)
# print(resp_obj.encoding)
#
# resp_obj.encoding = 'ISO-8859-1'
# print(resp_obj.encoding)
#
# resp_obj = requests.get('https://github.com/timeline.json')
# print(resp_obj.status_code)
# print(resp_obj.text)
# print(resp_obj.encoding)
# resp_obj.encoding = 'ISO-8859-1'
# print(resp_obj.encoding)
# print(resp_obj.text)

resp = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/01_Calanche_Piana.jpg/1024px-01_Calanche_Piana.jpg')

print(type(resp.content))
image = Image.open(BytesIO(resp.content))
print(type(image))
image.save('aurora.png')
Image.open('aurora.png')

