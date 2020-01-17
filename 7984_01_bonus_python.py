#!/usr/bin/env python
# coding: utf-8

# In[64]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re
get_ipython().run_line_magic('matplotlib', 'inline')
df_2=pd.read_csv("imdb.csv",escapechar='\\')
df=pd.read_csv("movie_metadata.csv").dropna()


# In[57]:


#QN 5
def Qn5(df_2):
    df_2=df_2.dropna(subset=['duration'])
    df_2["decile"]=pd.qcut(df_2["duration"],10,labels=False)
    x=df_2.groupby("decile").agg({"nrOfNominations":'sum',"nrOfWins":'sum','year':'count'})
    y=df_2.iloc[:,np.r_[8,17:45]]#data
    z=(y.groupby("decile")[y.columns.tolist()[1:28]].sum()).transpose()
    e=pd.DataFrame(z.apply(lambda x: x.nlargest(3).index,axis=0).transpose())
    e.columns=["first","second","third"]
    x["top genres"]=e["first"]+","+e["second"]+","+e["third"]
    return(x)
Qn5(df_2)


# In[5]:


#Qn 4
def Qn4 (df):
    a=df.groupby("title_year")["imdb_score"].mean().reset_index()
    b=pd.DataFrame(df.groupby("title_year")["gross"].apply(lambda x: x.nlargest(3).index).reset_index())
    b=b["gross"].apply(lambda x:df.loc[x,"movie_title"]).fillna("")
    b["title"]=""
    for j in range(0,74):
        for i in range(0,180):
            if(len(b.iloc[j,i])>1):
                b.iloc[j,180]=b.iloc[j,180]+b.iloc[j,i]+","
            else:
                 b.iloc[j,180]=b.iloc[j,180]+b.iloc[j,i]

    b["title"]=b["title"].map(lambda x: str(x)[:-1])
    
    return(a.join(b).iloc[:,np.r_[0,1,182]])
Qn4(df)


# In[10]:


#qn 3
def Qn3(df_3):
    df_3['z']=df_3['z'].apply(pd.to_numeric,errors='coerce')
    df_3['volume']=df_3.apply(lambda df: df['x']*df['y']*df['z'] if df['depth']>60 else 8,axis=1)
    df_3["bin"]=pd.qcut(df_3["volume"],q=5,labels=['1','2','3','4','5'])
    return(pd.crosstab(df_3["bin"],df_3["cut"],normalize='columns')*100)
df_3=pd.read_csv("diamonds.csv")
Qn3(df_3)


# In[63]:


#Qn 2
# in length column 1 denotes <25 percentile 2 denotes 25 to 50 percentile 
# 3 denotes 50 to 75 percentile 4 denotes > 75 percentile
def Qn2(df_2):
    df_2.dropna()
    df_2['length']=df_2['title'].apply(lambda x:len(x.split("(")[0].rstrip()))
    df_2['quant']=pd.qcut(df_2['length'],4,labels=False)
    df1=pd.crosstab(df_2.year,df_2.quant,margins=False)
    df1['min']=df_2.groupby(["year"])['length'].min()
    df1['max']=df_2.groupby(["year"])['length'].max()
    return(df1)
Qn2(df_2)


# In[19]:


df_2['length'].corr(df_2['imdbRating'])


# In[13]:


#qn 1
def Qn1(df_2):
    df_2['GenreCombo']=df_2[df_2.columns[16:]].T.apply(lambda g: '|'.join(g.index[g==1]),axis=0)
    return(df_2.groupby(["type","year","GenreCombo"]).agg({"imdbRating":[min,max,np.mean],'duration':np.sum}))
Qn1(df_2)


# In[ ]:




