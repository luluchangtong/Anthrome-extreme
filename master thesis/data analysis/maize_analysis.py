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


Temperature_maize = [35,36,37,38,39,40]

crop_path = r'/mnt/data/luyin/Dataprocess/Frequency_crop/GCMs_mean/maize'
All_files = os.listdir(crop_path)






