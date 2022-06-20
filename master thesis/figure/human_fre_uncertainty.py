# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 22:07:16 2022

@author: 54021
"""

import netCDF4 as nc
import os 
os.environ["PROJ_LIB"] = r"C:\Users\54021\anaconda3\Library\share"
from mpl_toolkits.basemap import Basemap, maskoceans
import matplotlib.pyplot as plt
import numpy as np

file1 = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Dataprocess\Frequency\human\GCM_mean\GCM_meanssp370_26.nc",'r')
file2 = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Dataprocess\Frequency\human\GCM_mean\GCM_meanssp370_30.nc",'r')
file3 = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Dataprocess\Frequency\human\GCM_mean\GCM_meanssp370_33.nc",'r')

fre1 = file1['Frequency_mean'][85]
fre2 = file2['Frequency_mean'][85]
fre3 = file3['Frequency_mean'][85]

fre = [fre1,fre2,fre3]


lons = file1.variables['lon'][:]
lats= file1.variables['lat'][:]

plt.rcParams['mathtext.default'] = 'regular'
plt.style.use('seaborn-ticks')
fig,axs = plt.subplots(1, 3,figsize = (13,4.8))
fig.subplots_adjust(hspace = -0.7)

title_name = ['WBGT = 26°C','WBGT = 30°C','WBGT = 33°C']


for i in range(3):
    axs[i].set_title(title_name[i],fontsize = 13,fontweight = 'bold')
    mp = Basemap(projection='cyl',resolution='c',lon_0 = 0, lat_0 = 0,ax = axs[i] )
    lon,lat = np.meshgrid(lons,lats)
    x, y = mp(lon,lat)
    mask_ocean = maskoceans(lon,lat,fre[i],resolution = 'c')
    c_scheme = mp.pcolor(x,y,np.squeeze(mask_ocean),cmap = 'Reds')
    #mp.drawcoastlines(linewidth = 0.2,linestyle='solid')
    mp.drawmapboundary(linewidth = 0.3,fill_color=None, zorder=None)
    
plt.tight_layout()
plt.savefig(r'C:\Users\54021\OneDrive\桌面\桌面\meeting\figure\figures_new\human\tre_uncertainty',dpi = 800,bbox_inches = 'tight')
    

