# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 19:56:58 2022

@author: 54021
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams
import os
import re 

All_files = os.listdir(r'C:\Users\54021\OneDrive\桌面\桌面\meeting\exposure')
DATA = list(filter(lambda x: re.search('30',x) != None, All_files))

# check file name
print(DATA)

# get files abs path
files_path = [os.path.join(r'C:\Users\54021\OneDrive\桌面\桌面\meeting\exposure',x) for x in DATA]
files_path = sorted(files_path)

ssp126 = pd.read_excel(files_path[0],sheet_name= 'GCMS_mean',header = [0],index_col= [0])
ssp370 = pd.read_excel(files_path[1],sheet_name= 'GCMS_mean',header = [0],index_col= [0])
ssp585 = pd.read_excel(files_path[2],sheet_name= 'GCMS_mean',header = [0],index_col= [0])

ssp126 = ssp126.T
ssp370 = ssp370.T
ssp585 = ssp585.T

ssp126['Rained & irrigated villages'] = ssp126['Irrigated villages'] + ssp126['Rainfed villages']
ssp370['Rained & irrigated villages'] = ssp370['Irrigated villages'] + ssp370['Rainfed villages']
ssp585['Rained & irrigated villages'] = ssp585['Irrigated villages'] + ssp585['Rainfed villages']

ssp126 = ssp126.drop(columns=['Irrigated villages','Rainfed villages'])
ssp370 = ssp370.drop(columns=['Irrigated villages','Rainfed villages'])
ssp585 = ssp585.drop(columns=['Irrigated villages','Rainfed villages'])

ssp126 = ssp126.divide(10**9)
ssp370 = ssp370.divide(10**9)
ssp585 = ssp585.divide(10**9)

plt.rcParams['mathtext.default'] = 'regular'
plt.style.use('seaborn-ticks')
fig,axs = plt.subplots(1, 3, figsize = (13,4.8),sharex = False, sharey = True)
ws = 0.08
fig.subplots_adjust(wspace=ws)


axs[0].plot(ssp126, linewidth=1.2)
axs[0].set_title('ssp126', fontweight = 'bold', fontsize = 15)
axs[0].set_ylabel('Person-day year${^{-1}}$ [billions]',fontweight = 'bold', fontsize = 15)
axs[1].plot(ssp370,linewidth=1.2)
axs[1].set_title('ssp370',fontweight = 'bold',fontsize = 15)
axs[1].set_xlabel('Year',fontweight = 'bold')
axs[2].plot(ssp585,linewidth=1.2)
axs[2].set_title('ssp585',fontweight = 'bold',fontsize = 15)


fig.legend(ssp126.columns,loc = 8, ncol = 6, bbox_to_anchor=(0.5,-0.05 ))

plt.savefig(r'C:\Users\54021\OneDrive\桌面\桌面\meeting\figure\figures_new\population_exposure',dpi = 800, bbox_inches = 'tight')