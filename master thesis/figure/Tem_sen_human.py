# -*- coding: utf-8 -*-
"""
Created on Fri May  6 03:28:45 2022

@author: 54021
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

df = pd.read_excel(r'C:\UUstudy\assignment\Master thesis\Dataprocess\human_analysis\population_%\temperature_sentivity\temperature_sen.xlsx', sheet_name = 'try',index_col = [0])
a = ['ssp126','ssp370','ssp585']
ssp126 = df.iloc[23:30,:]
ssp370 = df.iloc[31:38,:]
ssp585 = df.iloc[39:46,:]

ssp126 = ssp126.T
ssp370 = ssp370.T
ssp585 = ssp585.T

SSP = [ssp126,ssp370,ssp585]

plt.rcParams['mathtext.default'] = 'regular'
plt.style.use('seaborn-ticks')
fig,axs = plt.subplots(1,3, sharex = False, sharey = True,figsize=(15,5))

ws = 0.1


fig.subplots_adjust(wspace=ws)

for i in range(3):
    for j in range(1,7):
        axs[i].plot(SSP[i].index,SSP[i].iloc[:,j],linewidth=1.5)
    
    axs[i].set_title(a[i], fontweight = 'bold', loc = 'left',y = 0.93,x = 0.02)
    axs[i].set_xlabel('Year', fontweight = 'bold')
axs[0].legend(list(ssp126)[1:],loc = 'center right')  
axs[0].set_ylabel('Population increase(%) per unit temperature',fontweight = 'bold')

plt.savefig(r'C:\Users\54021\OneDrive\桌面\桌面\meeting\figure\T_sentivity',dpi = 500)