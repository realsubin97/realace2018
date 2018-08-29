
# coding: utf-8

# In[1]:


import threading

import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[ ]:


## firebase와의 연동


# In[2]:


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('realace2018-firebase-adminsdk-r7gk1-121be5edaf.json')

# Initialize the app with a service account, granting admin privileges
app=firebase_admin.initialize_app(cred, {
   'databaseURL': 'https://realace2018.firebaseio.com/'
})

ref=db.reference()


# In[ ]:


## 


# In[3]:


serviceKey='F%2FxP1NfaTBhw0giVbsH7HTUMMnbJF6p9LhD9p8mJ4HpucMsVcxUzoTw4RxZDFdnRP3NgWj0IwJke%2FOzfe5VxhA%3D%3D'
numOfRows=[25, 16, 8, 9, 5, 5, 5, 31, 6, 7, 14, 12, 9, 1, 9, 9, 3]
sidoName=['서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '강원', '충북', '충남', '전북', '전남', '세종', '경북', '경남', '제주']


# In[ ]:


## firebase저장 함수


# In[9]:



def func():
    timer=threading.Timer(3600,func)
    
    for number in range(0,17):
        url='http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?serviceKey='+str(serviceKey)+'&numOfRows='+str(numOfRows[number])+'&pageSize=10&pageNo=1&startPage=1&sidoName='+str(sidoName[number])+'&searchCondition=DAILY'
        html=requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
    
        citylist=[]
        pm10list=[]
        timelist=[]

        datatime=soup.find_all('datatime')
        cityname=soup.find_all('cityname')
        pm10vale=soup.find_all('pm10value')

        for code in datatime:
            timelist.append(code.text)
        for code in cityname:
            citylist.append(code.text)
        for code in pm10vale:
            pm10list.append(code.text)
    
        numb=numOfRows[number]
    
        for num in range(0,numb):
            users_ref= ref.child('pm')
            users_ref.push({'sidoname':sidoName[number],'cityname':citylist[int(num)], 'pm10vale':pm10list[int(num)],'datatime':timelist[int(num)]})
    
    timer.start()

func()

