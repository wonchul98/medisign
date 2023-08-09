import requests

url = "http://127.0.0.1:8000/users/User_list/1" # 수정할 유저 아이디 
data = {
    "regular_pharmacy": [4, 5, 6] # 추가할 pharmacy_id
}
headers = {
    "Content-Type": "application/json"
}
 
response = requests.put(url, json=data, headers=headers) #put방식으로 request
# print(response.text)