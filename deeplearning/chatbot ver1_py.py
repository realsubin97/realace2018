from pymongo import MongoClient
from datetime import datetime

import threading

conn = MongoClient('127.0.0.1')
db = conn.test1
collec = db.collect

def chatbot():
    sidoName=['����', '�λ�', '�뱸', '��õ', '����', '����', '���', '���', '����', '���', '�泲', '����', '����', '���', '�泲', '����', '����']
    while True:
        print("��� ������ �̼������� �˰� ��������? ���� exit")        
        answer=input("")
        now = datetime.now()
        nowDate = now.strftime('%Y-%m-%d %H')
        nowDate= nowDate+":00"
        if(answer.find("exit") != -1):
            break
        for sidolist in sidoName:
            if answer.find(sidolist) != -1:
                data=list(collec.find({"datatime":nowDate,"sidoname":sidolist},{"_id":False,"sidoname":False,"datatime":False,"pm25vale":False}))
                #print(data)
                for city in data:
                    if answer.find(city['cityname']) != -1:
                        #print(city['cityname'])
                        pm25list=list(collec.find({"datatime":nowDate,"sidoname":sidolist,"cityname":city['cityname']},{"_id":False,"sidoname":False,"datatime":False}))
                        pm25dict=dict(pm25list[0])
                        print(city['cityname']+'�� ���� �̼������� '+pm25dict['pm25vale']+'�Դϴ�.\n\n\n')
                        break
                break