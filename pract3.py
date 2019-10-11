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




