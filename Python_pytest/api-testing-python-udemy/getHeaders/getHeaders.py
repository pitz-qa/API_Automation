import requests

headetdata = {'T1':'firstheader','T2':'secondheader'}
responce = requests.get('http://httpbin.org/get',headers=headetdata)
print(responce.text)