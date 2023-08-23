import requests

url = 'http://127.0.0.1:8000/medicines/add_medicine/'

# 이미지와 함께 데이터를 보내기 위한 multipart/form-data 요청을 생성
files = {'image': open('path_to_image.jpg', 'rb')}
data = {
    'name': 'Medicine Name',
    'description': 'Medicine Description'
}

response = requests.post(url, data=data, files=files)
print(response.json())