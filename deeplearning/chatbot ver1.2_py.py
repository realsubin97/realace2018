from pymongo import MongoClient
from datetime import datetime

import threading

conn = MongoClient('127.0.0.1')
db = conn.test1
collec = db.collect

def chatbot():
    sidoName=['서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주', '세종']
    print("언니를 부르셨나요?")
    print("종료를 원하시면 exit를 입력해주세요! \n")
    while True:
        sidoCount = 0; # sidoName안에서 값을 찾았을 경우/ 찾지 못했을 경우를 판별
        cityCount = 0 ; # cityName안에서 값을 찾았을 경우/ 찾지 못했을 경우를 판별 
        print("어느 지역의 미세먼지가 알고 싶으세요?")        
        answer=input("")
        
        now = datetime.now()
        nowDate = now.strftime('%Y-%m-%d %H')
        nowDate= nowDate+":00"
        
        if(answer.find("exit") != -1):
            break
        
        for sidolist in sidoName:
            if answer.find(sidolist) != -1:
                sidoCount = 1 # sidoNAme을 찾았을 경우 
                data=list(collec.find({"datatime":nowDate,"sidoname":sidolist},{"_id":False,"sidoname":False,"datatime":False,"pm25vale":False}))
                #print(data)
                for city in data:
                    if answer.find(city['cityname']) != -1:
                        cityCount = 1;
                        #print(city['cityname'])
                        pm25list=list(collec.find({"datatime":nowDate,"sidoname":sidolist,"cityname":city['cityname']},{"_id":False,"sidoname":False,"datatime":False}))
                        pm25dict=dict(pm25list[0])
                        print(city['cityname']+'의 현재 미세먼지는 '+pm25dict['pm25vale']+'입니다.\n\n\n')
                        break
                break
        if(sidoCount == 0 or cityCount ==0):
            print("지역명을 다시 확인해 주세요 ㅠㅠ \n\n\n")


while True:
    hiFirst=['언니']
    hi=input("");
    if hi.find('언니') != -1 :
        chatbot()
