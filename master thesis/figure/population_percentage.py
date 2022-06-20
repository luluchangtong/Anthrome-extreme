# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 14:24:50 2022

@author: 54021
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams
import os
import re

All_files = os.listdir(r'C:\UUstudy\assignment\Master thesis\Dataprocess\human_analysis\total_population\GCMs_mean')
DATA = list(filter(lambda x: re.search('30',x) != None, All_files))

files_path = [os.path.join(r'C:\UUstudy\assignment\Master thesis\Dataprocess\human_analysis\total_population\GCMs_mean',x) for x in DATA]
files_path = sorted(files_path)

print(files_path)

# load total population data
pop_tol_ssp126_30 = pd.read_excel(files_path[0],header = [0],index_col = [0])
pop_tol_ssp370_30 = pd.read_excel(files_path[1],header = [0],index_col = [0])
pop_tol_ssp585_30 = pd.read_excel(files_path[2],header = [0],index_col = [0])

pop_tol_ssp126_30 = pop_tol_ssp126_30.T/10**6
pop_tol_ssp370_30 = pop_tol_ssp370_30.T/10**6
pop_tol_ssp585_30 = pop_tol_ssp585_30.T/10**6

# load population percentage 
All_files2 = os.listdir(r'C:\UUstudy\assignment\Master thesis\Dataprocess\human_analysis\population_%\GCMs_mean')
DATA2 = list(filter(lambda x: re.search('30',x) != None, All_files2))
files_path2 = [os.path.join(r'C:\UUstudy\assignment\Master thesis\Dataprocess\human_analysis\population_%\GCMs_mean',x) for x in DATA2]
files_path2 = sorted(files_path2)

print(files_path2)
pop_ssp126_30 = pd.read_excel(files_path2[0],header = [0],index_col = [0])
pop_ssp370_30 = pd.read_excel(files_path2[1],header = [0],index_col = [0])
pop_ssp585_30 = pd.read_excel(files_path2[2],header = [0],index_col = [0])

pop_ssp126_30 = pop_ssp126_30.T/10**6
pop_ssp370_30 = pop_ssp370_30.T/10**6
pop_ssp585_30 = pop_ssp585_30.T/10**6

# laod population > 10 days
All_files3 = os.listdir(r'C:\UUstudy\assignment\Master thesis\Dataprocess\human_analysis\population_%_10d\GCMs_mean')
DATA3 = list(filter(lambda x: re.search('30',x) != None, All_files3))
files_path3 = [os.path.join(r'C:\UUstudy\assignment\Master thesis\Dataprocess\human_analysis\population_%_10d\GCMs_mean',x) for x in DATA3]
files_path3 = sorted(files_path3)

pop_10_ssp126_30 = pd.read_excel(files_path3[0],header = [0],index_col = [0])
pop_10_ssp370_30 = pd.read_excel(files_path3[1],header = [0],index_col = [0])
pop_10_ssp585_30 = pd.read_excel(files_path3[2],header = [0],index_col = [0])

pop_10_ssp126_30 = pop_10_ssp126_30.T/10**6
pop_10_ssp370_30 = pop_10_ssp370_30.T/10**6
pop_10_ssp585_30 = pop_10_ssp585_30.T/10**6

plt.rcParams['mathtext.default'] = 'regular'
plt.style.use('seaborn-ticks')
fig,axs = plt.subplots(1,4, sharex = False, sharey = True, figsize = (18,4.8))
ws = 0.1
fig.subplots_adjust(wspace=ws)

axs[0].set_title('Pastoral villages',fontweight = 'bold', loc = 'center',y = 1.02, x = 0.09,fontsize = 15)
#sub figure 1
a, = axs[0].plot(pop_tol_ssp126_30.index,pop_tol_ssp126_30['Pastoral villages'],linewidth=0.5,color = 'skyblue')
axs[0].fill_between(y1 = 0,y2 = pop_tol_ssp126_30['Pastoral villages'],color = 'skyblue',alpha = 0.8,x = pop_tol_ssp126_30.index)

b, = axs[0].plot(pop_ssp126_30.index,pop_ssp126_30['Pastoral villages'],linewidth=0.5, color = 'gold')
axs[0].fill_between(y1 = 0,y2 = pop_ssp126_30['Pastoral villages'],color = 'gold',alpha = 0.8,x = pop_tol_ssp126_30.index)

c, = axs[0].plot(pop_10_ssp126_30.index,pop_10_ssp126_30['Pastoral villages'], linewidth=0.5, color = 'salmon')
axs[0].fill_between(y1 = 0,y2 = pop_10_ssp126_30['Pastoral villages'],color = 'salmon',alpha = 0.8,x = pop_tol_ssp126_30.index)

axs[0].set_ylabel('Population [Million - person]',fontweight = 'bold')

axs[0].set_title('ssp126',fontweight = 'bold', loc = 'left',y = 0.92, fontsize = 10)


# subfigure 2
axs[1].plot(pop_tol_ssp370_30.index,pop_tol_ssp370_30['Pastoral villages'],linewidth=0.5,color = 'skyblue')
axs[1].fill_between(y1 = 0,y2 = pop_tol_ssp370_30['Pastoral villages'],color = 'skyblue',alpha = 0.8,x = pop_tol_ssp126_30.index)

axs[1].plot(pop_ssp370_30.index,pop_ssp370_30['Pastoral villages'],linewidth=0.5, color = 'gold')
axs[1].fill_between(y1 = 0,y2 = pop_ssp370_30['Pastoral villages'],color = 'gold',alpha = 0.8,x = pop_tol_ssp126_30.index)

axs[1].plot(pop_10_ssp585_30.index,pop_10_ssp370_30['Pastoral villages'],linewidth=0.5, color = 'salmon')
axs[1].fill_between(y1 = 0,y2 = pop_10_ssp370_30['Pastoral villages'],color = 'salmon',alpha = 0.8,x = pop_tol_ssp126_30.index)

axs[1].set_title('ssp370',fontweight = 'bold', loc = 'left',y = 0.92, fontsize = 10)

# sub figure 3
axs[2].plot(pop_tol_ssp585_30.index,pop_tol_ssp585_30['Pastoral villages'],linewidth=0.5,color = 'skyblue')
axs[2].fill_between(y1 = 0,y2 = pop_tol_ssp585_30['Pastoral villages'],color = 'skyblue',alpha = 0.8,x = pop_tol_ssp126_30.index)

axs[2].plot(pop_ssp585_30.index,pop_ssp585_30['Pastoral villages'],linewidth=0.5, color = 'gold')
axs[2].fill_between(y1 = 0,y2 = pop_ssp585_30['Pastoral villages'],color = 'gold',alpha = 0.8,x = pop_tol_ssp126_30.index)

axs[2].plot(pop_10_ssp126_30.index,pop_10_ssp585_30['Pastoral villages'],linewidth=0.5, color = 'salmon' )
axs[2].fill_between(y1 = 0,y2 = pop_10_ssp585_30['Pastoral villages'],color = 'salmon',alpha = 0.8,x = pop_tol_ssp126_30.index)

axs[2].set_title('ssp585',fontweight = 'bold', loc = 'left',y = 0.92, fontsize = 10)

# legend


#axs[0].legend([a,b,c], ['Tol_pop','1d_pop','10d_pop'], loc = 'upper right')
#axs[1].legend([a,b,c], ['Tol_pop','1d_pop','10d_pop'], loc = 'upper right')
#axs[2].legend([a,b,c], ['Tol_pop','1d_pop','10d_pop'], loc = 'upper right')
#fig.legend([a,b,c],['Tol_pop','1d_pop','10d_pop'],loc =8,ncol=3, bbox_to_anchor=(0.40, -0.04))

# column chart
x = ['Present','ssp126','ssp370','ssp585']

y2 = [np.mean([pop_ssp126_30.loc[2015,'Pastoral villages'],pop_ssp370_30.loc[2015,'Pastoral villages'],pop_ssp585_30.loc[2015,'Pastoral villages']]),pop_ssp126_30.loc[2100,'Pastoral villages'],pop_ssp370_30.loc[2100,'Pastoral villages'],pop_ssp585_30.loc[2100,'Pastoral villages']]
y1 = [np.mean([pop_tol_ssp126_30.loc[2015,'Pastoral villages'],pop_tol_ssp370_30.loc[2015,'Pastoral villages'],pop_tol_ssp585_30.loc[2015,'Pastoral villages']]), pop_tol_ssp126_30.loc[2100,'Pastoral villages'], pop_tol_ssp370_30.loc[2100,'Pastoral villages'], pop_tol_ssp585_30.loc[2100,'Pastoral villages']]
y3 = [np.mean([pop_10_ssp126_30.loc[2015,'Pastoral villages'], pop_10_ssp370_30.loc[2015,'Pastoral villages'],pop_10_ssp585_30.loc[2015,'Pastoral villages']]),pop_10_ssp126_30.loc[2100,'Pastoral villages'],pop_10_ssp370_30.loc[2100,'Pastoral villages'],pop_10_ssp585_30.loc[2100,'Pastoral villages']]

axs[3].bar(x ,y1, color = 'skyblue',alpha = 0.8, label = 'Tol_pop')
axs[3].bar(x ,y2, color = 'gold',alpha = 0.8, label = '1d_pop')
axs[3].bar(x ,y3, color = 'salmon',alpha = 0.8, label = '10d_pop')
axs[3].legend(loc = 'upper left')

for i in range(3):
    axs[i].set_xlabel('Year', fontweight = 'bold')
    
for a,b,c in zip(x,y2,y1):
    axs[3].text(a,b+0.05, str(round(b/c*100,1))+'%', va = 'bottom', fontsize = 7,horizontalalignment='left')
    
for a,b,c in zip(x,y3,y1):
    axs[3].text(a,b+0.05, str(round(b/c*100,1))+'%', va = 'top', fontsize = 7,horizontalalignment='left')
    
plt.savefig(r'C:\Users\54021\OneDrive\桌面\桌面\meeting\figure\figures_new\population_Pastoral villages',bbox_inches = 'tight',dpi = 800)