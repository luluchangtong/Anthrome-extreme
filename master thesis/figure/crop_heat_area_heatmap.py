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
import numpy as np
import matplotlib as mpl


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
    
name = ['maize_ir','maize_rf','rice1_ir','rice1_rf','rice2_ir','rice2_rf','soybean_ir','soybean_rf','wheat_ir','wheat_rf']
legend = ['ssp126','ssp370','ssp585']
# make figures
#plt.rcParams['mathtext.default'] = 'regular'
#plt.style.use('seaborn-ticks')
#fig,axs = plt.subplots(5, 2,sharex = False, sharey = 'row',figsize=(15,20))
#fig.subplots_adjust(wspace=0.08)
x = ['Present','ssp126','ssp370','ssp585']

data = []
boundary = np.linspace(0,100,11)
for i in range(5):
    for j in range(2):
        y = [percentage_area[i*2+j].iloc[0,0]*100,percentage_area[i*2+j].iloc[85,0]*100,percentage_area[i*2+j].iloc[85,1]*100,percentage_area[i*2+j].iloc[85,2]*100]
        #axs[i,j].bar(x,[100,100,100,100],color = 'powderblue',alpha = 0.8, width = 0.5)
        #axs[i,j].bar(x,y,color = 'tomato',alpha = 0.8,width = 0.5)
        #axs[i,j].set_title(name[i*2+j], fontsize = 16, fontweight = 'bold')
        data.append(y)
        
data = pd.DataFrame(data,index=name,columns=x)
data = data.T
data = data.round(1)
color_select = sns.color_palette('Blues',10)
cmap = mpl.colors.ListedColormap(color_select)
norm = mpl.colors.BoundaryNorm(boundary, cmap.N)


ax = sns.heatmap(data, 
            linewidths = 0.05,
            vmin = 0,
            vmax = 100,
            cmap=cmap,
            square = True,
            cbar_kws = dict(use_gridspec=False,location="top",shrink = 1,ticks = boundary, pad = 0.02),
            annot = True
            )
        
ax.set_xticklabels(ax.get_xticklabels(), rotation=40,ha = 'right')
ax.set_title('Percentage of area(%) influenced by extreme heat',fontsize = 12, fontweight = 'bold',y = 1.3)
plt.savefig(r"C:\Users\54021\Desktop\桌面\meeting\figure\figures_new\croped\crop_area_per",dpi = 800,bbox_inches='tight')
