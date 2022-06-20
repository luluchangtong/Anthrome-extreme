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
file_selected_to = list(filter(lambda x: re.search('total area', x) != None, file_path))
file_selected_heat = list(filter(lambda x: re.search('total heat area', x) != None, file_path))
files_to = []
files_heat = []

for i in range(10):
    files_to.append(pd.read_excel(file_selected_to[i],header = [0],index_col = [0]))
    
for i in range(10):
    files_heat.append(pd.read_excel(file_selected_heat[i],header = [0],index_col = [0]))
    
percentage_area = []
for i in range(10):
    percentage_area.append(files_heat[i]/files_to[i])
    
name = ['mai_ir','mai_rf','rice1_ir','rice1_rf','rice2_ir','rice2_rf','soybean_ir','soybean_rf','wheat_ir','wheat_rf']
legend = ['ssp126','ssp370','ssp585']
# make figures
plt.rcParams['mathtext.default'] = 'regular'
plt.style.use('seaborn-ticks')
fig,axs = plt.subplots(5, 2,sharex = False, sharey = 'row',figsize=(15,20))
fig.subplots_adjust(wspace=0.08)
x = ['Present','ssp126','ssp370','ssp585']

data = []
for i in range(5):
    for j in range(2):
        y = [percentage_area[i*2+j].iloc[0,0]*100,percentage_area[i*2+j].iloc[85,0]*100,percentage_area[i*2+j].iloc[85,1]*100,percentage_area[i*2+j].iloc[85,2]*100]
        axs[i,j].bar(x,[100,100,100,100],color = 'powderblue',alpha = 0.8, width = 0.5)
        axs[i,j].bar(x,y,color = 'tomato',alpha = 0.8,width = 0.5)
        axs[i,j].set_title(name[i*2+j], fontsize = 16, fontweight = 'bold')
        
        for a,b in zip(x,y):
            axs[i,j].text(a,b+0.05, str(round(b,1))+'%', va = 'bottom', fontsize = 10,horizontalalignment='center')

axs[2,0].set_ylabel('Percentage of area(%) influenced by extreme heat',fontsize = 20, fontweight = 'bold')
fig.savefig(r"C:\Users\54021\Desktop\桌面\meeting\figure\figures_new\croped\crop_heat_area",dpi = 800,bbox_inches='tight')