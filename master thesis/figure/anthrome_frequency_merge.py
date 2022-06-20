# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:27:45 2022

@author: 54021
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
from matplotlib import rcParams
import os
import re 

# data file(90th)
All_files = os.listdir(r"C:\UUstudy\assignment\Master thesis\Dataprocess\analysis_biome\mean_fre_merge")
DATA = list(filter(lambda x: re.search('90th',x) != None, All_files))

# check file name
print(DATA)

# get files abs path
files_path = [os.path.join(r"C:\UUstudy\assignment\Master thesis\Dataprocess\analysis_biome\mean_fre_merge",x) for x in DATA]
files_path = sorted(files_path)

# load data
ssp126 = pd.read_excel(files_path[0],sheet_name= 'Mean',header = [0],index_col= [0])
ssp370 = pd.read_excel(files_path[1],sheet_name= 'Mean',header = [0],index_col= [0])
ssp585 = pd.read_excel(files_path[2],sheet_name= 'Mean',header = [0],index_col= [0])

ssp126 = ssp126.T
ssp370 = ssp370.T
ssp585 = ssp585.T

SSP = [ssp126,ssp370,ssp585]

# make figures
plt.rcParams['mathtext.default'] = 'regular'
plt.style.use('seaborn-ticks')
fig,axs = plt.subplots(1, 3, figsize = (13,4.8),sharex = False, sharey = True)
ws = 0.08
fig.subplots_adjust(wspace=ws)

linestyle = ['solid','-.',':','--']
legend1 = [i for i in range(20)]
colors = ['#DD514C','#F37B1D','#FAD232','#5EB95E','#1F8DD6','#8058A5']
color = sns.color_palette(colors)




for j in range(3):
    for i in range(2):
        legend1[i],= axs[j].plot(SSP[j].iloc[:,i], linewidth=0.9,linestyle = linestyle[i],color = 'r')
        
    for i in range(2,6):
        legend1[i],= axs[j].plot(SSP[j].iloc[:,i], linewidth=0.9,linestyle = linestyle[i-2],color = 'lightskyblue')
    
    for i in range(6,10):
        legend1[i],=axs[j].plot(SSP[j].iloc[:,i], linewidth=0.9,linestyle = linestyle[i-6],color = 'orange')
        
    for i in range(10,13):
        legend1[i],=axs[j].plot(SSP[j].iloc[:,i], linewidth=0.9,linestyle = linestyle[i-10],color = 'green')
        
    for i in range(13,17):
        legend1[i],=axs[j].plot(SSP[j].iloc[:,i], linewidth=0.9,linestyle = linestyle[i-13],color = 'y')
        
    for i in range(17,19):
        legend1[i],=axs[j].plot(SSP[j].iloc[:,i], linewidth=0.9,linestyle = linestyle[i-17],color = 'darkgrey')
axs[0].set_title('ssp126', fontweight = 'bold', fontsize = 15)
axs[0].set_ylabel('Extreme heat days',fontweight = 'bold', fontsize = 15)


#axs[1].plot(ssp370.iloc[:,0:20],linewidth=1.2)
axs[1].set_title('ssp370',fontweight = 'bold',fontsize = 15)
axs[1].set_xlabel('Year',fontweight = 'bold')


# axs[2].plot(ssp585.iloc[:,0:20],linewidth=1.2)
axs[2].set_title('ssp585',fontweight = 'bold',fontsize = 15)

fig.legend(handles = legend1[0:2], loc = 8, bbox_to_anchor=(0.12, -0.08),labels = ['Urban', 'Mixed settlements'])
fig.legend(handles = legend1[2:6], loc = 8, bbox_to_anchor=(0.24, -0.16),labels = ['Rice villages','Irrigated villages','Rainfed villages','Pastoral villages'])
fig.legend(handles = legend1[6:10], loc = 8, bbox_to_anchor=(0.39, -0.16),labels = ['Residential irrigated croplands','Residential rainfed croplands','Populated croplands','Remote croplands'])
fig.legend(handles = legend1[10:13], loc = 8, bbox_to_anchor=(0.55, -0.12),labels = ['Residential rangelands','Populated rangelands','Remote rangelands'])
fig.legend(handles = legend1[13:17], loc = 8, bbox_to_anchor=(0.72, -0.16),labels = ['Residential woodlands','Populated woodlands','Remote woodlands','Inhabited treeless & barren lands'])
fig.legend(handles = legend1[17:19], loc = 8, bbox_to_anchor=(0.85, -0.08),labels = ['Wild treeless & barren lands','Ice & uninhabited'])

# fig.legend(ssp126.columns[0:3],loc = 8, ncol = 1, bbox_to_anchor=(0.13, -0.12))
# fig.legend(ssp126.columns[3:6],loc = 8, ncol = 1, bbox_to_anchor=(0.26, -0.12))
# fig.legend(ssp126.columns[6:10],loc = 8, ncol = 1, bbox_to_anchor=(0.42, -0.16))
# fig.legend(ssp126.columns[10:13],loc = 8, ncol = 1, bbox_to_anchor=(0.59, -0.12))
# fig.legend(ssp126.columns[13:17],loc = 8, ncol = 1, bbox_to_anchor=(0.76, -0.16))
# fig.legend(ssp126.columns[17:20],loc = 8, ncol = 1, bbox_to_anchor=(0.93, -0.12))

# fig.show()


plt.savefig(r'C:\Users\54021\OneDrive\桌面\桌面\meeting\figure\figures_new\fre_biome_new',dpi =800,bbox_inches = 'tight')


