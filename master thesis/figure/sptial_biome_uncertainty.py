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

def get_all_abs_path(source_dir):
    path_list = []
    for fpathe, dirs, fs in os.walk(source_dir):
        for f in fs:
            p = os.path.join(fpathe, f)
            path_list.append(p)
            
    return path_list
files_list = get_all_abs_path(r'C:\UUstudy\assignment\Master thesis\Dataprocess\Frequency_biome\0.5x0.5\GCMs')
files_list = sorted(files_list)

threshold = ['80th','90th','95th','99th']
name = ['ssp126','ssp370','ssp585']

file_name = [i + '_' + j for i in name for j in threshold ]
SSP = []
for i in range(12):
    file = nc.Dataset(files_list[i],'r')
    locals()[file_name[i]] = file['Frequency_mean'][85]
    SSP.append(locals()[file_name[i]]) 
file = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Data collection\land_use crop\landuse-15crops_2015soc_annual_2015_2100.nc",'r')

lons = file.variables['lon'][:]
lats= file.variables['lat'][:]


plt.rcParams['mathtext.default'] = 'regular'
#plt.style.use('seaborn-ticks')
fig,axs = plt.subplots(4,3)
fig.subplots_adjust(wspace =-0.95,hspace = -0.3)

sns_colors = sns.color_palette('Reds',12)

cmap = mpl.colors.ListedColormap(sns_colors)
cmap.set_extremes(over = 'black')
norm = mpl.colors.BoundaryNorm([0,30,60,90,120,150,180,210,240,270,300,330], cmap.N) 


for i in range(4):
    for j in range(3):
        #axs[i].set_title(name[i],fontsize = 10,fontweight = 'bold')


        mp = Basemap(projection='robin',resolution='c',lon_0 = 0, lat_0 = 0,ax = axs[i,j] )
        mp.drawparallels(np.arange(-90.,120.,30.),linewidth= 0.2)
        mp.drawmeridians(np.arange(0.,360.,60.),linewidth= 0.2)
        mp.drawmapboundary(linewidth = 0.3)
        
        lon,lat = np.meshgrid(lons,lats)
        x, y = mp(lon,lat)
        mask_ocean = maskoceans(lon,lat,SSP[j*4+i],resolution = 'c')
        c_scheme = mp.pcolor(x,y,np.squeeze(mask_ocean),cmap= cmap,norm =norm)
        
        
        
        
        mp.drawmapboundary(linewidth = 0.3,fill_color=None, zorder=None)

plt.tight_layout()

for i in range(3):
    axs[0,i].set_title(name[i],fontsize = 6,fontweight = 'bold')
    
for j in range(4):
    axs[j,0].set_ylabel('Threshold = {}'.format(threshold[j]),fontsize = 4)
#fig.text(0.09,0.48, s = 'WBGT > 33°C',fontsize = 7, fontweight = 'bold')
fig.text(0.65,0.28, s = '(Days/year)',fontsize = 6, fontweight = 'bold')

cbar = fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap),orientation = 'horizontal',ax=axs,shrink=0.4,anchor=(0.5,1.8),extend ='max')
cbar.ax.tick_params(labelsize=7)
# plt.title('growing?')
#cbar = mp.colorbar(c_scheme, location = 'right', pad = '10%')

plt.savefig(r'C:\Users\54021\OneDrive\桌面\桌面\meeting\figure\figures_new\biome\spatial_biome_uncertainty',dpi = 1200,bbox_inches = 'tight')









