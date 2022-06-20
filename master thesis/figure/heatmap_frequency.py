# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 20:00:44 2022

@author: 54021
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
import os
import re 
from matplotlib.colors import LinearSegmentedColormap

# data file(90th)
All_files = os.listdir(r'D:/UUstudy/assignment/Master thesis/Dataprocess/analysis_biome/mean_fre_merge')
DATA = list(filter(lambda x: re.search('90th',x) != None, All_files))

# check file name
print(DATA)

# get files abs path
files_path = [os.path.join('D:/UUstudy/assignment/Master thesis/Dataprocess/analysis_biome/mean_fre_merge',x) for x in DATA]
files_path = sorted(files_path)

# load data
ssp126 = pd.read_excel(files_path[0],sheet_name= 'Mean',header = [0],index_col= [0])
ssp370 = pd.read_excel(files_path[1],sheet_name= 'Mean',header = [0],index_col= [0])
ssp585 = pd.read_excel(files_path[2],sheet_name= 'Mean',header = [0],index_col= [0])

ssp126 = ssp126.T
ssp370 = ssp370.T
ssp585 = ssp585.T

ssp126_av = ssp126.loc[list(range(2071,2101))]
ssp370_av = ssp370.loc[list(range(2071,2101))]
ssp585_av = ssp585.loc[list(range(2071,2101))]

ssp126_av.loc['mean'] = ssp126.apply(lambda x: x.mean())
ssp370_av.loc['mean'] = ssp370.apply(lambda x: x.mean())
ssp585_av.loc['mean'] = ssp585.apply(lambda x: x.mean())

new_data = pd.DataFrame([ssp126_av.iloc[30,0:20],ssp370_av.iloc[30,0:20],ssp585_av.iloc[30,0:20]],index = ['ssp126','ssp370','ssp585'])
new_data = new_data/36.6
new_data = new_data.T
new_data.index.name = None
boundaries = [1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0]

ax = sns.heatmap(new_data.T, 
            linewidths = 0.05,
            vmax=5, 
            vmin=1.5, 
            cmap='YlOrRd',
            square = True,
            cbar_kws = dict(use_gridspec=False,location="top",shrink = 1,ticks = boundaries, pad = 0.02),
            annot = False
            )


ax.set_xticklabels(ax.get_xticklabels(), rotation=40,ha = 'right')
ax.set_title('Extreme heat days(2071-2100) / extreme heat days(base period)', fontweight = 'bold', fontsize = 12, y = 1.7)
plt.savefig(r'C:\Users\54021\Desktop\meeting\Frequency_heatmap',dpi = 500, bbox_inches = 'tight')

plt.show()





 

