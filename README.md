# medisign

Behold My Awesome Project!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT



## Table of Contents

- [Settings](#settings)
- [Model Schema](#model-schema)
- [배포 URL](#배포-url)
- [Basic Commands](#basic-commands)
  - [User 모델](#user-모델)
  - [Medicine 모델](#medicine-모델)
  - [Prescription 모델](#prescription-모델)
  - [Pharmacy 모델](#pharmacy-모델)
  - [Disease 모델](#disease-모델)
  - [Admin](#admin)
- [References](#references)

## Settings

- [Official Settings Documentation](http://cookiecutter-django.readthedocs.io/en/latest/settings.html)

## Model Schema

![Model Schema](medisign%20%EB%AA%A8%EB%8D%B8%20%EC%8A%A4%ED%82%A4%EB%A7%88.drawio.png)

## 배포 URL

https://medisign-hackthon-95c791df694a.herokuapp.com/

## Basic Commands

### **User** 모델

- **List & Create** : `/users/User_list`
  - **Methods**: GET, POST
- **Retrieve, Update & Delete** : `/users/User_list/user_id`
  - **Methods**: GET, PUT, DELETE

### **Medicine** 모델

- **List & Create** : `/medicines/medicine_list/`
  - **Methods**: GET, POST
- **Retrieve, Update & Delete** : `/medicines/medicine_list/medicine_id`
  - **Methods**: GET, PUT, DELETE

### **Prescription** 모델

- **List & Create** : `/medicines/prescription_list/`
  - **Methods**: GET, POST
- **Retrieve, Update & Delete** : `/medicines/prescription_list/prescription_id`
  - **Methods**: GET, PUT, DELETE
  - **Note**: `dosage_times` 필드는 `dosage_time`의 id 값의 list 형태로 제공. 예시: 09:00, 12:00, 18:00 → [19,25,37]

### **Pharmacy** 모델

- **Nearby Pharmacies** : `/pharmacies/nearby?lat=위도&lon=경도&distance_km=반경(km)`
  - **Methods**: GET
- **Add Regular Pharmacy** : `/users/User_list/user_id`
  - **Methods**: PUT
- **Show Regular Pharmacy** : `/pharmacies/reg/user_id`
  - **Methods**: GET  
- **Show Nearby on Map** : `/pharmacies/show_near/?user_id=user_id`
  - **Note**: 현재 위치 기반으로 주변 약국 지도 정보 제공, 즐겨찾기된 약국 지도상 표시
- **Show Selected on Map** : `/pharmacies/show_select/?pharmacy_id=pharmacy_id`
  - **Note**: 입력받은 pharmacy_id의 위치 지도상 표시

### **Disease** 모델

- **List & Create** : `/diseases/disease_list`
  - **Methods**: GET, POST
- **Retrieve, Update & Delete** : `/diseases/disease_list/disease_id`
  - **Methods**: GET, PUT, DELETE

### **Admin**

- **Access** : `/admin`

## References

모델 별 상세 사용법은 각 `app_name/tests/test_api.py` 파일을 참고하십시오.


