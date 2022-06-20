# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 14:24:44 2022

@author: 54021
"""

import netCDF4 as nc
import datetime
import os
import re

start = datetime.datetime.now()
# use regular expression to get 5 databases
SSP_path = '/mnt/data/luyin/Dataprocess/Frequency_biome'
ssp_path = []

for parent,dirnames,filenames in os.walk(SSP_path):
    for file in filenames:
        ssp_path.append(os.path.join(parent,file))
        
Re_search = re.compile('ssp585.*99th')
GCMs_sel = [f for f in ssp_path if re.search(Re_search, f)]
print(GCMs_sel)
print(len(GCMs_sel))

Frequency_GCMs = []
for file_path in GCMs_sel:
    file = nc.Dataset(file_path,'r')
    lat = file.variables['lat'][:]
    lon = file.variables['lon'][:]
    nlat = len(lat)
    nlon = len(lon)
    time = file.variables['time']
    Frequency_GCMs.append(file['Frequency'][:])
    
      
print(len(Frequency_GCMs))
    
file_path = '/mnt/data/luyin/Dataprocess/Frequency_biome/GCM_mean/Mean_GCMs_ssp585_99th.nc'

file_mean = nc.Dataset('/mnt/data/luyin/Dataprocess/Frequency_biome/GCM_mean/Mean_fre_GCMs_ssp585_99th.nc','w',format=('NETCDF4'))
file_mean.createDimension('time', None)
file_mean.createDimension('lat', nlat)
file_mean.createDimension('lon', nlon)

_time = file_mean.createVariable('time', 'f4',('time'))
_lat = file_mean.createVariable('lat', 'f4', ('lat'))
_lon = file_mean.createVariable('lon', 'f4', ('lon'))
_Frequency_mean = file_mean.createVariable('Frequency', 'f4', ('time', 'lat', 'lon'), zlib=True)
  
_time.units = 'year'  

_Frequency_mean.units = 'number of a single year'
_Frequency_mean.long_name = 'Mean frequency of five GCMs'
    
_lat[:] = lat
_lon[:] = lon
_time[:] = time[:]

for i in range(0, 86):
    _Frequency_mean[i] = (Frequency_GCMs[0][i] + Frequency_GCMs[1][i] + Frequency_GCMs[2][i] + Frequency_GCMs[3][i] + Frequency_GCMs[4][i])/5
    
file_mean.close()
end = datetime.datetime.now()
print(end-start)