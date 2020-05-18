import requests

url = 'Http://10.32.36.171:8083/api/TAPWORKS/releaseSMTCarrier'
d = {"carrier_id": "string"}

r = requests.post(url, json=d)
print(r.text)