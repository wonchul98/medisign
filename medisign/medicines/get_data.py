# Python3 샘플 코드 #


import requests

url = 'http://apis.data.go.kr/1471000/DrbEasyDrugInfoService/getDrbEasyDrugList'
params ={
            'serviceKey' : 'DdMNKkLcQd5B+HEnLuuQHrRwheuszU4v/tznl0Hg5qC0B8J0DTak4UtRLkxEtQpRPI6w6wvCOBuw2etPyspTjQ==', 
            'pageNo' : '1', 
            'numOfRows' : '3', 
            'entpName' : '', 
            'itemName' : '타이놀', 
            'itemSeq' : '', 
            'efcyQesitm' : '', 
            'useMethodQesitm' : '', 
            'atpnWarnQesitm' : '', 
            'atpnQesitm' : '', 
            'intrcQesitm' : '', 
            'seQesitm' : '', 
            'depositMethodQesitm' : '', 
            'openDe' : '', 
            'updateDe' : '', 
            'type' : 'xml'
        }

response = requests.get(url, params=params)
decoded_data = response.content.decode('utf-8')
print(decoded_data)