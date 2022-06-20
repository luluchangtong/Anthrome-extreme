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
        Frequency_human_path = get_all_abs_path('/mnt/data/luyin/Dataprocess/Frequency_human/GCMs_mean')
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
        Frequency = file['Frequency_mean'][:]
        
        # create a Dataframe to contain exposure data
        Human_percentage = pd.DataFrame(index = list(anthrome_cls.index), columns=list(range(2015,2101)))
        Human_percentage_10 = pd.DataFrame(index = list(anthrome_cls.index), columns=list(range(2015,2101)))
        Human_total = pd.DataFrame(index = list(anthrome_cls.index), columns=list(range(2015,2101)))
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
            
            
            # select each anthrome
            for j in anthrome_cls.index:
                
                # select each anthrome
                grid_sel = (Land_use == anthrome_cls[j])
                heat_select = ((fre > 0) & grid_sel)
                heat_select_10 = ((fre>10) & grid_sel)
                
                # calculate total exposure 
                Human_total[i][j] = np.sum(pop[grid_sel])
                Human_percentage[i][j] = np.sum(pop[heat_select])
                Human_percentage_10[i][j] = np.sum(pop[heat_select_10])
                
        # create a xlsx file to save data
        
        fre_path_split = path1.split("/")[-1]
        file_abs_name = 'population_%_' + fre_path_split
        file_excel = file_abs_name.replace('.nc','.xlsx')
        file_path = '/mnt/data/luyin/Dataprocess/human_analysis/population_%/GCMs_mean/' + file_excel
        Human_percentage.to_excel(file_path,index = True)
        
        fre_path_split = path1.split("/")[-1]
        file_abs_name1 = 'population_%_10d_' + fre_path_split
        file_excel1 = file_abs_name1.replace('.nc','.xlsx')
        file_path1 = '/mnt/data/luyin/Dataprocess/human_analysis/population_%_10d/GCMs_mean/' + file_excel1
        Human_percentage_10.to_excel(file_path1,index = True)
        
        file_abs_name2 = 'population_total_' + fre_path_split
        file_excel2 = file_abs_name2.replace('.nc','.xlsx')
        file_path2 = '/mnt/data/luyin/Dataprocess/human_analysis/total_population/GCMs_mean/' + file_excel2
        Human_total.to_excel(file_path2,index = True)
        
        
        
        print(file_path,file_path2,'Success!')
        
        # create a netCDF4 file to contain data
        
        
end = datetime.datetime.now()

print('running time:', end - start) 
            
            
            
                
        
    

