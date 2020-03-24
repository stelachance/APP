import glob
import numpy as np
from osgeo import gdal
from scipy.stats import kurtosis

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kurtosis.html
#https://stackoverflow.com/questions/53024945/calculate-skewness-and-kurtosis




IT = r'C:/Users/Eliraptor/Downloads\dtm_1m_utm18_w_17_108.tif'
ds = gdal.Open(IT)

myarray = np.array(ds.GetRasterBand(1).ReadAsArray())

kur = kurtosis(myarray, fisher=True)
kur0 = kurtosis(myarray.reshape(-1), fisher=True)

print(kur)

print(kur0)