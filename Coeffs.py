#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:55:19 2019

@author: labarrie
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.stats
from random import *
import Model

def Find_coeff(order,P,NCOL,NROW1,NROW2,NROW,Time):
    N=len(order)
    err=np.zeros(N)
    h=3
    for i in range(N):
        err[i]=Model.TotalBoardingTime(order[i],P[i],NCOL[i],NROW1[i],NROW2[i],NROW[i])/60-Time[i]
    print(Norme(err))
    E=Norme(err)
    err0=err
    for i in range(1,100000):

        TWalk,TFollow,TLug,TWait,TRow,TInt= Model.TWalk,Model.TFollow,Model.TLug,Model.TWait,Model.TRow,Model.TInt      
        Model.TWalk,Model.TFollow,Model.TLug,Model.TWait,Model.TRow,Model.TInt=voisin(Model.TWalk,Model.TFollow,Model.TLug,Model.TWait,Model.TRow,Model.TInt)
        err=np.zeros(N)
        for i in range(N):
            err[i]=Model.TotalBoardingTime(order[i],P[i],NCOL[i],NROW1[i],NROW2[i],NROW[i])/60-Time[i]
        m=Norme(err)-Norme(err0)
        if (m>0):
            u=np.random.rand(1)
            if (u>=np.exp(-m/T(i,h))):
                Model.TWalk,Model.TFollow,Model.TLug,Model.TWait,Model.TRow,Model.TInt=TWalk,TFollow,TLug,TWait,TRow,TInt
            else:
                err0=err
        else:
            err0=err
        if (Norme(err)<E):
            E=Norme(err)
            print(Model.TWalk,Model.TFollow,Model.TLug,Model.TWait,Model.TRow,Model.TInt)
            print(E)
    print("TWalk = ",Model.TWalk)
    print("Tfollow =",Model.TFollow)
    print("TLug =",Model.TLug)
    print("TWait =",Model.TWait)
    print("TRow =",Model.TRow)
    print("TInt =",Model.TInt)
    print(Norme(err))
    pass

def voisin(TWalk,TFollow,TLug,TWait,TRow,TInt):
    TWalk2=np.maximum(TWalk+(random()-0.5)*0.5,1)
    TFollow2=np.maximum(TFollow+random()-0.5,3)
    TLug2=np.maximum(TLug+(random()-0.5)*0.5,3)
    TWait2=np.maximum(TWait+(random()-0.5)*0.5,0)
    TRow2=np.maximum(TRow+0.1*(random()-0.5),0)
    TInt2=np.maximum(TInt+0.1*(random()-0.5),0)
    return TWalk2,TFollow2,TLug2,TWait2,TRow2,TInt2

def Norme(err):
    return np.sqrt(np.sum(err**2))

def T(n,h):
    return h/np.log(n)
