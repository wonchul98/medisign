import requests
import json

url = "http://127.0.0.1:8000/medicines/auth"

response = requests.post(url, data = {'username': 'admin', 'password' : '1'})
myToken = response.json()['token'] # JSON 형식에서 토큰 추출
print(myToken)

header = {'Authorization': 'Token '+ myToken} # 'Token'을 사용
response = requests.get('http://127.0.0.1:8000/medicines/Medicine_list', headers = header)
print(response.text)