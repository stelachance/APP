import numpy as np
from osgeo import gdal
from scipy.stats import kurtosis

ds = gdal.Open(r'C:/Users/Eliraptor/Downloads/TWI_Dinf_CH_18_15w111.tif')

array = np.array(ds.GetRasterBand(1).ReadAsArray())

print(array.shape)
print(array.size)
print(array)