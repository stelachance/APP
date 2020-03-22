# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 12:15:52 2020

@author: caue3201
"""
import os
import csv
import glob
import numpy as np
from datetime import datetime
from osgeo import gdal
from scipy.stats import skew

stats = [['name', 'maximum', 'minimum', 'moyenne', 'mediane', 'standdev', 'skewness', 'MAJ']]

path_input = [r'F:/Elizabeth/Production_IT/TWI_W/NB/D8/',
              r'F:/Elizabeth/Production_IT/TWI_W/NB/FD8/',
              r'F:/Elizabeth/Production_IT/TWI_W/NB/Dinf/']

for path in path_input:
    listeIT = glob.glob(path + '*.tif', recursive=True)

    path_output = r'F:/Elizabeth/Analyse/'

    for imgpath in listeIT:
        filename = os.path.basename(imgpath)
        print(filename)
        ds = gdal.Open(imgpath)
        arrayIT = np.array(ds.GetRasterBand(1).ReadAsArray())
        arrayIT[arrayIT < -100] = np.nan
        maximum = np.nanmax(arrayIT)
        minimum = np.nanmin(arrayIT)
        moyenne = np.nanmean(arrayIT)
        mediane = np.nanmedian(arrayIT)
        standdev = np.nanstd(arrayIT)
        skewness = np.mean(skew(arrayIT, axis=0, nan_policy='omit'))
        date = datetime.now()

        info = [filename, maximum, minimum, moyenne, mediane, standdev, skewness, date]
        stats.append(info)


print(stats)
with open(path_output + 'NB_stats.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in stats:
            writer.writerow(row)








