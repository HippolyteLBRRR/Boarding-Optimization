#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:36:29 2019

@author: labarrie
"""

import xlrd
from xlwt import Workbook

path=r"/home/labarrie/4A/Projet_avion/Boarding.xlsx"

classeur = Workbook()
wb = xlrd.open_workbook('Boarding_par_vol (2)(1).xlsx')
sh=wb.sheet_by_name('Grain Passager')

num_vol=1
num_ligne=0
feuille = classeur.add_sheet("Vol n°"+str(num_vol))
for rownum in range(2,sh.nrows):
        if (sh.row_values(rownum)[0]-sh.row_values(rownum-1)[0]) > 0.0 :
            num_vol+=1
            feuille = classeur.add_sheet("Vol n°"+str(num_vol))
            num_ligne=0
        feuille.write(num_ligne, 0, sh.row_values(rownum)[2])
        feuille.write(num_ligne, 1, sh.row_values(rownum)[3])
        feuille.write(num_ligne, 2, sh.row_values(rownum)[4])
        feuille.write(num_ligne, 3, sh.row_values(rownum)[5])
        num_ligne+=1

classeur.save(path)