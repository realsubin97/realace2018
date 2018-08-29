
# coding: utf-8

# In[4]:


import os
import folium
import json
print(folium.__version__)
import threading
import requests
from pandas import Series, DataFrame
import pandas as pd
from datetime import datetime


# In[5]:


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


# In[6]:


def func():
    timer=threading.Timer(3600,func)
    
    df=pd.DataFrame()
    snapshot = ref.child('pm').get()
    for key, val in snapshot.items():
        df=df.append(pd.DataFrame([val]))
    
    now = datetime.now()
    nowDate = now.strftime('%Y-%m-%d %H:00')
    df=df[df['datatime'] == nowDate]
    df['pm10vale']=pd.to_numeric(df['pm10vale'], errors='coerce')
    
    map_osm = folium.Map(location=[37.566345, 126.977893])
    rfile = open('json/skorea_municipalities_geo_simple.json', 'r', encoding='utf-8').read()
    jsonData = json.loads(rfile)

    map_osm.choropleth(
        geo_data=jsonData,
        data=df,
        columns=['cityname', 'pm10vale'],
        key_on='feature.properties.name',
        fill_color='YlGn'
    )
    map_osm.save('results.html')
    
    timer.start()

func()

