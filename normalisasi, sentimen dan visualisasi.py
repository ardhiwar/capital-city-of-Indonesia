# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:02:34 2019

@author: ilmy
"""

import pandas as pd
import matplotlib.pyplot as plt
import random
from textblob import TextBlob
from collections import Counter
from nltk.corpus import stopwords
import string
#import goslate

from collections import defaultdict
# remember to include the other import from the previous post
 
com = defaultdict(lambda : defaultdict(int))

data=pd.read_csv('D:\\data_ibukota.csv')

import re
 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

count_all = Counter()
tweet_positif=[]
tweet_negatif=[]
tweet_netral=[]
pos_count=0
neg_count=0
netral=0
word_count=0
baris_counter=0
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=True):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

def clean_tweet(tweet): 
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 

def sentimen(tweet): 
        # create TextBlob object of passed tweet text 
        analysis = TextBlob(clean_tweet(tweet)) 
        an=analysis.translate(from_lang='id',to='en')        
        print (an)
        #print (tweet)
        #print (an.sentiment)
        # set sentiment 
        if an.polarity >= 0.2: 
            return 'positif'
        elif an.polarity == 0.0:
            return 'netral'
        else: 
            return 'negatif'
        
pos_tweet=open('D:\\tugas\positif.txt').read()
positif=pos_tweet.split('\n')
neg_tweet=open(r'D:\\tugas\negatif.txt').read()
negatif=neg_tweet.split('\n')
data2=list(data['text'])
data_random=random.sample(data2,10)

for i in data_random:
   
    # Create a list with all the terms
    terms_all = [term for term in preprocess(i)]
    # Update the counter
    punctuation = list(string.punctuation)
    stop = stopwords.words('english') + punctuation + ['RT', 'via','…']
    terms_stop = [term for term in preprocess(i) if term not in stop]
    count_all.update(terms_stop)
    word_count=word_count+len(terms_stop)
    baris_counter=baris_counter+1
#    for words in terms_stop:  
#        if words in positif:
#            tweet_positif.append(words)
#            pos_count=pos_count+1
#            #print (words+'+')
#        elif words in negatif:
#            tweet_negatif.append(words)
#            neg_count=neg_count+1
#            #print (words+'-')
#        else :
#            tweet_netral.append(words)
#            netral=netral+1
#    #print ('\n')
    a=clean_tweet(str(terms_stop))
    b=sentimen(a)
    if b=='positif':
        pos_count=pos_count+1
    elif b=='negatif':
        neg_count=neg_count+1
    else :
        netral=netral+1
    #print (baris_counter)
    
positif_counter=(pos_count/baris_counter)*100
negatif_counter=(neg_count/baris_counter)*100
netral_counter=(netral/baris_counter)*100

labels = 'Negatif\n'+str(neg_count),'Positif\n'+str(pos_count),'Netral\n'+str(netral)
sizes = [negatif_counter,positif_counter,netral_counter]
colors = ['red', 'lightgreen', 'lightgray']
explode = (0.1, 0.1, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=150)

plt.axis('equal')
plt.show()

          
#    a=clean_tweet(txt)
#    print(str(sentimen(a)))
#    #b=str(sentimen(a))
#    with open('D:\\sentimen_data.txt', 'a',encoding="utf-8") as f:
#        f.writelines(b+'\n')
#
#with open('D:\\wordcount.txt', 'a',encoding="utf-8") as f:
#        f.writelines('\n'+str(count_all.most_common()))

