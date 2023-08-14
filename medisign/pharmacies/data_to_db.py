import pandas as pd
import sys
print(sys.path)
from medisign.pharmacies.models import Pharmacy

def upload_data_from_excel(file_path):
    # Load the data from the Excel file
    data = pd.read_excel(file_path)
    print("excel read complete")
    # Create a list of Pharmacy instances from the data
    instances = [
        Pharmacy(
            encrypted_care_symbol=row['암호화요양기호'],
            care_institution_name=row['요양기관명'],
            city_code=row['시도코드'],
            city_name=row['시도코드명'],
            district_code=row['시군구코드'],
            district_name=row['시군구코드명'],
            subdistrict=row['읍면동'],
            postal_code=row['우편번호'],
            address=row['주소'],
            phone_number=row['전화번호'],
            coord_x=row['좌표(x)'],
            coord_y=row['좌표(y)']
        ) for _, row in data.iterrows()
    ]

    # Save the instances to the database
    Pharmacy.objects.bulk_create(instances)

# Call the function with the path to your Excel file
upload_data_from_excel('C:/Users/Administrator/Desktop/2.약국정보서비스.xlsx')