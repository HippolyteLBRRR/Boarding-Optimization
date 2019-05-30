#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:32:39 2019

@author: labarrie
"""
import numpy as np
import matplotlib.pyplot as plt
import math
import xlrd
import Rush
import Model
import Coeffs


def Data_translater(file_name,sheet_name,weight,display):
    wb = xlrd.open_workbook(file_name)
    sh=wb.sheet_by_name(sheet_name)
    d,f=Rush.find_rush(sh)
    order1=[]
    order2=[]
    order3=[]
    order4=[]
    order5=[]
    order6=[]
    deb1=0
    fin1=0
    deb2=0
    fin2=0
    deb3=0
    fin3=0
    deb4=0
    fin4=0
    deb5=0
    fin5=0
    deb6=0
    fin6=0
    P1=np.zeros([5,18])
    P2=np.zeros([5,18])
    P3=np.zeros([5,15])
    P4=np.zeros([5,15])
    P5=np.zeros([5,14])
    P6=np.zeros([5,14])
    [NC1,NR11,NR21,NR1]=[18,3,2,5]
    [NC2,NR12,NR22,NR2]=[18,2,3,5]
    [NC3,NR13,NR23,NR3]=[15,3,2,5]
    [NC4,NR14,NR24,NR4]=[15,2,3,5]
    [NC5,NR15,NR25,NR5]=[14,3,2,5]
    [NC6,NR16,NR26,NR6]=[14,2,3,5]
    for rownum in range(sh.nrows):
#        print(rownum)
        if (rownum==d):
            DEB=sh.row_values(rownum)[1]
        if (rownum<=f):
            FIN=sh.row_values(rownum)[1]
        col=(ord(sh.row_values(rownum)[3][0])-48)*10+ord(sh.row_values(rownum)[3][1])-48
        row=ord(sh.row_values(rownum)[3][2])-65
        if (col>9) and (col<28) and (row<6):
            p=(27-col)*5+row-1*(row>3)+1
            if (rownum<d):
                P1=Model.SetPassenger(p,P1,NC1,NR11,NR21,NR1)
            if (rownum>=d) and (rownum<=f):
                if (deb1==0):
                    deb1=sh.row_values(rownum)[1]
                order1+=[p]
                fin1=sh.row_values(rownum)[1]
        if (col>9) and (col<28) and (row>5):
            p=(27-col)*5+row-5-1*(row>8)
            if (rownum<d):
                P2=Model.SetPassenger(p,P2,NC2,NR12,NR22,NR2)
            if (rownum>=d) and (rownum<=f):
                if (deb2==0):
                    deb2=sh.row_values(rownum)[1]
                order2+=[p]
                fin2=sh.row_values(rownum)[1]
        if (col>28) and (col<45) and (row<6):
            p=(44-col)*5+row-1*(row>3)+1
            if (rownum<d):
                P3=Model.SetPassenger(p,P3,NC3,NR13,NR23,NR3)
            if (rownum>=d) and (rownum<=f):
                if (deb3==0):
                    deb3=sh.row_values(rownum)[1]
                order3+=[p]
                fin3=sh.row_values(rownum)[1]
        if (col>28) and (col<45) and (row>5):
            p=(44-col)*5+row-5-1*(row>8)
            if (rownum<d):
                P4=Model.SetPassenger(p,P4,NC4,NR14,NR24,NR4)
            if (rownum>=d) and (rownum<=f):
                if (deb4==0):
                    deb4=sh.row_values(rownum)[1]
                order4+=[p]
                fin4=sh.row_values(rownum)[1]
        if (col>45) and (col<59) and (row<6):
            p=(58-col)*5+row-1*(row>3)+1
            if (rownum<d):
                P5=Model.SetPassenger(p,P5,NC5,NR15,NR25,NR5)
            if (rownum>=d) and (rownum<=f):
                if (deb5==0):
                    deb5=sh.row_values(rownum)[1]
                order5+=[p]
                fin5=sh.row_values(rownum)[1]
        if (col>45) and (col<59) and (row>5):
            p=(58-col)*5+row-5-1*(row>8)
            if (rownum<d):
                P6=Model.SetPassenger(p,P6,NC6,NR16,NR26,NR6)
            if (rownum>=d) and (rownum<=f):
                if (deb6==0):
                    deb6=sh.row_values(rownum)[1]
                order6+=[p]
                fin6=sh.row_values(rownum)[1]
    BTime=FIN-DEB
    
    if display == True :
        print("=============================================")
        print("                  BLOC 1")
        print("=============================================")
        Model.Checkorder(order1,NC1,NR11,NR21,NR1)
        BT1=Model.TotalBoardingTime(order1,P1,NC1,NR11,NR21,NR1)
        print("Temps calculé :",BT1/60)
        print("Temps réel :",fin1-deb1)
        print("=============================================")
        print("                  BLOC 2")
        print("=============================================")
        Model.Checkorder(order2,NC2,NR12,NR22,NR2)
        BT2=Model.TotalBoardingTime(order2,P2,NC2,NR12,NR22,NR2)
        print("Temps calculé :",BT2/60)
        print("Temps réel :",fin2-deb2)
        print("=============================================")
        print("                  BLOC 3")
        print("=============================================")
        Model.Checkorder(order3,NC3,NR13,NR23,NR3)
        BT3=Model.TotalBoardingTime(order3,P3,NC3,NR13,NR23,NR3)
        print("Temps calculé :",BT3/60)
        print("Temps réel :",fin3-deb3)
        print("=============================================")
        print("                  BLOC 4")
        print("=============================================")
        Model.Checkorder(order4,NC4,NR14,NR24,NR4)
        BT4=Model.TotalBoardingTime(order4,P4,NC4,NR14,NR24,NR4)
        print("Temps calculé :",BT4/60)
        print("Temps réel :",fin4-deb4)
        print("=============================================")
        print("                  BLOC 5")
        print("=============================================")
        Model.Checkorder(order5,NC5,NR15,NR25,NR5)
        BT5=Model.TotalBoardingTime(order5,P5,NC5,NR15,NR25,NR5)
        print("Temps calculé :",BT5/60)
        print("Temps réel :",fin5-deb5)
        print("=============================================")
        print("                  BLOC 6")
        print("=============================================")
        Model.Checkorder(order6,NC6,NR16,NR26,NR6)
        BT6=Model.TotalBoardingTime(order6,P6,NC6,NR16,NR26,NR6)
        print("Temps calculé :",BT6/60)
        print("Temps réel :",fin6-deb6)
        print("=============================================")
        print("Temps total d'embarquement :",BTime)
        if (np.sum(weight)==0):
            weight[np.argmax([BT1/60,BT2/60,BT3/60,BT4/60,BT5/60,BT6/60])]=1
        print("Temps total d'embarquement calculé :",np.dot([BT1/60,BT2/60,BT3/60,BT4/60,BT5/60,BT6/60],weight))
    ORDER=[order1,order2,order3,order4,order5,order6]
    P=[P1,P2,P3,P4,P5,P6]
    NC=[18,18,15,15,14,14]
    NR1=[3,2,3,2,3,2]
    NR2=[2,3,2,3,2,3]
    NR=[5,5,5,5,5,5]
    Time=[fin1-deb1,fin2-deb2,fin3-deb3,fin4-deb4,fin5-deb5,fin6-deb6]
    return ORDER,P,NC,NR1,NR2,NR,Time,BTime

def weight_finder():
    Time,BTime=Data_translater('Boarding.xlsx','Vol n°1',np.zeros(6),False)[-2:]
    BTime=[BTime]
    Time=np.matrix(Time)
    k=0
    for i in range(2,87):
#We choose the only flights which have the good format
        if (i!=18 and i!=3 and i!=6 and i!=7 and i!=10 and i!=11 and i!=14 and i!=15 and i!=19 and i!=21 and i!=23 and i!=27 and i!=30 and i!=31 and i!=33 and i!=35 and i!=39 and i!=43 and i!=47 and i!=51 and i!=55 and i!=57 and i!=59 and i!=60 and i!=63 and i!=67 and i!=71 and i!=73 and i!=75 and i!=79 and i!=83 and i!=86):
            Time_temp,BTime_temp=Data_translater('Boarding.xlsx','Vol n°'+str(i),np.zeros(6),False)[-2:]
            Time=np.concatenate((Time,np.matrix(Time_temp)),axis=0)
            BTime+=[BTime_temp]
            k+=1
    w=np.linalg.solve(np.dot(Time.T,Time),np.ravel(np.dot(Time.T,BTime)))
    print(k)
    return w

ORDER,P,NC,NR1,NR2,NR,Time,BTime=Data_translater('Boarding.xlsx','Vol n°38',np.zeros(6),display=True)
#
#w=weight_finder()
#k=0
#ORDER,P,NC,NR1,NR2,NR,Time,BTime=Data_translater('Boarding.xlsx','Vol n°1',None,display=False)
#BTime=[BTime]
#for i in range(2,87):
#    if (i!=18 and i!=3 and i!=6 and i!=7 and i!=10 and i!=11 and i!=14 and i!=15 and i!=19 and i!=21 and i!=23 and i!=27 and i!=30 and i!=31 and i!=33 and i!=35 and i!=39 and i!=43 and i!=47 and i!=51 and i!=55 and i!=57 and i!=59 and i!=60 and i!=63 and i!=67 and i!=71 and i!=73 and i!=75 and i!=79 and i!=83 and i!=86):
#        k+=1
#        ORDER_temp,P_temp,NC_temp,NR1_temp,NR2_temp,NR_temp,Time_temp,BTime_temp=Data_translater('Boarding.xlsx','Vol n°'+str(i),None,display=False)
#        ORDER+=ORDER_temp
#        P+=P_temp
#        NC+=NC_temp
#        NR1+=NR1_temp
#        NR2+=NR2_temp
#        NR+=NR_temp
#        BTime+=[BTime_temp]
#        Time+=Time_temp
#Em=Coeffs.ErrBoarding(ORDER,P,NC,NR1,NR2,NR,Time,BTime,np.zeros(6))
#print("Erreur moyenne sur l'embarquement méthode max :",np.sum(Em)/len(Em))
#ELS=Coeffs.ErrBoarding(ORDER,P,NC,NR1,NR2,NR,Time,BTime,w)
#print("Erreur moyenne sur l'embarquement méthode moindres carrés :",np.sum(ELS)/len(ELS))

#k=0
#ORDER,P,NC,NR1,NR2,NR,Time,BTime=Data_translater('Boarding_par_vol.xlsx','Rapport 1',w,display=True)
#for i in range(1,87):
#    if (i!=18 and i!=3 and i!=6 and i!=7 and i!=10 and i!=11 and i!=14 and i!=15 and i!=19 and i!=21 and i!=23 and i!=27 and i!=30 and i!=31 and i!=33 and i!=35 and i!=39 and i!=43 and i!=47 and i!=51 and i!=55 and i!=57 and i!=59 and i!=60 and i!=63 and i!=67 and i!=71 and i!=73 and i!=75 and i!=79 and i!=83 and i!=86):
#        k+=1
#        ORDER_temp,P_temp,NC_temp,NR1_temp,NR2_temp,NR_temp,Time_temp,BTime_temp=Data_translater('Boarding.xlsx','Vol n°'+str(i),w,display=False)
#        ORDER+=ORDER_temp
#        P+=P_temp
#        NC+=NC_temp
#        NR1+=NR1_temp
#        NR2+=NR2_temp
#        NR+=NR_temp
#        Time+=Time_temp
#print(Coeffs.Errmoy(ORDER,P,NC,NR1,NR2,NR,Time))

#        ORDER,P,NC,NR1,NR2,NR,Time=Data_translater('Boarding.xlsx','Vol n°'+str(i),False)
#        print(Coeffs.Errmoy(ORDER,P,NC,NR1,NR2,NR,Time))

#Coeffs.Find_coeff(ORDER,P,NC,NR1,NR2,NR,Time)
#print(Coeffs.Errmoy(ORDER,P,NC,NR1,NR2,NR,Time))
#Coeffs.Find_coeff([order6],[P6],[NC6],[NR16],[NR26],[NR6],[fin6-deb6])
#o=Model.Metropolis(order2,P2,NC2,NR12,NR22,NR2,10000,40)

