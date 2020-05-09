import requests

demo_url='http://0.0.0.0/demo/api/v1.0/servername/'
for i in range(10):
    resp = requests.get(demo_url + str(i+1))
    print(resp.text)

