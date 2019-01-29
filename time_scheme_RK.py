# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:26:13 2019

@author: 25803263
"""
import numpy as np
#Time scheme, RK4 

def RK4(N_t, ):
    #initialise the vector
    q = np.zeros(2, N_t)
    q[0,0] =
    q[0,1] = 
    for n in range(N_t +1):
        q[n+1,n+1] = [dTdt()]
        
def dTdt(T, h, xi, eps):
    
    R = gamma * b - c
    dTdt = R * T + gamma * h - eps * (h + b * T) ^ 3 + gamma * xi
    
def dhdt(h, t, xi):
    dhdt = - r * h - alpha * b * T - alpha * xi