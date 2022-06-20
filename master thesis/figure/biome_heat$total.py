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


ssp126 = pd.read_excel(r"C:\UUstudy\assignment\Master thesis\Dataprocess\analysis_biome\Affected_area\heat_area_Mean_fre_GCMs_ssp126_90th.xlsx",header = [0],index_col= [0])
ssp370 = pd.read_excel(r"C:\UUstudy\assignment\Master thesis\Dataprocess\analysis_biome\Affected_area\heat_area_Mean_fre_GCMs_ssp370_90th.xlsx",header = [0],index_col= [0])
ssp585 = pd.read_excel(r"C:\UUstudy\assignment\Master thesis\Dataprocess\analysis_biome\Affected_area\heat_area_Mean_fre_GCMs_ssp585_90th.xlsx",header = [0],index_col= [0])

ssp126 = ssp126.T/10**5
ssp370 = ssp370.T/10**5
ssp585 = ssp585.T/10**5

ssp126_total = pd.read_excel(r"C:\UUstudy\assignment\Master thesis\Dataprocess\analysis_biome\total_anthrome_area\total_area_anthromessp126.xlsx",header = [0],index_col = [0])
ssp370_total = pd.read_excel(r"C:\UUstudy\assignment\Master thesis\Dataprocess\analysis_biome\total_anthrome_area\total_area_anthromessp370.xlsx",header = [0],index_col = [0])
ssp585_total = pd.read_excel(r"C:\UUstudy\assignment\Master thesis\Dataprocess\analysis_biome\total_anthrome_area\total_area_anthromessp585.xlsx",header = [0],index_col = [0])

ssp126_total = ssp126_total.T/10**5
ssp370_total = ssp370_total.T/10**5
ssp585_total = ssp585_total.T/10**5

ssp126 = ssp126.drop(['No lands'],axis =1)
ssp370 = ssp370.drop(['No lands'],axis =1)
ssp585 = ssp585.drop(['No lands'],axis =1)
ssp126_total = ssp126_total.drop(['No lands'],axis =1)
ssp370_total = ssp370_total.drop(['No lands'],axis =1)
ssp585_total = ssp585_total.drop(['No lands'],axis =1)

ssp = [ssp126,ssp370,ssp585]
ssp_total = [ssp126_total, ssp370_total, ssp585_total]
SSP = ['ssp126','ssp370','ssp585']

plt.rcParams['mathtext.default'] = 'regular'
plt.style.use('seaborn-ticks')
fig,axs = plt.subplots(5,3, sharex = False, sharey = 'row',figsize=(15,20))
ws = 0.15
fig.subplots_adjust(wspace=ws)

for i in range(5):
    
    axs[i,1].set_title(ssp126.columns[i],fontweight = 'bold',loc = 'center')
    axs[i,0].set_ylabel('Area [10${^5}$ x km${^2}$]',fontweight = 'bold')
    for j in range(3):

        #axs[i,j].plot(ssp_total[j].index, ssp_total[j][ssp_total[j].columns[i]] , width = 2,color = '',alpha = 0.5)
        
        #axs[i,j].plot(ssp[j].index,ssp[j][ssp[j].columns[i]],linewidth=0.5,color = 'black')
        axs[i,j].fill_between(y1 = 0,y2 =ssp[j][ssp[j].columns[i]],color = 'red',alpha = 1,x = ssp126.index)
        axs[i,j].fill_between(y1 =0, y2 =ssp_total[j][ssp_total[j].columns[i]],color='tab:blue',alpha = 0.5,x = ssp126.index)
        axs[i,j].set_title(SSP[j],fontweight = 'bold', loc = 'left',y = 0.92, fontsize = 10)

axs[4,1].set_xlabel('Year', fontweight = 'bold')
fig.savefig(r'C:\Users\54021\OneDrive\桌面\桌面\meeting\figure\figures_new\biome_fre1',dpi = 800)











# for i in range(5):
#     for j in range(4):
        
#         x = 

# axs[0].plot(ssp126.iloc[:,0:20], linewidth=1.2)
# axs[0].set_title('ssp126', fontweight = 'bold', fontsize = 15)
# axs[0].set_ylabel('AAEME/Total area per anthrome',fontweight = 'bold', fontsize = 15)
# axs[1].plot(ssp370.iloc[:,0:20],linewidth=1.2)
# axs[1].set_title('ssp370',fontweight = 'bold',fontsize = 15)
# axs[1].set_xlabel('Year',fontweight = 'bold')
# axs[2].plot(ssp585.iloc[:,0:20],linewidth=1.2)
# axs[2].set_title('ssp585',fontweight = 'bold',fontsize = 15)


# fig.legend(ssp126.columns[0:20],loc = 8, ncol = 4, bbox_to_anchor=(0.50, -0.2))
