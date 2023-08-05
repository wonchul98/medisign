import requests
import json

url = "https://medisign-hackthon-95c791df694a.herokuapp.com/users/auth"

response = requests.post(url, data = {'username': 'admin', 'password' : '1'})
myToken = response.json()['token'] # JSON 형식에서 토큰 추출
print(myToken)

header = {'Authorization': 'Token '+ myToken} # 'Token'을 사용
response = requests.get('https://medisign-hackthon-95c791df694a.herokuapp.com/users/User_list', headers = header)
print(response.text)