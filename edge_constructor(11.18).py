#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.getcwd()

folder_name = ''
abs_dir = os.path.join(os.getcwd(), folder_name)
file_names = os.listdir(abs_dir)
lyrics = []

for lyric in file_names:
    if lyric.endswith("txt"):
        lyrics.append(lyric)
        
import pandas as pd
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
from future.utils import iteritems
from collections import Counter
from sklearn.manifold import TSNE
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import csv
def single_lyrics_separator(file):
    from konlpy.tag import Twitter

    twitter = Twitter()
    with open(file, "r", encoding = "cp949") as f:
        contents = []        
        reader = csv.reader(f, delimiter = '\t')
        for row in f:
            row = row.replace("\n","")
            contents.append(row)
        tagged_lyrics = []
        for i in contents:
            tagged_lyric = twitter.pos(i)

            for pos in tagged_lyric:
                tagged_lyrics.append(pos)

    noun_list, verb_list, adj_list = [],[],[]
    for i in range(len(tagged_lyrics)):
        if tagged_lyrics[i][1]=='Noun':
            noun_list.append(tagged_lyrics[i][0])
        elif tagged_lyrics[i][1]=='Verb':
            verb_list.append(tagged_lyrics[i][0])
        elif tagged_lyrics[i][1]=='Adjective':
            adj_list.append(tagged_lyrics[i][0])
            
    return("noun:\n",noun_list, "verb:\n",verb_list, "adj:\n",adj_list)

def lyrics_separator(file):
    single = single_lyrics_separator(file)
    terms = {}
    for i in [1,3,5]:
        terms.update(Counter(single[i]))
    return terms
def send_tf_to_csv(file, file_name):
    with open("TF"+file_name+".csv",'w') as f:
        w = csv.writer(f)
        w.writerow(file.keys())
        w.writerow(file.values())
    print(file_name, " saved")
    
for i in lyrics:
    send_tf_to_csv(lyrics_separator(i),i)


# In[ ]:
import os
os.getcwd()

folder_name = ''
abs_dir = os.path.join(os.getcwd(), folder_name)

file_names = os.listdir(abs_dir)
lyrics = []

for lyric in file_names:
    if lyric.endswith("csv"):
        lyrics.append(lyric)
def lyrics_comparer(file1, file2):
    df1 = pd.read_csv(file1, encoding = 'cp949',engine="python")
    df2 = pd.read_csv(file2, encoding = 'cp949',engine="python")
    co_occur = {}
    for i in df1.columns:
        if i in df2.columns:
            co_occur[i] = int(df1[i])+int(df2[i])
    return co_occur
from itertools import combinations
import pandas as pd

def send_comparer_to_csv(file, file_name):
    with open("Co_occur"+file_name+".csv",'w') as f:
        w = csv.writer(f)
        w.writerow(file.keys())
        w.writerow(file.values())
    print(file_name, " saved")
import csv

for i,j in list(combinations(lyrics, 2)):
    try:
        x = lyrics_comparer(i,j)
        if len(x) != 0:
            send_comparer_to_csv(x,i+j)
    except:
        pass
# In[ ]:

import os
import pandas as pd
os.getcwd()

folder_name = ''
abs_dir = os.path.join(os.getcwd(), folder_name)
file_names = os.listdir(abs_dir)
lyrics = []

for lyric in file_names:
    if lyric.endswith("csv.csv"):
        lyrics.append(lyric)


def weight_cal(file):
    try:
        df = pd.read_csv(file, encoding = "cp949")
        numbers = []
        for i in df.iloc[0]:
            numbers.append(i)
        return sum(numbers)
    except:
        pass

pair = {}

for i in lyrics:
    temp = weight_cal(i)
    i= i.replace(".txt.csv","")
    pair[i[10:-4]]= temp

import csv
def send_edges_to_csv(file):
    with open("Edges"".csv",'w') as f:
        w = csv.writer(f)
        w.writerow(file.keys())
        w.writerow(file.values())
    print("saved")

send_edges_to_csv(pair)

df = pd.read_csv("Edges.csv", encoding = 'cp949')

row_1 = []
row_2 = []
for i in range(len(df.columns)):
    

    location = df.columns[i].find('TF')
    #first row
    row_1.append(df.columns[i][:location])
    #second row
    row_2.append(df.columns[i][location+2:])


with open("Edges"".csv",'a') as f:
    w = csv.writer(f)
    w.writerow(row_1)
    w.writerow(row_2)
print("saved")
    



