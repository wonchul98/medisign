import requests
from bs4 import BeautifulSoup
from medisign.medicines.models import Medicine, ItemSeq
import base64
import boto3
from io import BytesIO
from PIL import Image
import os
import uuid

AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
BUCKET_NAME = 'medisign-bucket'

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

def generate_file_name():
    return f"{uuid.uuid4().hex}"

def data_url_to_image(data_url):
    format, datastr = data_url.split(';base64,')
    decoded = base64.b64decode(datastr)
    image = Image.open(BytesIO(decoded))
    return image

# 이미지 파일을 S3에 업로드
def upload_to_s3(image, bucket_name, file_name):
    s3 = boto3.client('s3')
    
    # 이미지를 바이트 형식으로 변환
    buffer = BytesIO()
    image.save(buffer, format='JPEG')
    buffer.seek(0)
    
    # 'medicine_images/' 폴더 내에 파일을 업로드하기 위해 경로를 추가합니다.
    s3_key = f"medicine_images/{file_name}"
    
    # S3에 업로드
    s3.upload_fileobj(buffer, bucket_name, s3_key, ExtraArgs={'ContentType': 'image/jpeg'})
    
    # S3 URL 반환
    url = f"https://{bucket_name}.s3.amazonaws.com/{s3_key}"
    # print(url)
    return url

def extract_info_from_div(content_div):
    data_dict = {}
    h3_tags = content_div.find_all('h3', class_='cont_title4')
    div_tags = content_div.find_all('div', class_='info_box')
    if div_tags:
        div_tags.pop(0)

    # Ensure that the number of h3 tags and div tags are the same
    if len(h3_tags) != len(div_tags):
        raise ValueError("Mismatch between number of titles and content divs")

    for h3, div in zip(h3_tags, div_tags):
        title = h3.text.strip()
        content = div.get_text(strip=True)
        data_dict[title] = content
    return data_dict

def parse_table_content(table):
    data_dict = {}

    for row in table.find_all('tr'):
        # Safely get the th element with scope="row" attribute
        th_elem = row.find('th', attrs={"scope": "row"})
        td_elem = row.find('td')

        #Check if both elements exist before retrieving text
        if th_elem and td_elem:
            header = th_elem.get_text(strip=True)
            # Find span with class "pb10" within the td element
            span_elem = td_elem.find('span', class_='pb10')
            
            
            if span_elem:
                value = span_elem.get_text(strip=True)
            else:
                value = td_elem.get_text(strip=True)  # Default to the text of td if span not found
            data_dict[header] = value

    return data_dict

def get_additional_info(link):
    response = requests.get("https://nedrug.mfds.go.kr/" + link)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 정보
    table = soup.find('div', class_='r_sec').find('table', class_='s-dr_table dr_table_type1')
    parsed_data = parse_table_content(table)
    divs = soup.find_all('div', class_='info_box')
    

    # 각 div에서 정보 추출
    for div in divs:
        info_dict = extract_info_from_div(div)
        parsed_data.update(info_dict)
        
    # 사진
    table = soup.find('div', class_='pc-img')
    img_src = None
    if table:
        img_tag = table.find('img')
        if img_tag:
            img_src = img_tag['src']

    # print(img_src)
    if img_src:  # img_src가 None이 아닐 때만 처리
        image = data_url_to_image(img_src)
        file_name = generate_file_name()
        parsed_data["image"] = upload_to_s3(image, BUCKET_NAME, file_name)

    # for key, value in parsed_data.items():
    #         print(f"{key}: {value}")
            
    return parsed_data

# 기본 URL
base_url = "https://nedrug.mfds.go.kr/searchDrug"

# 파라미터
params = {
    'itemName': '타이레놀',
    'indutyClassCode': 'A0', # 품목구분(의약품)
}
# 요청 보내기
response = requests.get(base_url, params=params)
response.raise_for_status()  # 오류 발생 시 예외를 발생시킵니다.

# BeautifulSoup 객체 생성
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
# 여기에서 soup 객체를 사용하여 원하는 태그를 선택하고 데이터를 추출합니다.
# 예를 들어, 모든 제목에 해당하는 <h1> 태그의 텍스트를 가져오려면:
table = soup.find('table', class_='dr_table2 dr_table_type2')
tbody = table.find('tbody')

for tr in tbody.find_all('tr'):
    print("processing")
    data_dict = {}  # 각 행의 데이터를 저장할 딕셔너리
    
    for td in tr.find_all('td'):
        spans = td.find_all('span')
        for i in range(len(spans) - 1):
            # '주성분' 또는 '주성분영문명'을 key로 사용하는 span을 찾는다
            if spans[i].text.strip() in ['주성분', '주성분영문명']:
                key = spans[i].text.strip()
                value = spans[i+1].text.strip()
                data_dict[key] = value
                
                
        a_tag = td.find('a')
        if a_tag:  # a 태그가 존재하면
            href = a_tag.get('href')
            # href 링크에서 추가 정보를 가져옴
            additional_info = get_additional_info(href)
            data_dict.update(additional_info)  # data_dict에 추가 정보를 병합
            
    # print(f"data_dict: {data_dict}")
    
    filtered_data_info = {
        "name": data_dict.get("제품명", None),
        "image" : data_dict.get("image",None),
        "entpName" : data_dict.get("업체명", None),
        "itemSeq": data_dict.get("표준코드", None),
        "efcyQesitm": data_dict.get("이 약의 효능은 무엇입니까?", None),
        "useMethodQesitm": data_dict.get("이 약의 사용상 주의사항은 무엇입니까?", None),
        "atpnQesitm": data_dict.get("이 약을 사용하기 전에 반드시 알아야 할 내용은 무엇입니까?", None),
        "intrcQesitm": data_dict.get("이 약을 사용하는 동안 주의해야 할 약 또는 음식은 무엇입니까?", None),
        "depositMethodQesitm": data_dict.get("이 약은 어떻게 보관해야 합니까?",None),
        "seQesitm": data_dict.get("이 약은 어떤 이상반응이 나타날 수 있습니까?", None),
        "ingredient": data_dict.get("주성분", None),
        "eng_ingredient": data_dict.get("주성분영문명", None)
    }


    if filtered_data_info:
        for key, value in filtered_data_info.items():
                print(f"{key}: {value}")
        print("\n" + "-"*50 + "\n")  # 각 행 사이에 구분선 추가
    
    
 
    
    #!! 이 아래는 모델 저장 코드 !!#
    
    
    existing_medicine = Medicine.objects.filter(
        name=filtered_data_info['name'],
        entpName=filtered_data_info['entpName']
    ).first()
    
    if not existing_medicine:
        medicine = Medicine(
            name=filtered_data_info['name'],
            image = filtered_data_info['image'],
            entpName=filtered_data_info['entpName'],
            efcyQesitm=filtered_data_info['efcyQesitm'],
            useMethodQesitm = filtered_data_info['useMethodQesitm'],
            atpnQesitm = filtered_data_info['atpnQesitm'],
            intrcQesitm = filtered_data_info['intrcQesitm'],
            depositMethodQesitm = filtered_data_info['depositMethodQesitm'],
            seQesitm = filtered_data_info['seQesitm'],
            ingredient=filtered_data_info['ingredient'],
            eng_ingredient=filtered_data_info['eng_ingredient']
        )
    
        medicine.save()

        # itemSeq 리스트 처리
        item_seq_numbers = [int(num.strip()) for num in filtered_data_info['itemSeq'].split(',')]
        for num in item_seq_numbers:
            item_seq, created = ItemSeq.objects.get_or_create(number=num)  # 이미 있는 번호면 가져오고, 없으면 생성
            medicine.itemSeq.add(item_seq)
    else:
        # 이미 존재하는 Medicine 객체를 사용하거나
        # 다른 로직이 필요한 경우 처리
        medicine = existing_medicine
    

