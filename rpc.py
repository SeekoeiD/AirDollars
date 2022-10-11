import requests
import json

url = 'http://user:pass@localhost:2332'
body = {'method':'getblockhash', 'params':[2000]}

x = requests.post(url, json=body)

print(x.text)
print(json.dumps(json.loads(x.text), indent=4))