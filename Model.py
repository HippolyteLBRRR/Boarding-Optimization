#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:32:13 2019

@author: labarrie
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.stats
from random import randint

NCOL=15
NROW1=2
NROW2=3
NROW=NROW1+NROW2

TWalk=2
TFollow=18
TLug=21
TWait=8
TRow=2
TInt=2

#TWalk=80
#TFollow=40
#TLug=60
#TWait=45
#TRow=6
#TInt=7
##Checkorder displays a graph based on the order which is the parameter.
##Good way to visualize how the boarding occurs
def Checkorder(order,NCOL,NROW1,NROW2,NROW):
    n=NCOL*NROW
    Vecorder=np.zeros(n)
    for i in range(len(order)):
        Vecorder[order[i]-1]=i+1
    Matorder=np.reshape(Vecorder,[NCOL,NROW]).T
    Output=np.zeros([NROW+1,NCOL])
    Output[:NROW1,:]=Matorder[:NROW1,:]
    Output[NROW1+1:,:]=Matorder[NROW1:,:]
    plt.matshow(Output,cmap="YlOrBr")
    plt.colorbar()
    plt.show()
    pass

##randomorder generates an random order of boarding
def randomorder(NCOL,NROW):
    N=NCOL*NROW
    order=np.linspace(1,N,N).tolist()
    for i in range(N):
        j=randint(1,N)
        temp=order[j-1]
        order[j-1]=order[i-1]
        order[i-1]=temp
    order=np.ravel(np.matrix(order,int))
    return order

##Info returns informations on the position of the sit i
def Info(i,NCOL,NROW1,NROW2,NROW):
    column=int((i-1)/NROW)
    row=(i-1)%NROW
    side=int(row>=NROW1)
    position=row*(row<NROW1)+(NROW-1-row)*(row>=NROW1)
    return column,row,side,position


def testInfo(i,NCOL,NROW1,NROW2,NROW):
    N=NCOL*NROW
    print("Place ",i)
    c,r,s,p=Info(i,NCOL,NROW1,NROW2,NROW)
    print("column ",c)
    print("row ",r)
    print("side ",s)
    print("position ",p)
    test=np.zeros(N)
    test[-1]=i
    test=np.ravel(np.matrix(test,int))
    Checkorder(test,NCOL,NROW1,NROW2,NROW)
    pass

def BoardingTime(i,j,P,NCOL,NROW1,NROW2,NROW):
    #2 sec between two passengers
    c1,r1,s1,p1=Info(i,NCOL,NROW1,NROW2,NROW)
    c2,r2,s2,p2=Info(j,NCOL,NROW1,NROW2,NROW)
    if (c1>c2):
        T=NormalTime(j,P,NCOL,NROW1,NROW2,NROW)-NormalTime(i,P,NCOL,NROW1,NROW2,NROW)+TFollow
    if (c1<=c2):
        T=TLug+(c2-c1)*TWalk+Interaction(j,P,NCOL,NROW1,NROW2,NROW)-Interaction(i,P,NCOL,NROW1,NROW2,NROW)+Wait(j,P,NCOL,NROW1,NROW2,NROW)
    return T

def NormalTime(i,P,NCOL,NROW1,NROW2,NROW):
    #4 sec/column
    #20 sec to put the luggage
    c,r,s,p=Info(i,NCOL,NROW1,NROW2,NROW)
    t=TWalk*(c+1)+TLug+Interaction(i,P,NCOL,NROW1,NROW2,NROW)+Wait(i,P,NCOL,NROW1,NROW2,NROW)
    return t

def TotalBoardingTime(order,P,NCOL,NROW1,NROW2,NROW):
    T=NormalTime(order[0],P,NCOL,NROW1,NROW2,NROW)
    for i in range(len(order)-1):
        P=SetPassenger(order[i],P,NCOL,NROW1,NROW2,NROW)
        T+=BoardingTime(order[i],order[i+1],P,NCOL,NROW1,NROW2,NROW)
    return T

def SetPassenger(i,P,NCOL,NROW1,NROW2,NROW):
    c,r,s,p=Info(i,NCOL,NROW1,NROW2,NROW)
    P2=np.copy(P)
    P2[r,c]=1
    return P2

def Interaction(I,P,NCOL,NROW1,NROW2,NROW):
    c,r,s,p=Info(I,NCOL,NROW1,NROW2,NROW)
    j=(s==0)*NROW1+(s==1)*NROW2-1
    k=1
    T=TRow
    while (j!=p):
       if s==0:
           T=T+TRow+P[r+k,c]*TInt
       else:
           T=T+TRow+P[r-k,c]*TInt
       j-=1
       k+=1
    return T

def Wait(I,P,NCOL,NROW1,NROW2,NROW):
    c,r,s,p=Info(I,NCOL,NROW1,NROW2,NROW)
    j=(s==0)*NROW1+(s==1)*NROW2-1
    k=1
    T=0
    while (j!=p):
       if s==0:
           T+=P[r+k,c]
       else:
           T+=P[r-k,c]
       j-=1
       k+=1
    
    return TWait*int(T!=0)

def neighbour(order):
    N=len(order)
    order2=np.copy(order)
    u1=int(np.random.rand(1)*N)
    u2=int(np.random.rand(1)*N)
    while (u1==u2):
        u2=int(np.random.rand(1)*N)
    order2[u1]=order[u2]
    order2[u2]=order[u1]
    return order2

def Row(i,NCOL,NROW1,NROW2,NROW):
    R=np.linspace(0,NROW*(NCOL-1),NCOL)+i+1
    return np.flip(R)



def Outsidein(NCOL,NROW1,NROW2,NROW):
    N=NCOL*NROW
    order=np.zeros(N)
    for i in range(NROW1):
        order[i*NCOL:(i+1)*NCOL]=Row(i)
    for j in range(NROW2):
        order[NCOL*NROW1+j*NCOL:NCOL*NROW1+(j+1)*NCOL]=Row(NROW-j-1)
    order=np.ravel(np.matrix(order,int))
    return order

def Boeing(NCOL,NROW1,NROW2,NROW):
    N=NCOL*NROW
    order=np.linspace(3,N,N-2).tolist()
    order[0:3]=[1,2,3]
    for i in range(N-2):
        j=randint(1,N-2)
        temp=order[j-1]
        order[j-1]=order[i-1]
        order[i-1]=temp
    order=np.ravel(np.matrix(order,int))
    return order

def BoeingOI(NCOL,NROW1,NROW2,NROW):
    N=NCOL*NROW
    order=np.zeros(N-2)
    for i in range(NROW1):
        order[i*NCOL:(i+1)*NCOL]=Row(i,NCOL,NROW1,NROW2,NROW)
    for j in range(NROW2):
        R=Row(NROW-j-1,NCOL,NROW1,NROW2,NROW)[:-1]
        order[NCOL*NROW1+j*(NCOL-1):NCOL*NROW1+(j+1)*(NCOL-1)]=R
    order=np.ravel(np.matrix(order,int))
    return order

def T(n,h):
    return h/np.log(n)

def Metropolis(order,P,NCOL,NROW1,NROW2,NROW,nT,h):
    Checkorder(order,NCOL,NROW1,NROW2,NROW)
    print("Total Boarding Time : ",TotalBoardingTime(order,P,NCOL,NROW1,NROW2,NROW))
    
    n=2
    ordermin=order
    Checkorder(order,NCOL,NROW1,NROW2,NROW)
    print(TotalBoardingTime(order,P,NCOL,NROW1,NROW2,NROW))
#    F[0]=TotalBoardingTime(order)
    while (n<nT):
        o=np.copy(neighbour(order))
        m=TotalBoardingTime(o,P,NCOL,NROW1,NROW2,NROW)-TotalBoardingTime(order,P,NCOL,NROW1,NROW2,NROW)
        if (m<0):
            order=np.copy(o)
        else:
            u=np.random.rand(1)
            if (u<np.exp(-m/T(n,h))):
                order=np.copy(o)
    #    F[n-2]=distancetotale(X,Y,sig)
        n+=1
        if (TotalBoardingTime(order,P,NCOL,NROW1,NROW2,NROW)<TotalBoardingTime(ordermin,P,NCOL,NROW1,NROW2,NROW)):
            ordermin=order
        if (n%1000==0):
            Checkorder(order,NCOL,NROW1,NROW2,NROW)
            print(TotalBoardingTime(order,P,NCOL,NROW1,NROW2,NROW))
            print("Optimal boarding :")
            Checkorder(ordermin,NCOL,NROW1,NROW2,NROW)
            print(TotalBoardingTime(ordermin,P,NCOL,NROW1,NROW2,NROW))
#        F[n-2]=TotalBoardingTime(order)
    
    Checkorder(order,NCOL,NROW1,NROW2,NROW)
    print(TotalBoardingTime(order,P,NCOL,NROW1,NROW2,NROW))
    print("Température finale :",T(n,h))
    
    Checkorder(ordermin,NCOL,NROW1,NROW2,NROW)
    print(TotalBoardingTime(ordermin,P,NCOL,NROW1,NROW2,NROW))
    return ordermin

#P=np.zeros([NROW,NCOL])
#r=np.ravel(np.matrix(order,int))
#Checkorder(r)
#print(TotalBoardingTime(r,P))
#
#N=50000
#F=np.zeros(N-1)
#r=Metropolis(Boeing,N,20)
#plt.plot(F)
#r=Outsidein()
#Checkorder(r)
#print(TotalBoardingTime(r))
