# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 15:49:23 2022

@author: 54021
"""
import os
import re 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def get_all_abs_path(source_dir):
    path_list = []
    for fpathe, dirs, fs in os.walk(source_dir):
        for f in fs:
            p = os.path.join(fpathe, f)
            path_list.append(p)
            
    return path_list

file_path = get_all_abs_path(r"C:\UUstudy\assignment\Master thesis\Dataprocess\crop_analysis")
file_selected = list(filter(lambda x: re.search('mean frequency', x) != None, file_path))

files = []

for i in range(10):
    files.append(pd.read_excel(file_selected[i],header = [0],index_col = [0]))
    
name = ['mai_ir','mai_rf','rice1_ir','rice1_rf','rice2_ir','rice2_rf','soybean_ir','soybean_rf','wheat_ir','wheat_rf']
legend = ['ssp126','ssp370','ssp585']
# make figures
plt.rcParams['mathtext.default'] = 'regular'
plt.style.use('seaborn-ticks')
x = ['Present','ssp126','ssp370','ssp585']
fig,axs = plt.subplots(5, 2,sharex = False, sharey = 'row',figsize=(15,20))
fig.subplots_adjust(wspace=0.08)
for i in range(5):
    for j in range(2):
        y = [files[i*2+j].iloc[0,0],files[i*2+j].iloc[85,0],files[i*2+j].iloc[85,1],files[i*2+j].iloc[85,2]]
        axs[i,j].bar(x, y, color = ['deepskyblue','seagreen','darkorange','r'], alpha = 0.8,width = 0.5)
        axs[i,j].set_title(name[i*2+j], fontsize = 16, fontweight = 'bold')
        for a,b in zip(x,y):
            axs[i,j].text(a,b+0.05, str(round(b,1)), va = 'bottom', fontsize = 11,horizontalalignment='center')

axs[2,0].set_ylabel('Frequency of extreme heat(days/year)',fontsize = 20, fontweight = 'bold')
axs[4,1].set_xlabel('Years',fontsize = 18, fontweight = 'bold')
axs[4,0].set_xlabel('Years',fontsize = 18, fontweight = 'bold')   


fig.savefig(r"C:\Users\54021\Desktop\桌面\meeting\figure\figures_new\croped\crop_mean_fre",dpi = 800,bbox_inches='tight')
