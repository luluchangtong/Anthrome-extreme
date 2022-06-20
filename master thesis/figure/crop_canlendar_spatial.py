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
import matplotlib as mpl
import seaborn as sns


maize_ir = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Data collection\Crop calendar\mai_ir_ggcmi_crop_calendar_phase3_v1.01 (1).nc4",'r')
maize_rf = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Data collection\Crop calendar\mai_rf_ggcmi_crop_calendar_phase3_v1.01.nc4",'r')
ri1_ir = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Data collection\Crop calendar\ri1_ir_ggcmi_crop_calendar_phase3_v1.01.nc4",'r')
ri1_rf = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Data collection\Crop calendar\ri1_rf_ggcmi_crop_calendar_phase3_v1.01.nc4",'r')
ri2_ir = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Data collection\Crop calendar\ri2_ir_ggcmi_crop_calendar_phase3_v1.01.nc4",'r')
ri2_rf = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Data collection\Crop calendar\ri2_rf_ggcmi_crop_calendar_phase3_v1.01.nc4",'r')
soy_ir = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Data collection\Crop calendar\soy_ir_ggcmi_crop_calendar_phase3_v1.01.nc4",'r')
soy_rf = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Data collection\Crop calendar\soy_rf_ggcmi_crop_calendar_phase3_v1.01.nc4",'r')
wwh_ir = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Data collection\Crop calendar\wwh_ir_ggcmi_crop_calendar_phase3_v1.01.nc4",'r')
wwh_rf = nc.Dataset(r"C:\UUstudy\assignment\Master thesis\Data collection\Crop calendar\wwh_rf_ggcmi_crop_calendar_phase3_v1.01.nc4",'r')
lons = maize_ir.variables['lon'][:]
lats= maize_ir.variables['lat'][:]
file = [maize_ir,maize_rf,ri1_ir,ri1_rf,ri2_ir,ri2_rf,soy_ir,soy_rf,wwh_ir,wwh_rf]



name1 = ['Maize_ir_planting','Maize_rf_planting','Soybean_ir_planting','Soybean_rf_planting','Rice1_ir_planting','Rice1_rf_planting','Rice2_ir_planting','Rice2_rf_planting','Wheat_ir_planting','Wheat_rf_planting']
name2 = ['Maize_ir_maturity','Maize_rf_maturity','Soybean_ir_maturity','Soybean_rf_maturity','Rice1_ir_maturity','Rice1_rf_maturity','Rice2_ir_maturity','Rice2_rf_maturity','Wheat_ir_maturity','Wheat_rf_maturity']
plt.rcParams['mathtext.default'] = 'regular'
plt.style.use('seaborn-ticks')
fig,axs = plt.subplots(5,2,figsize = (16,18))
fig.subplots_adjust(wspace = -0.8, hspace = -0.35)


ticks = [0,40,80,120,160,200,240,280,320,365]

for i in range(5,10):
    
    
    axs[i-5,0].set_title(name1[i],fontsize = 13,fontweight = 'bold')


    mp = Basemap(projection='robin',resolution='c',lon_0 = 0, lat_0 = 0,ax = axs[i-5,0] )
    
    
    lon,lat = np.meshgrid(lons,lats)
    x, y = mp(lon,lat)
    
    c_scheme = mp.pcolor(x,y,np.squeeze(file[i]['planting_day'][:]),cmap='jet')
    mp.drawparallels(np.arange(-90.,120.,30.),linewidth= 0.2)
    mp.drawmeridians(np.arange(0.,360.,60.),linewidth= 0.2)
    
    
    #mp.drawcoastlines(linewidth = 0.2,linestyle='solid')
    mp.drawmapboundary(linewidth = 0.3,fill_color=None, zorder=None)
    
for i in range(5,10):
    
    
    axs[i-5,1].set_title(name2[i],fontsize = 13,fontweight = 'bold')


    mp = Basemap(projection='robin',resolution='c',lon_0 = 0, lat_0 = 0,ax = axs[i-5,1] )
    
    
    lon,lat = np.meshgrid(lons,lats)
    x, y = mp(lon,lat)
    
    c_scheme = mp.pcolor(x,y,np.squeeze(file[i]['maturity_day'][:]),cmap='jet')
    mp.drawparallels(np.arange(-90.,120.,30.),linewidth= 0.2)
    mp.drawmeridians(np.arange(0.,360.,60.),linewidth= 0.2)
    
    
    #mp.drawcoastlines(linewidth = 0.2,linestyle='solid')
    mp.drawmapboundary(linewidth = 0.3,fill_color=None, zorder=None)
    
cax = fig.add_axes([0.145,-0.03,0.7,.03])
fig.colorbar(c_scheme,orientation = 'horizontal',ax=axs,pad = 0.2,ticks = ticks,cax = cax)   
plt.tight_layout()
# plt.title('growing?')
#cbar = mp.colorbar(c_scheme, location = 'right', pad = '10%')

plt.savefig(r'C:\Users\54021\OneDrive\桌面\桌面\meeting\figure\figures_new\croped\crop_calendar2',dpi = 800,bbox_inches = 'tight')








