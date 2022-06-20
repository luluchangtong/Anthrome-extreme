# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 14:07:17 2022

@author: 54021
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
from matplotlib import rcParams
import os
import re 

# data file(90th)
All_files = os.listdir(r'D:/UUstudy/assignment/Master thesis/Dataprocess/analysis_biome/mean_fre_merge')
DATA = list(filter(lambda x: re.search('90th',x) != None, All_files))

# check file name
print(DATA)

# get files abs path
files_path = [os.path.join('D:/UUstudy/assignment/Master thesis/Dataprocess/analysis_biome/mean_fre_merge',x) for x in DATA]
files_path = sorted(files_path)

# load data
ssp126 = pd.read_excel(files_path[0],sheet_name= 'Mean',header = [0],index_col= [0])
ssp370 = pd.read_excel(files_path[1],sheet_name= 'Mean',header = [0],index_col= [0])
ssp585 = pd.read_excel(files_path[2],sheet_name= 'Mean',header = [0],index_col= [0])

ssp126 = ssp126.T
ssp370 = ssp370.T
ssp585 = ssp585.T

# make figures
plt.rcParams['mathtext.default'] = 'regular'
plt.style.use('seaborn')
fig, axs = plt.subplots(7, 3, figsize = (16, 35), sharex = False, sharey = True)
ws = 0.15
fig.subplots_adjust(wspace=ws)

# Urban 


for i in range(0,7):
    for j in range(0,3):
        ax = axs[i,j]
        ax.set_title(ssp126.columns[3*i+j],fontweight='bold')
        ax.plot(ssp126[ssp126.columns[3*i+j]], color = 'forestgreen',linewidth = 2.0)
        ax.plot(ssp370[ssp370.columns[3*i+j]], color = 'deepskyblue',linewidth = 2.0)
        ax.plot(ssp585[ssp585.columns[3*i+j]], color = 'r',linewidth = 2.0)
        ax.legend(['ssp126','ssp370','ssp585'], loc = 'upper left')

for i in range(0,7):
    ax = axs[i,1]
    ax.set(xlabel = 'Year')
    
for i in range(0,7):
    ax = axs[i,0]
    ax.set(ylabel = 'Extreme heat days in per year')
    
    



