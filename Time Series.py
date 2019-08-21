# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 08:32:35 2019

@author: Ardhi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timezone
import seaborn as sns
import vincent

data = pd.read_csv(r'C:\File Ardhi\Pelatihan\Digital Talent\DTS FGA 2019\Big Data\Project\Final Project\data_ibukota2.csv')

rt_max = np.max(data['retweet_count'])
like_max = np.max(data['favorite_count'])

tret = pd.Series(data=data['retweet_count'].values, index=data['created_at'])
tret.plot(figsize=(16,4), color='r')


#tweet = data.loc[:,['created_at']]
#tweet = data['created_at']-['2019-08-19 00:00:00']
#today = datetime.date.today()

# f is the file pointer to the JSON data set
 
# a list of "1" to count the hashtags
ones = [1]*len(data['created_at'])
# the index of the series
idx = pd.DatetimeIndex(data['created_at'])
# the actual series (at series of 1s for the moment)
tweet = pd.Series(ones, index=idx)
 
# Resampling / bucketing
per_minute = tweet.resample('1Min', how='sum').fillna(0)
print(per_minute)
#time_chart = vincent.Line(tweet)
#time_chart.axis_titles(x='Time', y='Freq')


#datetime.strptime(data["created_at"], '%a %b %d %H:%M:%S %z %Y').replace(tzinfo=timezone.utc).astimezone(pytz.timezone('US/Eastern')).strftime('%Y-%m-%d %H:%M:%S')
#for each in data['created_at']:
 #   each = each - today
    
#print(each)

##visualisasi time series 
fig = plt.figure(figsize=(16, 4))
ax = fig.add_subplot(111)
ax.set_title('Frekuensi Tweet')


per_minute.plot(ax=ax, color='Blue', label='Tweet')
ax.legend(loc='lower right')
ax.set_xlabel('Waktu')
ax.set_ylabel('Total Tweet')



#ax.set_title('Tweet Ibukota Timeseries')


#polarity_series_cro.plot(ax=ax, color='red', label='Croatia')
#polarity_series_fra.plot(ax=ax, color='Blue', label='France')
#ax.legend(loc='lower right')
#ax.set_xlabel('created_at')
#ax.set_ylabel('Sentiment')