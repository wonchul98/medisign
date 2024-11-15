# 서비스 소개

Medisign은 요양보호사의 알약 투약을 돕는 서비스입니다.

# 기획배경

고령화 시대. 요양 보호사들의 인력은 점점 줄어들고 있습니다.

1명의 요양 보호사당 담당하는 노인이 수는 점점 늘어납니다.

이에 따라 알약 오남용 수도 꾸준하게 증가합니다.

전문 지식 없이 노인들의 투약을 돕는 서비스를 기획하였습니다.

# 주요 기능

### 1.병용 금기 알약 탐지 기능

### 2.알약 식별 기능


## Basic Commands

### **User** 모델

*   **List & Create** : `/users/User_list`

    *   **Methods**: GET, POST

*   **Retrieve, Update & Delete** : `/users/User_list/user_id`

    *   **Methods**: GET, PUT, DELETE

### **Medicine** 모델

*   **List & Create** : `/medicines/medicine_list/`

    *   **Methods**: GET, POST

*   **Retrieve, Update & Delete** : `/medicines/medicine_list/medicine_id`

    *   **Methods**: GET, PUT, DELETE

*   **상호작용** : `/medicines/cont/medicine_id`

    *   **Methods**: GET
    *   **Note**: 약의 표준코드 기준 병용 금기 약품 리스트 제공

### **Prescription** 모델

*   **List & Create** : `/medicines/prescription_list/`

    *   **Methods**: GET, POST

*   **Retrieve, Update & Delete** : `/medicines/prescription_list/prescription_id`

    *   **Methods**: GET, PUT, DELETE
    *   **Note**: `dosage_times` 필드는 `dosage_time`의 id 값의 list 형태로 제공. 예시: 09:00, 12:00, 18:00 → [19,25,37]

### **Pharmacy** 모델

*   **Nearby Pharmacies** : `/pharmacies/nearby?lat=위도&lon=경도&distance_km=반경(km)`

    *   **Methods**: GET

*   **Add Regular Pharmacy** : `/users/User_list/user_id`

    *   **Methods**: PUT

*   **List Regular Pharmacy** : `/pharmacies/reg/user_id`

    *   **Methods**: GET

*   **Show Nearby on Map** : `/pharmacies/show_near/?user_id=user_id&lat=lat&lon=lon`

    *   **Note**: 입력받은 좌표 기반으로 주변 약국 지도 정보 제공, user_id 기반의 즐겨찾기된 약국 지도상 표시

*   **Show Selected on Map** : `/pharmacies/show_select/?pharmacy_id=pharmacy_id`

    *   **Note**: 입력받은 pharmacy_id의 위치 지도상 표시

### **Disease** 모델

*   **List & Create** : `/diseases/disease_list`

    *   **Methods**: GET, POST

*   **Retrieve, Update & Delete** : `/diseases/disease_list/disease_id`

    *   **Methods**: GET, PUT, DELETE

### **Widget** 모델

*   **List & Create** : `/widgets/widget_list`

    *   **Methods**: GET, POST

*   **Retrieve, Update & Delete** : `/widgets/widget_list/id`

    *   **Methods**: GET, PUT, DELETE

### **Admin**

*   **Access** : `/admin`

## References

모델 별 상세 사용법은 각 `app_name/tests/test_api.py` 파일을 참고하십시오.
