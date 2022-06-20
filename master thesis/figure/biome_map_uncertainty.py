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

file1 = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Dataprocess\Frequency_biome\0.5x0.5\GFDL-ESM4\ssp126\gfdl-esm4_r1i1p1f1_w5e5_ssp126_fre_biome_80th_global_daily_2015_2100.nc",'r')
file2 = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Dataprocess\Frequency_biome\0.5x0.5\GFDL-ESM4\ssp126\gfdl-esm4_r1i1p1f1_w5e5_ssp126_fre_biome_90th_global_daily_2015_2100.nc",'r')
file3 = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Dataprocess\Frequency_biome\0.5x0.5\GFDL-ESM4\ssp126\gfdl-esm4_r1i1p1f1_w5e5_ssp126_fre_biome_95th_global_daily_2015_2100.nc",'r')
file4 = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Dataprocess\Frequency_biome\0.5x0.5\GFDL-ESM4\ssp126\gfdl-esm4_r1i1p1f1_w5e5_ssp126_fre_biome_99th_global_daily_2015_2100.nc",'r')
fre1 = file1['Frequency'][85]
fre2 = file2['Frequency'][85]
fre3 = file3['Frequency'][85]
fre4 = file4['Frequency'][85]
file = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Data collection\land_use crop\landuse-15crops_2015soc_annual_2015_2100.nc",'r')

fre = [fre1,fre2,fre3,fre4]


lons = file.variables['lon'][:]
lats= file.variables['lat'][:]

plt.rcParams['mathtext.default'] = 'regular'
plt.style.use('seaborn-ticks')
fig,axs = plt.subplots(1, 4,figsize = (15,5))
fig.subplots_adjust(hspace = -0.7)

title_name = ['80th','90th','95th','99th']


for i in range(4):
    axs[i].set_title(title_name[i],fontsize = 13,fontweight = 'bold')
    mp = Basemap(projection='cyl',resolution='c',lon_0 = 0, lat_0 = 0,ax = axs[i] )
    lon,lat = np.meshgrid(lons,lats)
    x, y = mp(lon,lat)
    mask_ocean = maskoceans(lon,lat,fre[i],resolution = 'c')
    c_scheme = mp.pcolor(x,y,np.squeeze(mask_ocean),cmap = 'Reds')
    #mp.drawcoastlines(linewidth = 0.2,linestyle='solid')
    mp.drawmapboundary(linewidth = 0.3,fill_color=None, zorder=None)
    
plt.tight_layout()
plt.savefig(r'C:\Users\54021\OneDrive\桌面\桌面\meeting\figure\figures_new\biome\biome_uncertainty',dpi = 800,bbox_inches = 'tight')
    

