import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medisign.settings') 
django.setup()

from medisign.medicines.models import Contraindication 

def upload_csv_to_db(csv_file_path):
    with open(csv_file_path, 'r', encoding='cp949') as csv_file:
        print("opened")
        reader = csv.DictReader(csv_file)

        for row in reader:
            contraindication = Contraindication(
                drugNameA=row['제품명A'],
                drugNumberA=row['제품코드A'],
                ingredientNameA=row['성분명A'],
                companyNameA=row['업체명A'],
                drugNameB=row['제품명B'],
                drugNumberB=row['제품코드B'],
                ingredientNameB=row['성분명B'],
                companyNameB=row['업체명B'],
                detail = row['상세정보']
            )
            contraindication.save()

if __name__ == '__main__':
    csv_file_path = 'C:/Users/Administrator/Desktop/병용금기.csv' 
    print("start")
    upload_csv_to_db(csv_file_path)
    print("end")
