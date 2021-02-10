#!/usr/bin/env python
# coding: utf-8

# In[92]:


import os
os.getcwd()

folder_name = ''
abs_dir = os.path.join(os.getcwd(), folder_name)
file_names = os.listdir(abs_dir)
lyrics = []
for lyric in file_names:
    if lyric.endswith("txt"):
        lyrics.append(lyric)


# In[93]:


lyrics


# In[94]:


lyrics[1]

with open(lyrics[1],'r') as f:
    print(f.readlines())


# In[95]:


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

            
    return(file, noun_list)


# In[96]:


import csv
with open ("Artist_List.csv", "a") as f:
    w = csv.writer(f)
    w.writerow(["노래", "작곡가"])
for i in lyrics:
    
    with open ("Artist_List.csv", "a") as f:
        w = csv.writer(f)
        w.writerow(single_lyrics_separator(i))


# In[97]:


import pandas as pd
artists = {}
df = pd.read_csv("Artist_List.csv", encoding = "cp949")
for artists_per_song in df["작곡가"]:
#     print(artists_per_song)
    
    
    for artist in artists_per_song.strip('][').split(', '):
#         print(artist)
        if artist in artists.keys():
            artists[artist]+=1
        else:
            artists[artist]=1
# print(artists)
for keys in artists.keys():
    keys.strip('][').split(', ')
    
sorted(artists.items())


# In[98]:



with open("artist_count.csv",'w') as f:
    w = csv.writer(f)
    w.writerow(artists.keys())
    w.writerow(artists.values())
print(artists, " saved")


# In[ ]:





# In[ ]:




