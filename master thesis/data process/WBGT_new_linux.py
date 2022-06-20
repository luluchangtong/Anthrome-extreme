#!/usr/bin/python3.9

"""
Created on Sat Jan 22 17:40:29 2022

@author: Lu Yin, l.yin1@students.uu.nl, yinlu268@gmail.com
This program refers to following sources:
Github: https://github.com/dw-li/WBGT/find/master
National Weather Service: https://www.weather.gov/ama/heatindex
"""

import datetime
import netCDF4 as nc
import os 
import re

start = datetime.datetime.now()

# set internal parameters to calculate the WBGT
B = 0
a0 = -10.3
a1 = 1.1
a2 = 0.047

b0 = -42.379
b1 = 2.04901523
b2 = 10.14333127
b3 = -0.22475541
b4 = -6.83783*10**(-3)
b5 = -5.481717*10**(-2)
b6 = 1.22874*10**(-3)
b7 = 8.5282*10**(-4)
b8 = -1.99*10**(-6)

# tempeareture threshold in algorithm and relative humidity threshold

Tmax_threshold = [40.0, 79.0, 80.0, 112.0, 87.0]
RH_threshold = [13.0,85.0]

'''Wet bulb globe temperature caculation, this fuction uses near surface relative humidity(%) and near surface daily
max temperature(F) to calculate the WBGT, the detailed information and algorithm can be found at 
https://www.weather.gov/ama/heatindex. and https://doi.org/10.1073/pnas.2024792118'''

def Wet_bulb_globe_temperature(Tmax_K, RH):
    Tmax = 1.8*(Tmax_K-273.15)+32 # transfer K to F
    
    HI = (0.5*(Tmax+61.0+(Tmax-68.0)*1.2+(RH*0.094))+Tmax)/2 
    
    B = b0 + b1*Tmax + b2*RH + b3* Tmax*RH + b4*Tmax**2 + b5*RH**2 + b6*Tmax**2*RH + b7*Tmax*RH**2 + b8*Tmax**2*RH**2
    
    c0 = (HI>80.0)
    
    HI[c0] = B[c0]   
        
    c1 = ((Tmax>=80.0) & (Tmax<=112.0) & (RH <= 13.0))
    HI[c1] = B[c1] - ((13-RH[c1])/4)*(((17-abs(Tmax[c1]-95))/17)**0.5)        
    
    c2 = ((RH>85.0)&(Tmax>=80.0) &((Tmax<=87.0)))
    HI[c2] =  B[c2] + 0.02*(RH[c2] - 85) * (87 - Tmax[c2]) 
    
    c3 = (HI>141.17)
    
    HI[c3] = 141.17   # here When HI> 141.17, set it to 141.17
    
    WBGT = -0.0034*HI**2+0.96*HI-34  # use an empirical formula to estimate WBGT
    
    c4 = (WBGT<=0.0)
    
    WBGT[c4] = 0.001  # when WBGT<0, set value to 0.001

    return WBGT
 
# read all netCDF4(Tmax and RH) files' names in corresponding folder
Tmax_List = os.listdir('/mnt/data/luyin/WBGT/Tmax')
RH_List = os.listdir('/mnt/data/luyin/WBGT/rh')

#sort the files by name
Tmax_List = sorted(Tmax_List)
RH_List = sorted(RH_List)

# select every relevant timestep's Tmax and RH file
for T,Rh in zip(Tmax_List,RH_List):
    print('name:',T, flush=True)
    
    # use regular expression to get the starting and ending year for Tmax and RH files
    findyear1 = re.compile(r'\d\d\d\d')
    findyear2 = findyear1.findall(T)
    findyear2 = list(map(int,findyear2))
    
    # get the absolute path for Tmax and RH files
    tasmax_path = r'/mnt/data/luyin/WBGT/Tmax/'+T
    rh_path = r'/mnt/data/luyin/WBGT/rh/'+Rh

    print(tasmax_path, flush=True)
    print(rh_path, flush=True)
    print(findyear2, flush=True)
    
    # use absolute path that gotten from above to open corresponding files
    f1 = nc.Dataset(tasmax_path,'r')
    f2 = nc.Dataset(rh_path,'r')
    # read netCDF files which contain daily max temperature(F) and relative humidity(%) 
    
    lat = f1['lat'][:]
    lon = f1.variables['lon'][:]
    time = f1.variables['time']
    tax = f1.variables['tasmax'][:]
    hurs = f2['hurs'][:]
    print('It is fine up to now',flush=True )
    tax.astype('float32')
    hurs.astype('float32')
    nlat = len(lat)
    nlon = len(lon)
    
    
    # year_1 is starting year and year_2 is ending of every file
    year_1 = findyear2[0]
    year_2 = findyear2[1]
    leapyear = 0 
    
    print('OK',flush=True )
    
    # judge if it is a leap year
    for i in range(year_1,year_2+1) : 
        if (i % 4 == 0) and (i % 100 != 0 or i % 400 == 0):
            leapyear = leapyear +1
    
    # this i refers to number of days         
    i = 0
    print('Next step',flush=True )
    # create a matrix to contain WBGT data
    WBGT=[]
    
    # calculate the number of days for operation years
    nt = (year_2-year_1+1)*365+leapyear 
    
    # use a while loop to calculate the WBGT every day
    while i < nt:    
        
        WBGT.append(Wet_bulb_globe_temperature(tax[i,:,:],hurs[i,:,:])) 
        
        i = i +1
    print('last one',flush=True)    
    # delete some variables to make some space 
    del tax 
    del hurs 
    
    
    # create a WBGT file name based on Tmax name and make WBGT file's path   
    WBGT_name = T.replace('tasmax','WBGT')
    WBGT_path = '/mnt/data/luyin/WBGT/'+WBGT_name
    print(WBGT_path,flush=True)
    
    # create a WBGT database
    f3 = nc.Dataset(WBGT_path,'w',format=('NETCDF4'))
    
    # create dimensions
    f3.createDimension('time', None)
    f3.createDimension('lat', nlat)
    f3.createDimension('lon', nlon)
    
    # create variables
    _time = f3.createVariable('time', 'f4',('time'))
    _lat = f3.createVariable('lat', 'f4', ('lat'))
    _lon = f3.createVariable('lon', 'f4', ('lon'))
    _WBGT = f3.createVariable('WBGT', 'f4', ('time', 'lat', 'lon'), zlib=True)
    
    # give values and information to these variables
    _time.units = time.units
    _time.calendar = time.calendar
    
    _WBGT.units = 'Celsius'
    _WBGT.long_name = 'Wet bulb globe temperature'
    
    _lat[:] = lat
    _lon[:] = lon
    _WBGT[:] = WBGT
    _time[:] = time[:]
    
    f1.close()
    f2.close()
    f3.close()
    
    # delete vaiables to make some space for next loop
    del _WBGT  
    del WBGT

end = datetime.datetime.now()
# print the time that program takes
print(end-start)








