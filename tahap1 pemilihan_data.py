# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 09:06:32 2019

@author: ilmy
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#proses Craling data dg export ke csv
data=pd.read_json('D:\\ibukota.json',lines=True)
follower=pd.DataFrame(data['user'].apply(pd.Series)['followers_count'])
username=pd.DataFrame(data['user'].apply(pd.Series)['screen_name'])
fav=pd.DataFrame(data['favorite_count'])
rt=pd.DataFrame(data['retweet_count'])
text=pd.DataFrame(data['text'])
time=pd.DataFrame(data['created_at'])
lokasi=pd.DataFrame(data['user'].apply(pd.Series)['location'])
data1=pd.DataFrame.join(username,text)
data2=pd.DataFrame.join(data1,follower)
data3=pd.DataFrame.join(data2,fav)
data4=pd.DataFrame.join(data3,rt)
data5=pd.DataFrame.join(data4,time)
data6=pd.DataFrame.join(data5,lokasi)
data6.to_csv('D:\\data_ibukota2.csv')

#
