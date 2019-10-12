# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:12:49 2019

@author: Bruno
"""


#data analysis
import pandas as pd
import numpy as np
from nltk.collocations import *
import nltk
from nltk import FreqDist
import re



#Plotting
import cufflinks as cf
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)
import plotly.graph_objs as go
from wordcloud import WordCloud
import seaborn as sns
import matplotlib.pyplot as plt



##########################
#loading dataset
bd_complaints = "Consumer_Complaints.csv"
df = pd.read_csv(bd_complaints)

#Sample dataset
df2 = df.sample(100000)

#-------------------------------------------#



#-------------------------------------------#
####-----Creating date columns:-----#####


###Transforming dates into date object
df2['n_date_received'] = pd.to_datetime(df2['Date received'], 
                                 format='%m/%d/%Y', 
                                 errors='coerce')
df2['n_date_received'] = pd.to_datetime(df2['n_date_received'])



df2['n_data_sent_company'] = pd.to_datetime(df2['Date sent to company'], 
                                 format='%m/%d/%Y', 
                                 errors='coerce')
df2['n_data_sent_company'] = pd.to_datetime(df2['n_data_sent_company'])


###response delay????????

df2['response_delay'] =  df2['n_data_sent_company'] - df2['n_date_received']



##### New data frame #####

#creating a new data set without missing values in the consumer complaint narrative
df3 = df2.copy()
df3 = df3[df3['Consumer complaint narrative'].notnull()]

#### Creating ammount of money indicator column ####

#this expression identify money with this struture:
#$xxx.yy xxx.y
#xxx.yy xxx.y
#xxxk

pattern = "(\$[0-9]+\.?[0-9]{1,2}|[0-9]+k)"
df3['money1'] = df3['Consumer complaint narrative'].apply(lambda x: re.findall(pattern, str(x)))

#Transforming the list into a string, astype force the result as astring
df3['money2'] = df3['money1'].apply(lambda x: ' '.join(x)).astype(str)

#Transforming the symbol $ into "" , and k into "000"

df3['money3'] = df3['money2'].str.replace('k','000')
df3['money3'] = df3['money3'].str.replace('$','')

#Now transforming the string into a list to obtein the max:

df3['money4'] = df3['money3'].apply(lambda x: x.split())

#Transforming the elements into float format to correctly detect the max:
df3['money5'] = df3['money4'].apply(lambda x: list(map(float,x)) if len(x)>0 else None)

#Getting the max using a lambda function with a conditional statement
#bbecause if the list have none elements the function max
#will rise an error.
df3['money_max'] = df3['money5'].apply(lambda x: max(x) if x!=None else None)

#droping columns no longer needed:
df3.drop(['money1', 'money2' ,'money3','money4','money5'], inplace=True, axis=1)













