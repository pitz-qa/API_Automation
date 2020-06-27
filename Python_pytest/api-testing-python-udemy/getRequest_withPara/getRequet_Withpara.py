import requests

para = {'name':'Google','Adress':'USA','Mobile':1234567890}
responce = requests.get('http://httpbin.org/get',params=para)
print(responce.text)