#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:35:40 2019

@author: labarrie
"""

import xlrd

wb = xlrd.open_workbook('Boarding_par_vol.xlsx')
sh=wb.sheet_by_name('Rapport 1')

def find_rush(sh):
    nmax = 0
    debmax = 0
    finmax = 0
    N = 0
    deb=0
    for rownum in range(2,sh.nrows):
            if (sh.row_values(rownum)[1]-sh.row_values(rownum-1)[1]) < 2.0 :
                N = N+1
            else:
                if nmax<N:
                    nmax=N
                    finmax=rownum
                    debmax=rownum-N
                
                N=0
    return debmax,finmax

