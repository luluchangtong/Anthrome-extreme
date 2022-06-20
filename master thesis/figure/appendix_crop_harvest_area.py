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

file = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Data collection\land_use crop\landuse-15crops_2015soc_annual_2015_2100.nc",'r')
lons = file.variables['lon'][:]
lats= file.variables['lat'][:]

maize_irrigated = file['maize_irrigated'][0]>0
maize_rainfed = file['maize_rainfed'][0]
oil_crops_soybean_irrigated = file['oil_crops_soybean_irrigated'][0]>0
oil_crops_soybean_rainfed = file['oil_crops_soybean_rainfed'][0]>0
rice_irrigated = file['rice_irrigated'][0]>0
rice_rainfed = file['rice_rainfed'][0]>0
temperate_cereals_irrigated = file['temperate_cereals_irrigated'][0]>0
temperate_cereals_rainfed = file['temperate_cereals_rainfed'][0]>0

crops = [maize_irrigated,maize_rainfed,oil_crops_soybean_irrigated,oil_crops_soybean_rainfed,rice_irrigated,rice_rainfed,temperate_cereals_irrigated,temperate_cereals_rainfed]
name = ['Maize_irrigated','Maize_rainfed','Soybean_irrigated','Soybean_rainfed','Rice_irrigated','Rice_rainfed','Temperate_cereals_irrigated','Temperate_cereals_rainfed']

plt.rcParams['mathtext.default'] = 'regular'
plt.style.use('seaborn-ticks')
fig,axs = plt.subplots(4, 2,figsize = (14,15))
fig.subplots_adjust(wspace = -1, hspace = -0.7)

cmap_list = ['Blues','BuGn','Purples','Oranges']

for i in range(4):
    for j in range(2):
        axs[i,j].set_title(name[i*2+j],fontsize = 13,fontweight = 'bold')


        mp = Basemap(projection='robin',resolution='c',lon_0 = 0, lat_0 = 0,ax = axs[i,j] )
        
        
        lon,lat = np.meshgrid(lons,lats)
        x, y = mp(lon,lat)
        
        c_scheme = mp.pcolor(x,y,np.squeeze(crops[i*2+j]),cmap=cmap_list[i])
        mp.drawparallels(np.arange(-90.,120.,30.),linewidth= 0.2)
        mp.drawmeridians(np.arange(0.,360.,60.),linewidth= 0.2)
        
        
        #mp.drawcoastlines(linewidth = 0.2,linestyle='solid')
        mp.drawmapboundary(linewidth = 0.3,fill_color=None, zorder=None)
        
plt.tight_layout()
# plt.title('growing?')
#cbar = mp.colorbar(c_scheme, location = 'right', pad = '10%')

plt.savefig(r'C:\Users\54021\OneDrive\桌面\桌面\meeting\figure\figures_new\croped\harvested_area',dpi = 800,bbox_inches = 'tight')






