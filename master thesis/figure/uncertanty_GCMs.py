# -*- coding: utf-8 -*-
"""
Created on Sun May  8 14:39:51 2022

@author: 54021
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams
import os
import re

a = r'C:\UUstudy\assignment\Master thesis\Dataprocess\analysis_biome\mean_fre'
all_files = os.listdir(a)


files_sel = list(filter(lambda x: re.search('90th',x) != None, all_files))
SSP = ['ssp126','ssp370','ssp585']
GCMs = ['GFDL-ESM4','IPSL-CM6A-LR','GCMs_mean','MPI-ESM1-2-HR','MRI-ESM2-0','UKESM1-0-LL']

file_con = []
for i in files_sel:
    b = pd.read_excel(os.path.join(a,i),header = [0], index_col=[0])
    b = b.drop(['No lands'])
    b = b.T
    file_con.append(b)
# 2071 - 2100 
ssp_mean = []   

index_ssp = []

for i in GCMs:
    for j in SSP:
        x = i+'_'+j
        index_ssp.append(x)

df = pd.DataFrame(data = None, index = index_ssp, columns = list(file_con[0]))

# calculate the mean frequency of 2017-2100, for 5 GCMS
for i in range(18):
    df.iloc[i,0:20] = file_con[i][56:86].mean(axis = 0)
    
plt.rcParams['mathtext.default'] = 'regular'
plt.style.use('seaborn-ticks')
fig,axs = plt.subplots(3,1, sharex = True, sharey = True, figsize = (15,15))
plt.xticks(rotation = 60)
ws = 0.1
fig.subplots_adjust(wspace=ws)

# set scatter shape
set_marker = ['o','v','_','2','s','+']
for i in range(3):
    axs[i].set_ylabel('Extreme heat days',fontweight = 'bold', fontsize = 15)
    axs[i].set_title(SSP[i],fontweight = 'bold', loc = 'left',y = 0.91,fontsize = 15)
    
    axs[i].scatter(list(df),df.iloc[0*3+i,:],marker = set_marker[0],s = 80,c = 'deepskyblue')
    axs[i].scatter(list(df),df.iloc[1*3+i,:],marker = set_marker[1],s = 80,c = 'gold')
    axs[i].scatter(list(df),df.iloc[2*3+i,:],marker = set_marker[2],s = 80,c = 'r',linewidth = 2)
    axs[i].scatter(list(df),df.iloc[3*3+i,:],marker = set_marker[3],s = 80,c = 'darkgoldenrod',linewidth = 2)
    axs[i].scatter(list(df),df.iloc[4*3+i,:],marker = set_marker[4],s = 80, facecolors='none',edgecolors = 'mediumpurple',linewidth = 1.5)
    axs[i].scatter(list(df),df.iloc[5*3+i,:],marker = set_marker[5],s = 80, c = 'darkorange')

axs[2].set_xticklabels(list(df),rotation = 45, ha = 'right',fontsize = 13)     
axs[0].legend(GCMs,loc = 'upper right',fontsize =13)


fig.tight_layout()

plt.savefig(r'C:\Users\54021\OneDrive\桌面\桌面\meeting\figure\figures_new\biome_uncertainty',dpi = 800)