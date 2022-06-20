# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 16:49:26 2022

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
    anthrome_path = get_all_abs_path('/mnt/data/luyin/Dataprocess/Anthrome')
    print(ssp,len(anthrome_path))
    anthrome_path_ssp = list(filter(lambda x: re.search(ssp, x) != None, anthrome_path))
    anthrome_path_ssp = sorted(anthrome_path_ssp)
    print(ssp,'select anthrome:',anthrome_path_ssp)
    Anthrome_land = []
    for Anthrome_abs_path in anthrome_path_ssp:
        Anthrome_land.append(np.loadtxt(Anthrome_abs_path, skiprows=6))
        print(ssp,'Anthrome shape:',Anthrome_abs_path)
    anthrome_area = pd.DataFrame(index = list(anthrome_cls.index),columns = list(range(2015,2101)))
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
            
            for j in anthrome_cls.index:
                grid_sel = (Land_use == anthrome_cls[j])
                tot_area = np.sum(cell_area[grid_sel])/1000000
                anthrome_area[i][j] = tot_area
                
    
    file_name = 'total_area_anthrome' + ssp + '.xlsx'
    file_path = '/mnt/data/luyin/Dataprocess/Analysis_biome/total_anthrome_area/'+file_name
    anthrome_area.to_excel(file_path,sheet_name = 'total_area',index = True)
                