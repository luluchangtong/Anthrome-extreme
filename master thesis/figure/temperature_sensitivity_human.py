# -*- coding: utf-8 -*-
"""
Created on Thu May  5 15:10:59 2022

@author: 54021
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams
import os
import re

All_files = os.listdir(r'D:\UUstudy\assignment\Master thesis\Dataprocess\human_analysis\population_%\GCMs_mean')
ssp =[]
SSP = ['ssp126','ssp370','ssp585']
T = ['25','26','28','30','33']

for i,j in zip(range(3),SSP):
    for x,y in zip(range(5),T):
        file_path = os.path.join(r'D:\UUstudy\assignment\Master thesis\Dataprocess\human_analysis\population_%\GCMs_mean', All_files[i*5+x])
        
        str1 = SSP[i] + '_' + T[x]
        locals()[str1] = pd.read_excel(file_path, header = [0], index_col = [0])
        locals()[str1] = locals()[str1].T/10**6
        ssp.append(locals()[str1])
        
plt.rcParams['mathtext.default'] = 'regular'
plt.style.use('seaborn')
fig,axs = plt.subplots(1,3, sharex = False, sharey = True, figsize = (15,5))
ws = 0.1
fig.subplots_adjust(wspace=ws)

for i in range(3):
    for j in range(5):
        axs[i].plot(ssp[i*5+j].index,ssp[i*5+j]['Pastoral villages'],linewidth=1.5)
    axs[i].legend(['25','26','28','30','33'], loc = 'upper left')
    axs[i].set_title(SSP[i], fontweight = 'bold', loc = 'right',y = 0.93)
    axs[i].set_xlabel('Year', fontweight = 'bold')

axs[0].set_title('Pastoral villages', fontweight = 'bold', loc = 'left', y = 1.0, fontsize = 14, x = -0.1)    
axs[0].set_ylabel('Population [Million - person]',fontweight = 'bold')





plt.savefig(r'C:\Users\54021\Desktop\meeting\figure\T_sen_Pastoral villages',dpi = 500)


        
        
        