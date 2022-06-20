# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 10:53:30 2022

@author: 54021
"""

import netCDF4 as nc
import datetime
import os
import re

start = datetime.datetime.now()
# use regular expression to get 5 databases
SSP_path = r'C:\UUstudy\assignment\Master thesis\Dataprocess\Frequency_biome\0.5x0.5'
ssp_path = []

for parent,dirnames,filenames in os.walk(SSP_path):
    for file in filenames:
        ssp_path.append(os.path.join(parent,file))
        
tem = ['80th','90th','95th','99th']
SSP = ['ssp126','ssp370','ssp585']

for ssp in SSP:
    for tem_sel in tem:
        
            
        
        Re_search = re.compile(ssp + '_.*' + tem_sel)
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
            file.close()
              
        print(len(Frequency_GCMs))
            
        file_path = r'C:\UUstudy\assignment\Master thesis\Dataprocess\Frequency_biome\0.5x0.5\GCMs' + ssp +'_' + tem_sel + '.nc'
        
        file_mean = nc.Dataset(file_path,'w',format=('NETCDF4'))
        file_mean.createDimension('time', None)
        file_mean.createDimension('lat', nlat)
        file_mean.createDimension('lon', nlon)
        
        _time = file_mean.createVariable('time', 'f4',('time'))
        _lat = file_mean.createVariable('lat', 'f4', ('lat'))
        _lon = file_mean.createVariable('lon', 'f4', ('lon'))
        _Frequency_mean = file_mean.createVariable('Frequency_mean', 'f4', ('time', 'lat', 'lon'), zlib=True)
          
        _time.units = 'year'  
        
        _Frequency_mean.units = 'number of a single year'
        _Frequency_mean.long_name = 'Mean frequency of five GCMs'
            
        _lat[:] = lat
        _lon[:] = lon
        _time[:] = time[:]
        
        for i in range(0, 86):
            _Frequency_mean[i] = (Frequency_GCMs[0][i] + Frequency_GCMs[1][i] + Frequency_GCMs[2][i] + Frequency_GCMs[3][i] + Frequency_GCMs[4][i])/5
            
        file_mean.close()
        print('Success!')
end = datetime.datetime.now()
print(end-start)
