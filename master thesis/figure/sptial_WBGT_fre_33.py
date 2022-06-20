# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 22:07:16 2022

@author: 54021
"""

import netCDF4 as nc
import matplotlib as mpl
import os 
os.environ["PROJ_LIB"] = r"C:\Users\54021\anaconda3\Library\share"
from mpl_toolkits.basemap import Basemap, maskoceans
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

file1 = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Dataprocess\Frequency\human\GCM_mean\GCM_meanssp126_33.nc",'r')
file2 = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Dataprocess\Frequency\human\GCM_mean\GCM_meanssp370_33.nc",'r')
file3 = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Dataprocess\Frequency\human\GCM_mean\GCM_meanssp585_33.nc",'r')
ssp126 = file1['Frequency_mean'][85]
ssp370 = file2['Frequency_mean'][85]
ssp585 = file3['Frequency_mean'][85]
SSP = [ssp126,ssp370,ssp585]

lons = file1.variables['lon'][:]
lats= file1.variables['lat'][:]
name = ['ssp126','ssp370','ssp585']



plt.rcParams['mathtext.default'] = 'regular'
#plt.style.use('seaborn-ticks')
fig,axs = plt.subplots(1,3)
fig.subplots_adjust(wspace = -1)

sns_colors = sns.color_palette('Reds',7)

cmap = mpl.colors.ListedColormap(sns_colors)
cmap.set_extremes(over = 'black')
norm = mpl.colors.BoundaryNorm([0,30,60,100,150,200,250,300], cmap.N) 


for i in range(3):
        axs[i].set_title(name[i],fontsize = 10,fontweight = 'bold')


        mp = Basemap(projection='robin',resolution='c',lon_0 = 0, lat_0 = 0,ax = axs[i] )
        mp.drawparallels(np.arange(-90.,120.,30.),linewidth= 0.2)
        mp.drawmeridians(np.arange(0.,360.,60.),linewidth= 0.2)
        
        lon,lat = np.meshgrid(lons,lats)
        x, y = mp(lon,lat)
        mask_ocean = maskoceans(lon,lat,SSP[i],resolution = 'c')
        c_scheme = mp.pcolor(x,y,np.squeeze(mask_ocean),cmap= cmap,norm =norm)
        
        
        
        
        mp.drawmapboundary(linewidth = 0.3,fill_color=None, zorder=None)

plt.tight_layout()

fig.text(0.1,0.23, s = 'WBGT > 33°C',fontsize = 8, fontweight = 'bold')
fig.text(0.75,0.23, s = '(Days/year)',fontsize = 8, fontweight = 'bold')

fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap),orientation = 'horizontal',ax=axs,shrink=0.5,anchor=(0.5,1.8),extend ='max')

# plt.title('growing?')
#cbar = mp.colorbar(c_scheme, location = 'right', pad = '10%')

plt.savefig(r'C:\Users\54021\OneDrive\桌面\桌面\meeting\figure\figures_new\human\WBGT_fre_33',dpi = 1200,bbox_inches = 'tight')







