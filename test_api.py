import requests

url = "https://api.remonline.ua/token/new"

payload={'api_key': '237a1231fe9b4a13b66e5389598b9d85'}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)