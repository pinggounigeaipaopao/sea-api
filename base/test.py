import requests

paydata = {"sn":"F1N717P002774"}
r = requests.get(url='http://os-prod.duochang.cc/api/device/v1/device/oauth',params=paydata)
print(r.status_code)
print(r.text)