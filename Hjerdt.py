import os
import glob
import numpy as np
from osgeo import gdal
from tkinter import Tk
from tkinter.filedialog import askdirectory

'''
tan alphad = d / Ld 
où d = elevation (m) 
Ld = horizontal distance to the point with an elevation d meters below the elevation of the starting cell 
following the steepest-direction flow path
'''


def index_2d(data, search):
    for i, e in enumerate(data):
        try:
            return i, e.index(search)
        except ValueError:
            pass
    raise ValueError("{} is not in list".format(repr(search)))

def matrice_voisin(array, row, col, x, y):
    if x >= 1 and y >= 1 and x < (row - 1) and y < (col - 1):  # on ne considère pas les cellules en bordure
        # g = gauche c = centre d = droit
        # h = haut m = milieu b = bas

        cell_gh = array[x - 1][y - 1]  # todo remplacer dans la maitrce diff pour simplifier
        cell_gm = array[x][y - 1]
        cell_gb = array[x + 1][y - 1]
        cell_ch = array[x - 1][y]
        cell_cm = array[x][y]
        cell_cb = array[x + 1][y]
        cell_dh = array[x - 1][y + 1]
        cell_dm = array[x][y + 1]
        cell_db = array[x + 1][y + 1]

        matrice = [[cell_gh, cell_ch, cell_dh],
                   [cell_gm, cell_cm, cell_dm],
                   [cell_gb, cell_cb, cell_db]]

        return(matrice)

'''

            if i >= 1 and j >= 1 and i < (row - 1) and j < (col - 1):  # on ne considère pas les cellules en bordure
                # g = gauche c = centre d = droit
                # h = haut m = milieu b = bas
                print('cellule :', cell)
                cell_gh = array[i - 1][j - 1]  # todo remplacer dans la maitrce diff pour simplifier
                cell_gm = array[i][j - 1]
                cell_gb = array[i + 1][j - 1]
                cell_ch = array[i - 1][j]
                cell_cm = array[i][j]
                cell_cb = array[i + 1][j]
                cell_dh = array[i - 1][j + 1]
                cell_dm = array[i][j + 1]
                cell_db = array[i + 1][j + 1]

                matrice = [[cell_gh, cell_ch, cell_dh],
                           [cell_gm, cell_cm, cell_dm],
                           [cell_gb, cell_cb, cell_db]]

                print(matrice)
'''


def index_pour_calcul(array, d, row, col): #todo faire fonction a part pour trouver index pour le calcul
    '''
    :param array: MNT sous forme de matrice
    :param d: paramètre d (différence d'élévation) du calcul du Hjerdt
    :param nbrow: nombre de rangée de la matrice
    :param nbcol: nombre de colonne de la matrice
    :return: position x,y (rangée,  colonne) de la cellule ayant une difference de d # todo fonctionne pas comme retour si on veut avoir lD
    '''
    for i in range(row):
        for j in range(col):
            cell = array[i][j]
            print('cellule :', cell)

            matrice = matrice_voisin(array, row, col, i, j)
            print('matrice:', matrice)

            positionx = 0
            '''
            for k in matrice:
                for l in k:
                    if l == (cell - d):
                        positiony = k.index(l)
                        print('yes k ', positionx)
                        print('position: ', positiony)
                positionx += 1
            '''
    return(positionx, positiony)


def Hjerdt(array, d):
    '''
    :param array: MNT sous forme de matrice
    :param d: différence d'élévation à considérer pour le calcul du Hjerdt (paramètre d)
    :return: matrice résultante du calcul Hjerdt

    pseudo-code:
    pour chaque élément du MNT sous forme de matrice:
        trouver la cellule la plus près (donc Ld le plus faible) ayant une différence de d
        calculer le Ld
        mettre le Ld dans la matrice Ld

    pour tous les éléments de la matrice ld:
        calculer le Hdjert

    retourner la matrice Hjert
    '''
    Ld = [[]]
    nbrow = len(array)
    nbcol = len(array[0])

    print('array : ', array)
    index_pour_calcul(smallarray, 5, nbrow, nbcol)
    # print('size : ', nbrow, nbcol)

    # calcul = d/Ld


smallarray = [[9, 8, 5, 3],
              [5, 7, 6, 2],
              [1, 2, 6, 1]]
Hjerdt(smallarray, 5)
'''
def main():
    # source = r'C:/Users/caue3201/Downloads/Kingston/Kingston/'
    Tk().withdraw()
    #source = askdirectory(title=u"Sélectionner le dossier contenant les MNT")
    source = r'F:/Jonathan/APP_Jonathan/MNT/Kingston/'
    #sortie = askdirectory(title=u"Sélectionner le dossier pour les fichiers de sortie")
    listeMNT = glob.glob(source + 'dtm_2m_utm18_w_5_44.tif')

    for imgpath in listeMNT:
        filename = os.path.basename(imgpath)
        print(filename)
        #ds = gdal.Open(imgpath)
        #array = np.array(ds.GetRasterBand(1).ReadAsArray())
        #smallarray = array[555:556] todo il va falloir considérer la différence d en integer, pas float
        smallarray = [[9, 8, 5, 3],
                      [5, 7, 4, 2],
                      [1, 3, 6, 1]]
        Hjerdt(smallarray, 5)







        # print('Méthode D8 en cours...')
        # D8(source, filename, r'F:/Elizabeth/Production_IT/TWI_W/Kingston/D8/')
        # print('Méthode Dinf en cours...')
        # Dinf(source, filename, r'F:/Elizabeth/Production_IT/TWI_W/Kingston/Dinf/')
        # print('Méthode FD8 en cours...')
        # fD8(source, filename, r'F:/Elizabeth/Production_IT/TWI_W/Kingston/FD8/')


main()
'''
