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


wb = xlrd.open_workbook('Boarding_par_vol.xlsx')
sh=wb.sheet_by_name('Rapport 1')
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

#ORDER=[order1,order2,order3,order4,order5,order6]
#P=[P1,P2,P3,P4,P5,P6]
#NC=[18,18,15,15,14,14]
#NR111=[3,2,3,2,3,2]
#NR222=[2,3,2,3,2,3]
#NR=[5,5,5,5,5,5]
#Time=[fin1-deb1,fin2-deb2,fin3-deb3,fin4-deb4,fin5-deb5,fin6-deb6]
#
#wb = xlrd.open_workbook('Boarding_par_vol (2).xlsx')
#sh=wb.sheet_by_name('Grain Passager')
#d,f=Rush.find_rush(sh)
#
#
#order1=[]
#order2=[]
#order3=[]
#order4=[]
#order5=[]
#order6=[]
#deb1=0
#fin1=0
#deb2=0
#fin2=0
#deb3=0
#fin3=0
#deb4=0
#fin4=0
#deb5=0
#fin5=0
#deb6=0
#fin6=0
#P1=np.zeros([5,18])
#P2=np.zeros([5,18])
#P3=np.zeros([5,15])
#P4=np.zeros([5,15])
#P5=np.zeros([5,14])
#P6=np.zeros([5,14])
#[NC1,NR11,NR21,NR1]=[18,3,2,5]
#[NC2,NR12,NR22,NR2]=[18,2,3,5]
#[NC3,NR13,NR23,NR3]=[15,3,2,5]
#[NC4,NR14,NR24,NR4]=[15,2,3,5]
#[NC5,NR15,NR25,NR5]=[14,3,2,5]
#[NC6,NR16,NR26,NR6]=[14,2,3,5]
#for rownum in range(sh.nrows):
#    col=(ord(sh.row_values(rownum)[3][0])-48)*10+ord(sh.row_values(rownum)[3][1])-48
#    row=ord(sh.row_values(rownum)[3][2])-65
#    if (col>9) and (col<28) and (row<6):
#        p=(27-col)*5+row-1*(row>3)+1
#        if (rownum<d):
#            P1=Model.SetPassenger(p,P1,NC1,NR11,NR21,NR1)
#        if (rownum>=d) and (rownum<=f):
#            if (deb1==0):
#                deb1=sh.row_values(rownum)[1]
#            order1+=[p]
#            fin1=sh.row_values(rownum)[1]
#    if (col>9) and (col<28) and (row>5):
#        p=(27-col)*5+row-5-1*(row>8)
#        if (rownum<d):
#            P2=Model.SetPassenger(p,P2,NC2,NR12,NR22,NR2)
#        if (rownum>=d) and (rownum<=f):
#            if (deb2==0):
#                deb2=sh.row_values(rownum)[1]
#            order2+=[p]
#            fin2=sh.row_values(rownum)[1]
#    if (col>28) and (col<45) and (row<6):
#        p=(44-col)*5+row-1*(row>3)+1
#        if (rownum<d):
#            P3=Model.SetPassenger(p,P3,NC3,NR13,NR23,NR3)
#        if (rownum>=d) and (rownum<=f):
#            if (deb3==0):
#                deb3=sh.row_values(rownum)[1]
#            order3+=[p]
#            fin3=sh.row_values(rownum)[1]
#    if (col>28) and (col<45) and (row>5):
#        p=(44-col)*5+row-5-1*(row>8)
#        if (rownum<d):
#            P4=Model.SetPassenger(p,P4,NC4,NR14,NR24,NR4)
#        if (rownum>=d) and (rownum<=f):
#            if (deb4==0):
#                deb4=sh.row_values(rownum)[1]
#            order4+=[p]
#            fin4=sh.row_values(rownum)[1]
#    if (col>45) and (col<59) and (row<6):
#        p=(58-col)*5+row-1*(row>3)+1
#        if (rownum<d):
#            P5=Model.SetPassenger(p,P5,NC5,NR15,NR25,NR5)
#        if (rownum>=d) and (rownum<=f):
#            if (deb5==0):
#                deb5=sh.row_values(rownum)[1]
#            order5+=[p]
#            fin5=sh.row_values(rownum)[1]
#    if (col>45) and (col<59) and (row>5):
#        p=(58-col)*5+row-5-1*(row>8)
#        if (rownum<d):
#            P6=Model.SetPassenger(p,P6,NC6,NR16,NR26,NR6)
#        if (rownum>=d) and (rownum<=f):
#            if (deb6==0):
#                deb6=sh.row_values(rownum)[1]
#            order6+=[p]
#            fin6=sh.row_values(rownum)[1]
#
#print("=============================================")
#print("                  BLOC 1")
#print("=============================================")
#Model.Checkorder(order1,NC1,NR11,NR21,NR1)
#BT1=Model.TotalBoardingTime(order1,P1,NC1,NR11,NR21,NR1)
#print("Temps calculé :",BT1/60)
#print("Temps réel :",fin1-deb1)
#print("=============================================")
#print("                  BLOC 2")
#print("=============================================")
#Model.Checkorder(order2,NC2,NR12,NR22,NR2)
#BT2=Model.TotalBoardingTime(order2,P2,NC2,NR12,NR22,NR2)
#print("Temps calculé :",BT2/60)
#print("Temps réel :",fin2-deb2)
#print("=============================================")
#print("                  BLOC 3")
#print("=============================================")
#Model.Checkorder(order3,NC3,NR13,NR23,NR3)
#BT3=Model.TotalBoardingTime(order3,P3,NC3,NR13,NR23,NR3)
#print("Temps calculé :",BT3/60)
#print("Temps réel :",fin3-deb3)
#print("=============================================")
#print("                  BLOC 4")
#print("=============================================")
#Model.Checkorder(order4,NC4,NR14,NR24,NR4)
#BT4=Model.TotalBoardingTime(order4,P4,NC4,NR14,NR24,NR4)
#print("Temps calculé :",BT4/60)
#print("Temps réel :",fin4-deb4)
#print("=============================================")
#print("                  BLOC 5")
#print("=============================================")
#Model.Checkorder(order5,NC5,NR15,NR25,NR5)
#BT5=Model.TotalBoardingTime(order5,P5,NC5,NR15,NR25,NR5)
#print("Temps calculé :",BT5/60)
#print("Temps réel :",fin5-deb5)
#print("=============================================")
#print("                  BLOC 6")
#print("=============================================")
#Model.Checkorder(order6,NC6,NR16,NR26,NR6)
#BT6=Model.TotalBoardingTime(order6,P6,NC6,NR16,NR26,NR6)
#print("Temps calculé :",BT6/60)
#print("Temps réel :",fin6-deb6)
#
#
#ORDER+=[order1,order2,order3,order4,order5,order6]
#P+=[P1,P2,P3,P4,P5,P6]
#NC+=[18,18,15,15,14,14]
#NR111+=[3,2,3,2,3,2]
#NR222+=[2,3,2,3,2,3]
#NR+=[5,5,5,5,5,5]
#Time+=[fin1-deb1,fin2-deb2,fin3-deb3,fin4-deb4,fin5-deb5,fin6-deb6]
#
#
#
#Coeffs.Find_coeff(ORDER,P,NC,NR111,NR222,NR,Time)

#Coeffs.Find_coeff([order6],[P6],[NC6],[NR16],[NR26],[NR6],[fin6-deb6])
#o=Model.Metropolis(order2,P2,NC2,NR12,NR22,NR2,10000,40)
#order2=[]
#deb=0
#fin=0
#for rownum in range(sh.nrows):
#    col=(ord(sh.row_values(rownum)[3][0])-48)*10+ord(sh.row_values(rownum)[3][1])-48
#    row=ord(sh.row_values(rownum)[3][2])-65
#    if (col>9) and (col<28) and (row>5) and (rownum>16) and (rownum<389):
#        if (deb==0):
#            deb=sh.row_values(rownum)[1]
#        p=(27-col)*5+row-5-1*(row>8)
#        order+=[p]
#        fin=sh.row_values(rownum)[1]
#print(order)
#print(fin-deb)
#
#order=[]
#deb=0
#fin=0
#for rownum in range(sh.nrows):
#    col=(ord(sh.row_values(rownum)[3][0])-48)*10+ord(sh.row_values(rownum)[3][1])-48
#    row=ord(sh.row_values(rownum)[3][2])-65
#    if (col>28) and (col<45) and (row<6) and (rownum>16) and (rownum<389):
#        if (deb==0):
#            deb=sh.row_values(rownum)[1]
#        p=(44-col)*5+row-1*(row>3)+1
#        order+=[p]
#        fin=sh.row_values(rownum)[1]
#print(order)
#print(fin-deb)
#
#order=[]
#deb=0
#fin=0
#for rownum in range(sh.nrows):
#    col=(ord(sh.row_values(rownum)[3][0])-48)*10+ord(sh.row_values(rownum)[3][1])-48
#    row=ord(sh.row_values(rownum)[3][2])-65
#    if (col>28) and (col<45) and (row>5) and (rownum>16) and (rownum<389):
#        if (deb==0):
#            deb=sh.row_values(rownum)[1]
#        p=(44-col)*5+row-5-1*(row>8)
#        order+=[p]
#        fin=sh.row_values(rownum)[1]
#print(order)
#print(fin-deb)
#
#order=[]
#deb=0
#fin=0
#for rownum in range(sh.nrows):
#    col=(ord(sh.row_values(rownum)[3][0])-48)*10+ord(sh.row_values(rownum)[3][1])-48
#    row=ord(sh.row_values(rownum)[3][2])-65
#    if (col>45) and (col<59) and (row<6) and (rownum>16) and (rownum<389):
#        if (deb==0):
#            deb=sh.row_values(rownum)[1]
#        p=(58-col)*5+row-1*(row>3)+1
#        order+=[p]
#        fin=sh.row_values(rownum)[1]
#print(order)
#print(fin-deb)
#
#order=[]
#deb=0
#fin=0
#for rownum in range(sh.nrows):
#    col=(ord(sh.row_values(rownum)[3][0])-48)*10+ord(sh.row_values(rownum)[3][1])-48
#    row=ord(sh.row_values(rownum)[3][2])-65
#    if (col>45) and (col<59) and (row>5) and (rownum>16) and (rownum<389):
#        if (deb==0):
#            deb=sh.row_values(rownum)[1]
#        p=(58-col)*5+row-5-1*(row>8)
#        order+=[p]
#        fin=sh.row_values(rownum)[1]
#print(order)
#print(fin-deb)
