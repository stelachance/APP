# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 12:15:52 2020
@author: caue3201
Références:
Kurtosis
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kurtosis.html
https://stackoverflow.com/questions/53024945/calculate-skewness-and-kurtosis
"""
import os
import csv
import glob
import numpy as np
from datetime import datetime
from osgeo import gdal
from scipy.stats import skew, kurtosis


# coucou

stats = [['name', 'maximum', 'minimum', 'moyenne', 'mediane', 'standdev', 'skewness', 'kurtosis', 'MAJ']]

path_input = [r'F:/Elizabeth/Production_IT/1m_resolution/TWI/NB/D8/',
              r'F:/Elizabeth/Production_IT/1m_resolution/TWI/NB/FD8/',
              r'F:/Elizabeth/Production_IT/1m_resolution/TWI/NB/Dinf/']

for path in path_input:
    listeIT = glob.glob(path + '*.tif', recursive=True)

    path_output = r'F:/Elizabeth/Analyse/1m/'

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
        arrayreshape = arrayIT.reshape(-1)
        skewness = skew(arrayreshape, nan_policy='omit')
        kur = kurtosis(arrayreshape, fisher=True, nan_policy='omit')
        date = datetime.now()
        readabledate = date.strftime("%c")

        info = [filename, maximum, minimum, moyenne, mediane, standdev, skewness, kur, readabledate]
        stats.append(info)

        del ds
        del arrayIT
        del kur


print(stats)
with open(path_output + 'NB_stats.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in stats:
            writer.writerow(row)
