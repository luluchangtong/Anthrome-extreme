# -*- coding: utf-8 -*-
"""
Created on Sat May  7 14:34:57 2022

@author: -
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams
import os 

files = []
file_folder = r'C:\UUstudy\assignment\Master thesis\Dataprocess\analysis_biome\GCMs'
All_files = os.listdir(file_folder)
a = ['ssp126','ssp370','ssp585']
b = ['80th','90th','95th','99th']

list_name= []
for c in a:
    for d in b:
        x = c + '-' + d
        list_name.append(x)
        

for i in range(3):
    for j in range(4):
        str1 = a[i] + '_' + b[j]
        locals()[str1] = pd.read_excel(file_folder + '/' + All_files[i*4+j], header = [0], index_col=[0])
        locals()[str1] = locals()[str1].T
        locals()[str1] = locals()[str1].drop(['No lands'], axis = 1)
        files.append(locals()[str1])


mean_value = pd.DataFrame(data = None, columns = list(ssp126_80th), index = list_name)
for i in range(12):
    file1 = files[i]
    mean_value.iloc[i,0:20] = file1[56:86].mean(axis = 0)
    
mean_value = mean_value.T   


# select ssp take average 2017-2100 as my result

name = list(ssp126_80th)

plt.rcParams['mathtext.default'] = 'regular'
plt.style.use('seaborn-ticks')
fig,axs = plt.subplots(3,1, sharex = True, sharey = True, figsize = (15,15))
plt.xticks(rotation = 60)
ws = 0.1
fig.subplots_adjust(wspace=ws)

# fix xticks
n_label = np.arange(20)




index_x = np.arange(20)

for i in range(3):
    
        axs[i].bar(index_x,mean_value.iloc[:,i*4+0],color = 'skyblue',alpha = 0.8,label = '80th',align = 'center',width = 0.5)
        axs[i].bar(index_x,mean_value.iloc[:,i*4+1],color = 'limegreen',alpha = 0.8,label = '90th',align = 'center',width = 0.5)
        axs[i].bar(index_x,mean_value.iloc[:,i*4+2],color = 'gold',alpha = 0.8,label = '95th',align = 'center', width =0.5)
        axs[i].bar(index_x,mean_value.iloc[:,i*4+3],color = 'salmon',alpha = 0.8,label = '99th',align = 'center', width = 0.5)
        axs[i].set_xticks(n_label)
        axs[i].set_xticklabels(mean_value.index,rotation = 45, ha = 'right',fontsize = 14,fontweight='bold')
        axs[i].set_ylabel('Extreme heat days',fontweight = 'bold',fontsize = 15)
        axs[i].set_title(a[i],fontweight = 'bold', loc = 'left',y = 0.91,fontsize = 15)
#axs[2].set_xlabel('Anthrome',fontweight = 'bold',fontsize = 13)
axs[0].legend(['80th','90th','95th','99th'],loc = 'upper right',fontsize =15)
fig.tight_layout()

#plt.savefig(r'C:\Users\54021\OneDrive\桌面\桌面\meeting\figure\biome_sen', dpi = 500)
