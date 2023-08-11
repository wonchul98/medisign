# medisign

Behold My Awesome Project!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## model schema
![](medisign%20%EB%AA%A8%EB%8D%B8%20%EC%8A%A4%ED%82%A4%EB%A7%88.drawio.png) 

## 배포 URL
https://medisign-hackthon-95c791df694a.herokuapp.com/ <br><br>


# Basic Commands

## **User** 모델<br>

> /users/User_list<br>

get, post 방식으로 user정보 조회, 추가<br><br>
> /users/User_list/`user_id`<br>

get, put, delete 방식으로 user정보 조회, 수정, 삭제<br><br>

## **Medicine** 모델<br>
> /medicines/medicine_list/<br>

get, post 방식으로 medicine정보 조회, 추가<br><br>
>/medicines/medicine_list/`medicine_id`<br>

get, put, delete 방식으로 medicine정보 조회, 수정, 삭제<br><br>

## **Pharmacy** 모델<br>
> /pharmacies/nearby?lat=`위도`&lon=`경도`&distance_km=`반경(km)`
<br>

get 방식으로 주변 약국 리스트 조회 (거리 순)<br><br>


> /pharmacies/show_near/?user_id=`user_id`

주변 약국 지도 정보 html로 제공<br><br>

## **Disease** 모델<br>

> /diseases/disease_list<br>

get, post 방식으로 disease정보 조회, 추가<br><Br>
> /diseases/disease_list/`disease_id`<br>

get, put, delete 방식으로 user정보 조회, 수정, 삭제<br><br>



### 단골 약국 추가
/users/User_list/user_id 에 put 방식으로 request<br>
(medisign/user/tests/test.py에 샘플 코드 있음)

<br><br>
### 모델 별 정확한 사용법은 `app_name`/tests/test_api.py 참고
<br>


