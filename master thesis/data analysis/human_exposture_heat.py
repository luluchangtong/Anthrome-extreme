# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 22:07:16 2022

@author: 54021
"""

import numpy as np
import netCDF4 as nc
import pandas as pd
import datetime
import os
import re
start = datetime.datetime.now() 
# create a pandas series of anthrome classification
anthrome_cls = pd.Series([11,12,21,22,23,24],
                         index =  ['Urban','Mixed settlements','Rice villages',
                                                    'Irrigated villages', 'Rainfed villages',
                                                    'Pastoral villages'])

tem = ['25','26','28','30','33'] 
SSP = ['ssp1','ssp3','ssp5']
SSP_an = ['ssp126','ssp370','ssp585']
  
# read grid area file
grid_file = nc.Dataset(r'/mnt/data/luyin/Dataprocess/grid_area/grid_area_5_arcmin.nc','r')
cell_area = grid_file['cell_area'][:]
grid_file.close()

# get absolute path of all files 
def get_all_abs_path(source_dir):
    path_list = []
    for fpathe, dirs, fs in os.walk(source_dir):
        for f in fs:
            p = os.path.join(fpathe, f)
            path_list.append(p)
            
    return path_list

for ssp,ssp_an in zip(SSP, SSP_an):
    
    

    # get anthorme files absolute path of ssp
    anthrome_path = get_all_abs_path('/mnt/data/luyin/Dataprocess/Anthrome')
    anthrome_path_ssp = list(filter(lambda x: re.search(ssp, x) != None, anthrome_path))
    anthrome_path_ssp = sorted(anthrome_path_ssp)
    print(anthrome_path_ssp)
    
    Anthrome_land = []
    
    # load anthorme database
    for Anthrome_abs_path in anthrome_path:
        Anthrome_land.append(np.loadtxt(Anthrome_abs_path, skiprows=6))
    
    # get population files absolute path
    population_path = get_all_abs_path('/mnt/data/luyin/Datacollection/population')
    population_path_ssp = list(filter(lambda x: re.search(ssp, x) != None, population_path))
    print(population_path_ssp[0])
    population_file = nc.Dataset(population_path_ssp[0],'r')
    population = population_file['population'][:]
    population_file.close()
    
        
    for tem_sel in tem:
        Frequency_human_path = get_all_abs_path('/mnt/data/luyin/Dataprocess/Frequency_human/ipsl-cm6a-lr')
        pattern = ssp_an + '.*_' + tem_sel
        path1 = list(filter(lambda x: re.search(pattern, x) != None, Frequency_human_path))
        print('Fre_file:',path1)
        path1 = path1[0]
        # read frequnecy files of netCDF4 format
        file = nc.Dataset(path1,'r')
        lat = file['lat'][:]
        lon = file['lon'][:]
        nlat = len(lat)
        nlon = len(lon)
        time = file['time'][:]
        Frequency = file['Frequency'][:]
        
        # create a Dataframe to contain exposure data
        Human_exposure = pd.DataFrame(index = list(anthrome_cls.index), columns=list(range(2015,2101)))
        Tot_exposure = []
        # every year analysis
        for i in range(2015,2101):
            
            if (i >= 2015) & (i<2020):
                Land_use = Anthrome_land[0]
           
            elif (i >= 2020) & (i < 2030):
                Land_use = Anthrome_land[1]
               
            elif (i >= 2030) & (i < 2040):
                Land_use = Anthrome_land[2]
               
            elif (i >= 2040) & (i < 2050):
                Land_use = Anthrome_land[3]
               
            elif (i >= 2050) & (i < 2060):
                Land_use = Anthrome_land[4]
               
            elif (i >= 2060) & (i < 2070):
                Land_use = Anthrome_land[5]
               
            elif (i >= 2070) & (i < 2080):
                Land_use = Anthrome_land[6]
               
            elif (i >= 2080) & (i < 2090):
                Land_use = Anthrome_land[7]
               
            elif (i >= 2090) & (i < 2099):
                Land_use = Anthrome_land[8]
               
            else:
                Land_use = Anthrome_land[9]
               
            fre = Frequency[i-2015]
            
            # population starts from 2006
            pop = population[i+9-2015]
            
            # calculate exposure for each grid
            Tot_exposure.append(fre * pop)
            
            # select each anthrome
            for j in anthrome_cls.index:
                
                # select each anthrome
                grid_sel = (Land_use == anthrome_cls[j])
                Tot = Tot_exposure[i-2015]
                
                # calculate total exposure 
                Human_exposure[i][j] = np.sum(Tot[grid_sel])
                
        # create a xlsx file to save data
        
        fre_path_split = path1.split("/")[-1]
        file_abs_name = 'human_exposure_' + fre_path_split
        file_excel = file_abs_name.replace('.nc','.xlsx')
        file_path = '/mnt/data/luyin/Dataprocess/human_analysis/excel/ipsl-cm6a-lr/' + file_excel
        Human_exposure.to_excel(file_path,sheet_name= 'ipsl-cm6a-lr',index = True)
        print(file_path,'Success!')
        
        # create a netCDF4 file to contain data
        nc_file_path = '/mnt/data/luyin/Dataprocess/human_analysis/netCDF4/ipsl-cm6a-lr/' + file_abs_name
        nc_file = nc.Dataset(nc_file_path,'w', format=('NETCDF4'))
       
        nc_file.createDimension('time', None)
        nc_file.createDimension('lat', nlat)
        nc_file.createDimension('lon', nlon)
        
        _time = nc_file.createVariable('time', 'f4',('time'))
        _lat = nc_file.createVariable('lat', 'f4', ('lat'))
        _lon = nc_file.createVariable('lon', 'f4', ('lon'))
        _population_exposure = nc_file.createVariable('popualtion_exposure', 'f4', ('time', 'lat', 'lon'), zlib=True)
          
        _time.units = 'year'  
        
        _population_exposure.units = 'population*day/year'
            
        _lat[:] = lat
        _lon[:] = lon
        _time[:] = np.array(range(2015,2101))
        _population_exposure[:] = Tot_exposure
        
        
        nc_file.close()
        print('netCDf4:',nc_file_path,'Success!')
        
end = datetime.datetime.now()

print('running time:', end - start) 
            
            
            
                
        
    

