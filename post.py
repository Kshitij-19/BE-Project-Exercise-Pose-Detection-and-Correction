import requests

url = "https://postman-echo.com/post"

payload={}
files=[
  ('',('sample_bicep_curl.mp4',open('sample_bicep_curl.mp4','rb'),'application/octet-stream'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
