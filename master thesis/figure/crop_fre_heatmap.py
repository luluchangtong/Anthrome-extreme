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
import matplotlib as mpl
import numpy as np


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
    
name = ['maize_ir','maize_rf','rice1_ir','rice1_rf','rice2_ir','rice2_rf','soybean_ir','soybean_rf','wheat_ir','wheat_rf']
legend = ['ssp126','ssp370','ssp585']
# make figures
plt.rcParams['mathtext.default'] = 'regular'
plt.style.use('seaborn-ticks')
x = ['Present','ssp126','ssp370','ssp585']

data = []
boundary = np.linspace(0,40,11)

for i in range(5):
    for j in range(2):
        y = [files[i*2+j].iloc[0,0],files[i*2+j].iloc[85,0],files[i*2+j].iloc[85,1],files[i*2+j].iloc[85,2]]
        data.append(y)
        
data = pd.DataFrame(data,index=name,columns=x)
data = data.T
data = data.round(2)
color_select = sns.color_palette('YlOrBr',10)
cmap = mpl.colors.ListedColormap(color_select)
norm = mpl.colors.BoundaryNorm(boundary, cmap.N)

ax = sns.heatmap(data, 
            linewidths = 0.05,
            vmin = 0,
            vmax = 40,
            cmap=cmap,
            square = True,
            cbar_kws = dict(use_gridspec=False,location="top",shrink = 1,ticks = boundary, pad = 0.02),
            annot = True
            )

ax.set_title('Frequency of extreme heat(days/year)',fontsize = 12, fontweight = 'bold', y=1.3)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40,ha = 'right')


plt.savefig(r"C:\Users\54021\Desktop\桌面\meeting\figure\figures_new\croped\crop_mean_fre",dpi = 800,bbox_inches='tight')

