#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 09:33:45 2019

@author: labarrie
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.stats
from random import randint

NCOL=16
NROW=6


TWalk=2
TFollow=2
TLug=12
TWait=6
TRow=2
TInt=3

def Checkorder(order):
    n=len(order)
    Vecorder=np.zeros(n)
    NROW1=int(NROW/2)
    for i in range(n):
        Vecorder[order[i]-1]=i+1
#    Matorder=np.reshape(Vecorder,[NCOL,NROW]).T
    Matorder=np.reshape(Vecorder,[NCOL,NROW]).T
    Output=np.zeros([NROW+1,NCOL])
    Output[:NROW1,:]=Matorder[:NROW1,:]
    Output[NROW1+1:,:]=Matorder[NROW1:,:]
    plt.matshow(Output.T,cmap="YlOrBr")
    plt.colorbar()
    plt.show()
#    plt.matshow(Matorder,cmap="YlOrBr")
#    plt.colorbar()
#    plt.show()
    pass

def randomorder():
    N=NCOL*NROW
    order=np.linspace(1,N,N).tolist()
    for i in range(N):
        j=randint(1,N)
        temp=order[j-1]
        order[j-1]=order[i-1]
        order[i-1]=temp
    order=np.ravel(np.matrix(order,int))
    return order

def Info(i):
    column=int((i-1)/NROW)
    row=(i-1)%NROW
    side=int(row>=(NROW/2))
    position=row*(row<(NROW/2))+(NROW-1-row)*(row>=(NROW/2))
    return column,row,side,position

def testInfo(i):
    N=NCOL*NROW
    print("Place ",i)
    c,r,s,p=Info(i)
    print("column ",c)
    print("row ",r)
    print("side ",s)
    print("position ",p)
    test=np.zeros(N)
    test[-1]=i
    test=np.ravel(np.matrix(test,int))
#    for j in range(N):
#        test[j]=math.floor(test[j])
    print(test)
    Checkorder(test)
    pass

def BoardingTime(i,j,P):
    #2 sec between two passengers
    c1,r1,s1,p1=Info(i)
    c2,r2,s2,p2=Info(j)
    if (c1>c2):
        T=NormalTime(j,P)-NormalTime(i,P)+TFollow
    if (c1<=c2):
        T=TLug+(c2-c1)*TWalk+Interaction(j,P)-Interaction(i,P)+Wait(j,P)
    return T

def NormalTime(i,P):
    #4 sec/column
    #20 sec to put the luggage
    c,r,s,p=Info(i)
    t=TWalk*(c+1)+TLug+Interaction(i,P)+Wait(i,P)
    return t

def TotalBoardingTime(order):
    N=NCOL*NROW
    P=np.zeros([NROW,NCOL])
    T=NormalTime(order[0],P)
    for i in range(N-1):
        P=SetPassenger(order[i],P)
        T+=BoardingTime(order[i],order[i+1],P)
    return T

def SetPassenger(i,P):
    c,r,s,p=Info(i)
    P2=np.copy(P)
    P2[r,c]=1
    return P2

def Interaction(I,P):

    c,r,s,p=Info(I)
    j=NROW/2-1
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

def Wait(I,P):
    c,r,s,p=Info(I)
    j=NROW/2-1
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

def randomize(o):
    N=len(o)
    order=np.copy(o)
    for i in range(N):
        j=randint(1,N)
        temp=order[j-1]
        order[j-1]=order[i-1]
        order[i-1]=temp
    order=np.ravel(np.matrix(order,int))
    return order

def Byrow():
    N=NCOL*NROW
    order=np.flip(np.linspace(1,N,N))
    for i in range(NCOL):
        order[i*NROW:(i+1)*NROW]=randomize(order[i*NROW:(i+1)*NROW])
    order=np.ravel(np.matrix(order,int))
    return order
    
def Byhalfrow():
    N=NCOL*6
    ROW=int(NROW/2)
    order=np.zeros(N)
    for i in range(NCOL):
        order[i*3:i*3+3]=np.linspace(i*6+1,i*6+3,3)
    order[(NCOL)*3:]=order[:(NCOL)*3]+3
    for i in range(NCOL*2):
        order[i*ROW:(i+1)*ROW]=randomize(order[i*ROW:(i+1)*ROW])
    order=np.ravel(np.matrix(order,int))
    return np.flip(order)

def Outsidein():
#    N=NCOL*6
#    order=np.zeros(N)
#    for i in range(NCOL):
#        order[i]=i*6+1
#    order[:NCOL]=np.flip(order[:NCOL])
#    order[NCOL:2*NCOL]=order[:NCOL]+5
#    order[2*NCOL:3*NCOL]=order[:NCOL]+1
#    order[3*NCOL:4*NCOL]=order[:NCOL]+4
#    order[4*NCOL:5*NCOL]=order[:NCOL]+2
#    order[5*NCOL:6*NCOL]=order[:NCOL]+3
#    order=np.ravel(np.matrix(order,int))
    
    N=NCOL*NROW
    order=np.zeros(N)
    for i in range(NCOL):
        order[i]=i*NROW+1
    order[:NCOL]=np.flip(order[:NCOL])
    for j in range(int(NROW/2)):
        if (j!=0):
            order[(2*j)*NCOL:(2*j+1)*NCOL]=order[:NCOL]+j
        order[(2*j+1)*NCOL:(2*j+2)*NCOL]=order[:NCOL]+NROW-1-j
#    order[NCOL:2*NCOL]=order[:NCOL]+5
#    order[2*NCOL:3*NCOL]=order[:NCOL]+1
#    order[3*NCOL:4*NCOL]=order[:NCOL]+4
#    order[4*NCOL:5*NCOL]=order[:NCOL]+2
#    order[5*NCOL:6*NCOL]=order[:NCOL]+3
    for i in range(int(NROW/2)):
        order[2*i*NCOL:2*(i+1)*NCOL]=randomize(order[2*i*NCOL:2*(i+1)*NCOL])
    order=np.ravel(np.matrix(order,int))
    return order

def Backtofront():
    N=NCOL*6
    COL=int(NCOL/4)
    order=np.zeros(N)
    for i in range(COL):
        order[i]=i*6+1
    order[:COL]=(order[:COL])+2
    order[COL:2*COL]=order[:COL]+1
    order[2*COL:3*COL]=order[:COL]-1
    order[3*COL:4*COL]=order[:COL]+2
    order[4*COL:5*COL]=order[:COL]-2
    order[5*COL:6*COL]=order[:COL]+3
    for j in range(3):
        order[(j+1)*6*COL:(j+2)*6*COL]=COL*6*(j+1)+order[:6*COL]
    for i in range(4):
        order[6*i*COL:6*(i+1)*COL]=randomize(order[6*i*COL:6*(i+1)*COL])
    order=np.ravel(np.matrix(order,int))
    return np.flip(order)

def T(n,h):
    return h/np.log(n)
    

def Calculh():
    order=randomorder()
    max=0
    for i in range(10000):
        o=np.copy(neighbour(order))
        m=TotalBoardingTime(order)-TotalBoardingTime(o)
        if m>max:
            max=m
        order=o
    return max
    
    
#N=32*6
#order=(np.linspace(1,N,N))
#order=np.ravel(np.matrix(order,int))
#testInfo(61)
    
def Metropolis(funcorder,nT,h):
    order=funcorder()
    Checkorder(order)
    print("Total Boarding Time : ",TotalBoardingTime(order))
    
    n=2
    order=randomorder()
    ordermin=order
    Checkorder(order)
    print(TotalBoardingTime(order))
    F[0]=TotalBoardingTime(order)
    while (n<nT):
        o=np.copy(neighbour(order))
        m=TotalBoardingTime(o)-TotalBoardingTime(order)
        if (m<0):
            order=np.copy(o)
        else:
            u=np.random.rand(1)
            if (u<np.exp(-m/T(n,h))):
                order=np.copy(o)
    #    F[n-2]=distancetotale(X,Y,sig)
        n+=1
        if (TotalBoardingTime(order)<TotalBoardingTime(ordermin)):
            ordermin=order
        if (n%1000==0):
            Checkorder(order)
            print(TotalBoardingTime(order))
            print("Optimal boarding :")
            Checkorder(ordermin)
            print(TotalBoardingTime(ordermin))
        F[n-2]=TotalBoardingTime(order)
    
    Checkorder(order)
    print(TotalBoardingTime(order))
    print("Température finale :",T(n,h))
    
    Checkorder(ordermin)
    print(TotalBoardingTime(ordermin))
    return ordermin



#print("==============================================================")
#print("Outside-in boarding :")
#r=Outsidein()
#Checkorder(r)
#print("Estimated boarding time:",TotalBoardingTime(r))
#print("==============================================================")
#print("Random boarding :")
#r=randomorder()
#Checkorder(r)
#print("Estimated boarding time:",TotalBoardingTime(r))
#print("==============================================================")
#print("Boarding by row :")
#r=Byrow()
#Checkorder(r)
#print("Estimated boarding time:",TotalBoardingTime(r))
#print("==============================================================")
#print("Boarding by half row :")
#r=Byhalfrow()
#Checkorder(r)
#print("Estimated boarding time:",TotalBoardingTime(r))
#print("==============================================================")
#print("Back to front boarding :")
#r=Backtofront()
#Checkorder(r)
#print("Estimated boarding time:",TotalBoardingTime(r))

#N=1000
##TL=[2,8,14,20]
#TW=np.linspace(0,20,10)
#J=len(TW)
#TOI=np.zeros(J)
#TR=np.zeros(J)
#TBTF=np.zeros(J)
#TBR=np.zeros(J)
#TBHR=np.zeros(J)
#for j in range(J):
#    TWait=TW[j]
#    TimeOI=0
#    TimeRandom=0
#    TimeBtF=0
#    TimeBR=0
#    TimeBHR=0
#    for i in range(N):
#        r=Outsidein()
#        TimeOI+=TotalBoardingTime(r)
#        r=randomorder()
#        TimeRandom+=TotalBoardingTime(r)
#        r=Backtofront()
#        TimeBtF+=TotalBoardingTime(r)
#        r=Byrow()
#        TimeBR+=TotalBoardingTime(r)
#        r=Byhalfrow()
#        TimeBHR+=TotalBoardingTime(r)
#    TimeOI=TimeOI/N
#    TimeRandom=TimeRandom/N
#    TimeBtF=TimeBtF/N
#    TimeBR=TimeBR/N
#    TimeBHR=TimeBHR/N
#    print("==========================================")
#    print("Tlug =",TLug)
#    print("Temps moyen Outside in :",TimeOI)
#    print("Temps moyen random :",TimeRandom)
#    print("Temps moyen Back to Front :",TimeBtF)
#    print("Temps moyen By row:",TimeBR)
#    print("Temps moyen By half row :",TimeBHR)
#    TOI[j]=TimeOI
#    TR[j]=TimeRandom
#    TBTF[j]=TimeBtF
#    TBR[j]=TimeBR
#    TBHR[j]=TimeBHR
#    
#plt.plot(TW,TOI)
#plt.plot(TW,TR)
#plt.plot(TW,TBTF)
#plt.plot(TW,TBR)
#plt.plot(TW,TBHR)
#plt.legend(["Outside-in","Random","Back to front","By row","By half row"])
#plt.show()

N=1000
#TL=[2,8,14,20]
TL=np.linspace(0,30,10)
J=len(TL)
TOI=np.zeros(J)
TR=np.zeros(J)
TBTF=np.zeros(J)
TBR=np.zeros(J)
TBHR=np.zeros(J)
for j in range(J):
    TWalk=TL[j]
    TimeOI=0
    TimeRandom=0
    TimeBtF=0
    TimeBR=0
    TimeBHR=0
    for i in range(N):
        r=Outsidein()
        TimeOI+=TotalBoardingTime(r)
        r=randomorder()
        TimeRandom+=TotalBoardingTime(r)
        r=Backtofront()
        TimeBtF+=TotalBoardingTime(r)
        r=Byrow()
        TimeBR+=TotalBoardingTime(r)
        r=Byhalfrow()
        TimeBHR+=TotalBoardingTime(r)
    TimeOI=TimeOI/N
    TimeRandom=TimeRandom/N
    TimeBtF=TimeBtF/N
    TimeBR=TimeBR/N
    TimeBHR=TimeBHR/N
    print("==========================================")
    print("Tlug =",TLug)
    print("Temps moyen Outside in :",TimeOI)
    print("Temps moyen random :",TimeRandom)
    print("Temps moyen Back to Front :",TimeBtF)
    print("Temps moyen By row:",TimeBR)
    print("Temps moyen By half row :",TimeBHR)
    TOI[j]=TimeOI
    TR[j]=TimeRandom
    TBTF[j]=TimeBtF
    TBR[j]=TimeBR
    TBHR[j]=TimeBHR
    
plt.plot(TL,TOI)
plt.plot(TL,TR)
plt.plot(TL,TBTF)
plt.plot(TL,TBR)
plt.plot(TL,TBHR)
plt.legend(["Outside-in","Random","Back to front","By row","By half row"])
plt.show()




#print(Calculh())
#N=50000
#F=np.zeros(N-1)
#r=Metropolis(randomorder,N,20)
#plt.plot(F)

#plt.plot(t,F)
#plt.show()

#r=[3,4,2,5,1,6]
#Checkorder(r)
#print(TotalBoardingTime(r))
#r=neighbour(r)
#Checkorder(r)
#print(TotalBoardingTime(r))
