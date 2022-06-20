"""
Created on Tue Apr 19 17:22:00 2022

@author: 54021
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams
import matplotlib.ticker as ticker


ssp126 = pd.read_excel(r'C:\Users\54021\Desktop\meeting\area\heat_area\heat_area_Mean_fre_GCMs_ssp126_90th.xlsx',header = [0],index_col= [0])
ssp370 = pd.read_excel(r'C:\Users\54021\Desktop\meeting\area\heat_area\heat_area_Mean_fre_GCMs_ssp370_90th.xlsx',header = [0],index_col= [0])
ssp585 = pd.read_excel(r'C:\Users\54021\Desktop\meeting\area\heat_area\heat_area_Mean_fre_GCMs_ssp585_90th.xlsx',header = [0],index_col= [0])

ssp126 = ssp126.T/10**5
ssp370 = ssp370.T/10**5
ssp585 = ssp585.T/10**5

ssp126_total = pd.read_excel(r'C:\Users\54021\Desktop\meeting\area\total_area\total_area_anthromessp126.xlsx',header = [0],index_col = [0])
ssp370_total = pd.read_excel(r'C:\Users\54021\Desktop\meeting\area\total_area\total_area_anthromessp370.xlsx',header = [0],index_col = [0])
ssp585_total = pd.read_excel(r'C:\Users\54021\Desktop\meeting\area\total_area\total_area_anthromessp585.xlsx',header = [0],index_col = [0])

ssp126_total = ssp126_total.T/10**5
ssp370_total = ssp370_total.T/10**5
ssp585_total = ssp585_total.T/10**5

ssp = [ssp126,ssp370,ssp585]
ssp_total = [ssp126_total, ssp370_total, ssp585_total]
SSP = ['ssp126','ssp370','ssp585']

plt.rcParams['mathtext.default'] = 'regular'
plt.style.use('seaborn')
fig,axs = plt.subplots(5,3, sharex = False, sharey = False,figsize=(15,20))
ws = 0.15
fig.subplots_adjust(wspace=ws)

for i in range(5):
    
    axs[i,1].set_title(ssp126.columns[i+15],fontweight = 'bold',loc = 'center')
    axs[i,0].set_ylabel('Area [10${^5}$ x km${^2}$]',fontweight = 'bold')
    for j in range(3):

        axs[i,j].bar(ssp_total[j].index, ssp_total[j][ssp_total[j].columns[i+10]] , width = 1,color = 'skyblue',alpha = 0.5)
        
        axs[i,j].plot(ssp[j].index,ssp[j][ssp[j].columns[i+10]],linewidth=0.5,color = 'black')
        axs[i,j].fill_between(y1 = 0,y2 =ssp[j][ssp[j].columns[i+10]],color = 'indianred',alpha = 0.8,x = ssp126.index)
        axs[i,j].set_title(SSP[j],fontweight = 'bold', loc = 'left',y = 0.92, fontsize = 10)

axs[4,1].set_xlabel('Year', fontweight = 'bold')
#fig.savefig(r'C:\Users\54021\Desktop\meeting\figure\biome_heat3',dpi = 500)

