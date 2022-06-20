# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 13:50:04 2022

@author: 54021
"""

import os 
import re 
import netCDF4 as nc
from mpl_toolkits.basemap import Basemap, maskoceans
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# read population file 
ssp126_file = nc.Dataset(r'D:\UUstudy\assignment\Master thesis\Dataprocess\human_analysis\netCDF4\GCMs_mean\human_exposure_ssp126_30.nc','r')
ssp370_file = nc.Dataset(r'D:\UUstudy\assignment\Master thesis\Dataprocess\human_analysis\netCDF4\GCMs_mean\human_exposure_ssp370_30.nc','r')
ssp585_file = nc.Dataset(r'D:\UUstudy\assignment\Master thesis\Dataprocess\human_analysis\netCDF4\GCMs_mean\human_exposure_ssp585_30.nc','r')

# read anthrome data

an_ssp1_20 = np.loadtxt(r'D:\UUstudy\assignment\Master thesis\Data collection\anthromes_12K_full\output\output\anthromesSSP1_20.asc',skiprows = 6)
an_ssp1_50 = np.loadtxt(r'D:\UUstudy\assignment\Master thesis\Data collection\anthromes_12K_full\output\output\anthromesSSP1_50.asc',skiprows = 6)
an_ssp1_90 = np.loadtxt(r'D:\UUstudy\assignment\Master thesis\Data collection\anthromes_12K_full\output\output\anthromesSSP1_90.asc',skiprows = 6)

an_ssp3_20 = np.loadtxt(r'D:\UUstudy\assignment\Master thesis\Data collection\anthromes_12K_full\output\output\anthromesSSP3_20.asc',skiprows = 6)
an_ssp3_50 = np.loadtxt(r'D:\UUstudy\assignment\Master thesis\Data collection\anthromes_12K_full\output\output\anthromesSSP3_50.asc',skiprows = 6)
an_ssp3_90 = np.loadtxt(r'D:\UUstudy\assignment\Master thesis\Data collection\anthromes_12K_full\output\output\anthromesSSP3_90.asc',skiprows = 6)

an_ssp5_20 = np.loadtxt(r'D:\UUstudy\assignment\Master thesis\Data collection\anthromes_12K_full\output\output\anthromesSSP5_20.asc',skiprows = 6)
an_ssp5_50 = np.loadtxt(r'D:\UUstudy\assignment\Master thesis\Data collection\anthromes_12K_full\output\output\anthromesSSP5_50.asc',skiprows = 6)
an_ssp5_90 = np.loadtxt(r'D:\UUstudy\assignment\Master thesis\Data collection\anthromes_12K_full\output\output\anthromesSSP5_90.asc',skiprows = 6)

# calculate mean population exposure for 2020-2030, 2050-2060, 2090-2100

ssp126_20_av = np.mean(ssp126_file['popualtion_exposure'][6:16,:,:],axis = 0)
ssp370_20_av = np.mean(ssp370_file['popualtion_exposure'][6:16,:,:],axis = 0)
ssp585_20_av = np.mean(ssp585_file['popualtion_exposure'][6:16,:,:],axis = 0)

ssp126_50_av = np.mean(ssp126_file['popualtion_exposure'][36:46,:,:],axis = 0)
ssp370_50_av = np.mean(ssp370_file['popualtion_exposure'][36:46,:,:],axis = 0)
ssp585_50_av = np.mean(ssp585_file['popualtion_exposure'][36:46,:,:],axis = 0)

ssp126_90_av = np.mean(ssp126_file['popualtion_exposure'][76:86,:,:],axis = 0)
ssp370_90_av = np.mean(ssp370_file['popualtion_exposure'][76:86,:,:],axis = 0)
ssp585_90_av = np.mean(ssp585_file['popualtion_exposure'][76:86,:,:],axis = 0)

bo_ssp1_20 = ( (an_ssp1_20 == 11) | (an_ssp1_20 == 12) | (an_ssp1_20 == 21) | (an_ssp1_20 == 22) | (an_ssp1_20 == 23) | (an_ssp1_20 == 24))
bo_ssp1_20 = (bo_ssp1_20 == 0)
ssp126_20_av[bo_ssp1_20] = 0

bo_ssp1_50 = ( (an_ssp1_50 == 11) | (an_ssp1_50 == 12) | (an_ssp1_50 == 21) | (an_ssp1_50 == 22) | (an_ssp1_50 == 23) | (an_ssp1_50 == 24))
bo_ssp1_50 = (bo_ssp1_50 == 0)
ssp126_50_av[bo_ssp1_50] = 0

bo_ssp1_90 = ( (an_ssp1_90 == 11) | (an_ssp1_90 == 12) | (an_ssp1_90 == 21) | (an_ssp1_90 == 22) | (an_ssp1_90 == 23) | (an_ssp1_90 == 24))
bo_ssp1_90 = (bo_ssp1_90 == 0)
ssp126_90_av[bo_ssp1_90] = 0

bo_ssp3_20 = ( (an_ssp3_20 == 11) | (an_ssp3_20 == 12) | (an_ssp3_20 == 21) | (an_ssp3_20 == 22) | (an_ssp3_20 == 23) | (an_ssp3_20 == 24))
bo_ssp3_20 = (bo_ssp3_20 == 0)
ssp370_20_av[bo_ssp3_20] = 0

bo_ssp3_50 = ( (an_ssp3_50 == 11) | (an_ssp3_50 == 12) | (an_ssp3_50 == 21) | (an_ssp3_50 == 22) | (an_ssp3_50 == 23) | (an_ssp3_50 == 24))
bo_ssp3_50 = (bo_ssp3_50 == 0)
ssp370_50_av[bo_ssp3_50] = 0

bo_ssp3_90 = ( (an_ssp3_90 == 11) | (an_ssp3_90 == 12) | (an_ssp3_90 == 21) | (an_ssp3_90 == 22) | (an_ssp3_90 == 23) | (an_ssp3_90 == 24))
bo_ssp3_90 = (bo_ssp3_90 == 0)
ssp370_90_av[bo_ssp3_90] = 0

bo_ssp5_20 = ( (an_ssp5_20 == 11) | (an_ssp5_20 == 12) | (an_ssp5_20 == 21) | (an_ssp5_20 == 22) | (an_ssp5_20 == 23) | (an_ssp5_20 == 24))
bo_ssp5_20 = (bo_ssp5_20 == 0)
ssp585_20_av[bo_ssp5_20] = 0

bo_ssp5_50 = ( (an_ssp5_50 == 11) | (an_ssp5_50 == 12) | (an_ssp5_50 == 21) | (an_ssp5_50 == 22) | (an_ssp5_50 == 23) | (an_ssp5_50 == 24))
bo_ssp5_50 = (bo_ssp5_50 == 0)
ssp585_50_av[bo_ssp5_50] = 0

bo_ssp5_90 = ( (an_ssp5_90 == 11) | (an_ssp5_90 == 12) | (an_ssp5_90 == 21) | (an_ssp5_90 == 22) | (an_ssp5_90 == 23) | (an_ssp5_90 == 24))
bo_ssp5_90 = (bo_ssp5_90 == 0)
ssp585_90_av[bo_ssp5_90] = 0

# make geo figure
lons = ssp126_file.variables['lon'][:]
lats = ssp126_file.variables['lat'][:]

mp = Basemap(projection='robin',resolution='c',lat_0=0,lon_0=0)

plt.figure(dpi = 800)
lon,lat = np.meshgrid(lons,lats)
x, y = mp(lon,lat)
s = ssp126_20_av
c_scheme = mp.pcolor(x,y,np.squeeze(s),cmap='Reds')

mp.drawcoastlines()
mp.drawcountries()
plt.title('try')
cbar = mp.colorbar(c_scheme, location = 'right', pad = '10%')

plt.show()


