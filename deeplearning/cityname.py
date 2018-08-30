import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv

serviceKey='F%2FxP1NfaTBhw0giVbsH7HTUMMnbJF6p9LhD9p8mJ4HpucMsVcxUzoTw4RxZDFdnRP3NgWj0IwJke%2FOzfe5VxhA%3D%3D'
numOfRows=[25, 16, 8, 9, 5, 5, 5, 31, 6, 7, 14, 12, 9, 1, 9, 9, 3]
sidoName=['서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '강원', '충북', '충남', '전북', '전남', '세종', '경북', '경남', '제주']


def cityname():
    filename = 'cityname'+'.csv'
    file = open(filename,'w',encoding='utf-8',newline='')
    wr = csv.writer(file)
    
    for number in range(0,17):
        url='http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?serviceKey='+str(serviceKey)+'&numOfRows='+str(numOfRows[number])+'&pageSize=10&pageNo=1&startPage=1&sidoName='+str(sidoName[number])+'&searchCondition=DAILY'
        html=requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
    
        citylist=[]
        pm25list=[]
        timelist=[]

        datatime=soup.find_all('datatime')
        cityname=soup.find_all('cityname')
        pm25vale=soup.find_all('pm25value')
    
        for code in datatime:
            timelist.append(code.text)
        for code in cityname:
            wr.writerow({code.text})
            #print(code.text)
        for code in pm25vale:
            pm25list.append(code.text)
    
        numb=numOfRows[number]
   

    file.close()


cityname()
