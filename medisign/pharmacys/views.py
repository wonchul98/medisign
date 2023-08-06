from django.shortcuts import render

# Create your views here.
import requests
import xml.etree.ElementTree as ET
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

def parse_error(xml_data):
    root = ET.fromstring(xml_data)
    error_msg = root.find(".//errMsg").text if root.find(".//errMsg") is not None else None
    error_code = root.find(".//returnReasonCode").text if root.find(".//returnReasonCode") is not None else None
    
    return error_code, error_msg

def get_pharmacy_info(
    serviceKey = 'DdMNKkLcQd5B%2BHEnLuuQHrRwheuszU4v%2Ftznl0Hg5qC0B8J0DTak4UtRLkxEtQpRPI6w6wvCOBuw2etPyspTjQ%3D%3D',
    pageNo='1',
    numOfRows='10',
    sidoCd='110000',
    sgguCd='110019',
    emdongNm='신내동',
    yadmNm='온누리건강',
    xPos='127.0965441345503',
    yPos='37.60765568913871',
    radius='3000'
):
    # params를 인자에서 받은 값으로 설정
    params = {
        'serviceKey': serviceKey, 
        'pageNo': pageNo, 
        'numOfRows': numOfRows, 
        'sidoCd': sidoCd, 
        'sgguCd': sgguCd, 
        'emdongNm': emdongNm, 
        'yadmNm': yadmNm, 
        'xPos': xPos, 
        'yPos': yPos, 
        'radius': radius 
    }

    url = 'http://apis.data.go.kr/B551182/pharmacyInfoService/getParmacyBasisList'
    response = requests.get(url, params=params)
    if response.status_code != 200 or "<cmmMsgHeader>" in response.text:
        error_code, error_msg = parse_error(response.content)
        
        if error_code == "1":
            raise Exception("Application Error")
        elif error_code == "4":
            raise Exception("HTTP Error")
        elif error_code == "12":
            raise Exception("No OpenAPI Service or Service Deprecated")
        elif error_code == "20":
            raise Exception("Service Access Denied")
        elif error_code == "22":
            raise Exception("Exceeded Limit of Service Requests")
        elif error_code == "30":
            raise Exception("Service Key Not Registered")
        elif error_code == "31":
            raise Exception("Utilization Period Expired")
        elif error_code == "32":
            raise Exception("IP not Registered")
        elif error_code == "99":
            raise Exception("Unknown Error")
        else:
            raise Exception(f"Unhandled Error Code: {error_code}, Error Message: {error_msg}")
    xml_data = response.content  # 여기에 위에서 제공된 XML 데이터를 삽입합니다.
    root = ET.fromstring(xml_data)
    item = root.find(".//item")

    # ... (기존의 XML 파싱 코드)
    
    addr = item.find("addr").text
    clCdNm = item.find("clCdNm").text
    distance = item.find("distance").text
    emdongNm = item.find("emdongNm").text
    estbDd = item.find("estbDd").text
    postNo = item.find("postNo").text
    sgguCdNm = item.find("sgguCdNm").text
    sidoCdNm = item.find("sidoCdNm").text
    telno = item.find("telno").text
    XPos = item.find("XPos").text
    YPos = item.find("YPos").text
    yadmNm = item.find("yadmNm").text

    return {
        "addr": addr,
        "clCdNm": clCdNm,
        "distance" : distance,
        "emdongNm" : emdongNm,
        "estbDd" : estbDd,
        "postNo" : postNo,
        "sgguCdNm" : sgguCdNm,
        "sidoCdNm" : sidoCdNm,
        "telno" : telno,
        "XPos" : XPos,
        "YPos" : YPos,
        "yadmNm" : yadmNm,
    }
    

class PharmacyInfo(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        data = get_pharmacy_info()
        return Response(data)
    
def index(request):
    return render(request, 'users/nothing.html')