#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""

"""
from sympy import *
import sys



T = Symbol('T') #create 'T' symbol
m = Symbol('m') #create 'm' symbol
Kp = Symbol('Kp') #create 'Kp' symbol

T = 0.01#Symbol('T') #create 'T' symbol
m = 10000#Symbol('m') #create 'm' symbol
Kp = 50#Symbol('Kp') #create 'Kp' symbol

A = Matrix([[1,T],[0,1]]) #A matrix
B = Matrix([[0],[T/m]]) #B matrix
C = Matrix([[1,0]]) #C matrix
K = Matrix([[Kp,10]]) #K matrix

print('Matrix A:')
print(A)
print('Matrix B: ')
print(B)
print('Matrix C:')
print(C)
print('Matrix K:')
print(K)
print(eye(2))

#sys.exit(0);
print('====================')
print("Open Loop Natural Frequencies/Eigenvalues:")
print(A.eigenvals())
print("Closed Loop Natural Frequencies/Eigenvalues:")
M = A- B*K #calculate closed loop state transition matrix
print(M.eigenvals())
#print("Ku Value:")
#Ku = (C*(eye(2)-A +B*K)**(-1)*B)**(-1) #calculate input scaling gain
#print(Ku)
