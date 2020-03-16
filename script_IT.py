# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 12:36:29 2019

@author: caue3201
"""

#importation des librairies
import whitebox
import glob
#from tkinter import Tk
#from tkinter.filedialog import askdirectory
import os
from shutil import copyfile

# =============================================================================
# Indice de Hjerdt: 
#   We propose a new way of estimating the hydraulic gradient by calculating how
#   far downhill (Ld, [m]) a parcel of water must move in order to lose a certain
#   amount of potential energy (d, [m]). Expressed as a gradient, tanad = d/Ld, 
#   values tend to be lower on concave slope profiles and higher on convex slope 
#   profiles compared with the local gradient, tanb.


# Suite à la lecture de l'article: 
# faudrait lire les amélioration de tarboton 1997 et woods et al 1997

# Grayson et Western 2001 on vu que many hydrologic processes that drive the 
# wetness distribution may be controlled by other factors not captured by the index

# Rodhe and Seibert [1999] found that local topographic slope alone was a better 
# predictor of wet areas than the ln(a/tanb) index

# Theoretically, the ln(a/tanb) index makes the assumption that local drainage is
# not affected by downslope conditions. However, Speight [1980] argued that it is
# the balance between the specific catchment area (upslope contributing area per 
# unit length of contour) and the specific dispersal area (downslope area per unit 
# length of contour) that controls the drainage of water from any location

# Many common hydrologic models use land surface slope as a substitute for the slope of 
# the groundwater table and hydraulic gradients. In strongly convex or concave terrain
# , however, hydraulic gradients may also be influenced by drainage conditions downslope
# of the immediate area around the point of consideration

#The downslope value can be reported either as a distance Ld or as a grandiant tandalphad 
#où tan_alpha_d = d/ ld where ld is the horizontal distance to the point with an elevation d beters
# below the elevation of the starting cell, follining the steepest direction flow path.  

#Reasonable values ofdare assessed on thebasis of topographic relief, resolution of the DEM used, 
#and local soil transmissivity. We illustrate the effects of varyingthedvalue for a given 
#DEM in section 3.

# tester tan alpha à 5m, 10m et 25 m 

# =============================================================================


# https://github.com/jblindsay/whitebox-tools/blob/master/manual/WhiteboxToolsManual.md
wbt = whitebox.WhiteboxTools()


def D8(dossier, img, directory):
    wbt.set_working_dir(directory)
    wbt.verbose = False
    
    imgpath = dossier + img
    copyfile(imgpath, directory+img)
    imgFile = os.path.splitext(img)[0]
    imgName = imgFile[4:]
    wbt.breach_depressions(img, "D8_"+imgName+"_breached.tif")
    wbt.slope(img, "D8_"+imgName+"_slope.tif")
    wbt.d8_flow_accumulation("D8_"+imgName+"_breached.tif", "D8_"+imgName+"flow_acc.tif", 'specific contributing area')
        
    wbt.wetness_index("D8_"+imgName+"flow_acc.tif", "D8_"+imgName+"_slope.tif", "TWI_D8_"+imgName+".tif")
    os.remove(directory + img)
    os.remove(directory + "D8_"+imgName+"_slope.tif")
    os.remove(directory + "D8_"+imgName+"_breached.tif")
    os.remove(directory + "D8_"+imgName+"flow_acc.tif")
   
    
def Dinf(dossier, img, directory):
    wbt.set_working_dir(directory)
    wbt.verbose = False
    
    imgpath = dossier + img
    copyfile(imgpath, directory+img)
    
    imgFile = os.path.splitext(img)[0]
    imgName = imgFile[4:]
    
    wbt.breach_depressions(img, "D8_"+imgName+"_breached.tif")
    wbt.slope(img, "D8_"+imgName+"_slope.tif")
    wbt.d_inf_flow_accumulation("D8_"+imgName+"_breached.tif", "Dinf_"+imgName+"flow_acc.tif", 'specific contributing area')
    wbt.wetness_index("Dinf_"+imgName+"flow_acc.tif", "D8_"+imgName+"_slope.tif", "TWI_Dinf_"+imgName+".tif")
    os.remove(directory + img)
    os.remove(directory + "D8_"+imgName+"_slope.tif")
    os.remove(directory + "D8_"+imgName+"_breached.tif")
    os.remove(directory + "Dinf_"+imgName+"flow_acc.tif")

    

def fD8(dossier, img, directory):
    wbt.set_working_dir(directory)
    wbt.verbose = False
    
    imgpath = dossier + img
    copyfile(imgpath, directory+img)
    
    imgFile = os.path.splitext(img)[0]
    imgName = imgFile[4:]
    
    wbt.breach_depressions(img, "D8_"+imgName+"_breached.tif")
    wbt.slope(img, "D8_"+imgName+"_slope.tif")
    wbt.d_inf_flow_accumulation("D8_"+imgName+"_breached.tif", "FD8_"+imgName+"flow_acc.tif", 'specific contributing area')
    wbt.wetness_index("FD8_"+imgName+"flow_acc.tif", "D8_"+imgName+"_slope.tif", "TWI_FD8_"+imgName+".tif")
    os.remove(directory + img)
    os.remove(directory + "D8_"+imgName+"_slope.tif")
    os.remove(directory + "D8_"+imgName+"_breached.tif")
    os.remove(directory + "FD8_"+imgName+"flow_acc.tif")
    

    


def main():
    dossier = r'F:/Jonathan/APP_Jonathan/MNT/Reproj/Chapeau/'
    #dossier = r'G:/Hiv2020/APPJO/MNT/TEST/'
    listeMNT = glob.glob(dossier + '*.tif')

    for imgpath in listeMNT:
        filename = os.path.basename(imgpath)
        print(filename)
        
        print('Méthode D8 en cours...')
        D8(dossier, filename, r'F:/Elizabeth/Production_IT/1m_resolution/TWI/Chapeau/D8/')
        # print('Méthode Dinf en cours...')
        Dinf(dossier, filename, r'F:/Elizabeth/Production_IT/1m_resolution/TWI/Chapeau/Dinf/')
        # print('Méthode FD8 en cours...')
        fD8(dossier, filename, r'F:/Elizabeth/Production_IT/1m_resolution/TWI/Chapeau/FD8/')

main()

