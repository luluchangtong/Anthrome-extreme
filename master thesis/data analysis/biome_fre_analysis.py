# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 10:30:10 2022

@author: 54021
"""

import numpy as np
import netCDF4 as nc
import pandas as pd
import datetime
import os
import re

# create a pandas series of anthrome classification
anthrome_cls = pd.Series([11,12,21,22,23,24,31,32,33,34,41,42,43,51,52,53,54,61,62,63,70],
                         index =  ['Urban','Mixed settlements','Rice villages',
                                                    'Irrigated villages', 'Rainfed villages',
                                                    'Pastoral villages','Residential irrigated croplands',
                                                    'Residential rainfed croplands','Populated croplands',
                                                    'Remote croplands', 'Residential rangelands',
                                                    'Populated rangelands','Remote rangelands',
                                                    'Residential woodlands','Populated woodlands',
                                                    'Remote woodlands','Inhabited treeless & barren lands',
                                                    'Wild woodlands','Wild treeless & barren lands',
                                                    'Ice & uninhabited','No lands'])

start = datetime.datetime.now()    
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
# SSP for loop
SSP = ['ssp126','ssp370','ssp585']
for ssp in SSP:
    
    
    # look for anthrome files for each ssp
    anthrome_path = get_all_abs_path('/mnt/data/luyin/Dataprocess/Anthrome')
    print(ssp,len(anthrome_path))
    anthrome_path_ssp = list(filter(lambda x: re.search(ssp, x) != None, anthrome_path))
    anthrome_path_ssp = sorted(anthrome_path_ssp)
    print(ssp,'select anthrome:',anthrome_path_ssp)
    
    
    # look for frequency files for each ssp
    fre_path = get_all_abs_path('/mnt/data/luyin/Dataprocess/Frequency_biome')
    print(ssp,len(fre_path))
    fre_path_ssp = list(filter(lambda x: re.search(ssp, x) != None, fre_path))
    fre_path_ssp = sorted(fre_path_ssp)
    print(ssp,'selected fre:',len(fre_path_ssp))
    
    
    # createa blank list to store land data
    Anthrome_land = []
    for Anthrome_abs_path in anthrome_path_ssp:
        Anthrome_land.append(np.loadtxt(Anthrome_abs_path, skiprows=6))
    print(ssp,'Anthrome shape:',len(Anthrome_land))
    
    for fre_abs_path in fre_path_ssp:
        print('Frequnecy_file:',fre_abs_path)
        Fre_file = nc.Dataset(fre_abs_path,'r')
        Frequency = Fre_file['Frequency']
        print('Success!')
        
        # selected dynamic of anthrome
       
        anthrome_fre = pd.DataFrame(index = anthrome_cls.index,columns = list(range(2015,2101)))
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
            
            # calculate mean frequency of each biome
        
            for j in anthrome_cls.index:
                grid_sel = (Land_use == anthrome_cls[j])
                tot_area = np.sum(cell_area[grid_sel])
                tot_fre = np.sum(fre[grid_sel]*cell_area[grid_sel])
                mean_fre = tot_fre/tot_area
                anthrome_fre[i][j] = mean_fre
                
        fre_abs_path_split = fre_abs_path.split("/")[-1]
        file_name = 'accumu_fre_' + fre_abs_path_split
        file_name_xl = file_name.replace('.nc','.xlsx')
        file_path = '/mnt/data/luyin/Dataprocess/Analysis_biome/mean_fre/'+file_name_xl
        anthrome_fre.to_excel(file_path,sheet_name = 'accumulated frequency',index = True)
        
        Fre_file.close()
        
        print(file_name,':success')
            
end = datetime.datetime.now()

print('running time:', end - start)            
            
           
            
            
                
            
            
            
        
   
    

    