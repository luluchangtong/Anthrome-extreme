# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 17:22:00 2022

@author: 54021
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams



ssp126 = pd.read_excel(r'C:\Users\54021\OneDrive\桌面\桌面\meeting\heat_total_area.xlsx',sheet_name= 'ssp126',header = [0],index_col= [0])
ssp370 = pd.read_excel(r'C:\Users\54021\OneDrive\桌面\桌面\meeting\heat_total_area.xlsx',sheet_name= 'ssp370',header = [0],index_col= [0])
ssp585 = pd.read_excel(r'C:\Users\54021\OneDrive\桌面\桌面\meeting\heat_total_area.xlsx',sheet_name= 'ssp585',header = [0],index_col= [0])

ssp126 = ssp126.T
ssp370 = ssp370.T
ssp585 = ssp585.T

plt.rcParams['mathtext.default'] = 'regular'
plt.style.use('seaborn-ticks')
fig,axs = plt.subplots(1, 3, figsize = (13,4.8),sharex = False, sharey = True)
ws = 0.08
fig.subplots_adjust(wspace=ws)


#axs[0].plot(ssp126.iloc[:,0:20], linewidth=1.2)
axs[0].set_title('ssp126', fontweight = 'bold', fontsize = 15)
axs[0].set_ylabel('Percentage(%) of area',fontweight = 'bold', fontsize = 14)
#axs[1].plot(ssp370.iloc[:,0:20],linewidth=1.2)
axs[1].set_title('ssp370',fontweight = 'bold',fontsize = 15)
axs[1].set_xlabel('Year',fontweight = 'bold')
#axs[2].plot(ssp585.iloc[:,0:20],linewidth=1.2)
axs[2].set_title('ssp585',fontweight = 'bold',fontsize = 15)
linestyle = ['solid','-.',':','--']
legend1 = [i for i in range(20)]

SSP = [ssp126,ssp370,ssp585]

for j in range(3):
    for i in range(2):
        legend1[i],= axs[j].plot(SSP[j].iloc[:,i]*100, linewidth=0.9,linestyle = linestyle[i],color = 'r')
        
    for i in range(2,6):
        legend1[i],= axs[j].plot(SSP[j].iloc[:,i]*100, linewidth=0.9,linestyle = linestyle[i-2],color = 'lightskyblue')
    
    for i in range(6,10):
        legend1[i],=axs[j].plot(SSP[j].iloc[:,i]*100, linewidth=0.9,linestyle = linestyle[i-6],color = 'orange')
        
    for i in range(10,13):
        legend1[i],=axs[j].plot(SSP[j].iloc[:,i]*100, linewidth=0.9,linestyle = linestyle[i-10],color = 'green')
        
    for i in range(13,17):
        legend1[i],=axs[j].plot(SSP[j].iloc[:,i]*100, linewidth=0.9,linestyle = linestyle[i-13],color = 'y')
        
    for i in range(17,19):
        legend1[i],=axs[j].plot(SSP[j].iloc[:,i]*100, linewidth=0.9,linestyle = linestyle[i-17],color = 'darkgrey')

fig.legend(handles = legend1[0:2], loc = 8, bbox_to_anchor=(0.12, -0.08),labels = ['Urban', 'Mixed settlements'])
fig.legend(handles = legend1[2:6], loc = 8, bbox_to_anchor=(0.24, -0.16),labels = ['Rice villages','Irrigated villages','Rainfed villages','Pastoral villages'])
fig.legend(handles = legend1[6:10], loc = 8, bbox_to_anchor=(0.39, -0.16),labels = ['Residential irrigated croplands','Residential rainfed croplands','Populated croplands','Remote croplands'])
fig.legend(handles = legend1[10:13], loc = 8, bbox_to_anchor=(0.55, -0.12),labels = ['Residential rangelands','Populated rangelands','Remote rangelands'])
fig.legend(handles = legend1[13:17], loc = 8, bbox_to_anchor=(0.72, -0.16),labels = ['Residential woodlands','Populated woodlands','Remote woodlands','Inhabited treeless & barren lands'])
fig.legend(handles = legend1[17:19], loc = 8, bbox_to_anchor=(0.85, -0.08),labels = ['Wild treeless & barren lands','Ice & uninhabited'])

plt.savefig(r'C:\Users\54021\OneDrive\桌面\桌面\meeting\figure\figures_new\heat_area_di_total',dpi = 800,bbox_inches = 'tight')
