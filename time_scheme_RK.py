# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:26:13 2019

@author: 25803263
"""
import numpy as np
#Time scheme, RK4 

def RK4(N_t, dt, xi, eps, b):
    #initialise the vector
    q = np.zeros(2, N_t)
    q[:,0] = [T_0, h_0]
    
    for n in range(N_t + 1):
        k1 = [dTdt(q[0,n],q[1,n], xi, eps, b), dhdt(q[0,n], q[1,n], xi, b)]
        k2 = []
        k3 = []
        k4 = []
        
        q[:,n+1] = q[:, n] + dt * 1/6 * (k1 + 2 * (k2 + k3) + k4)
        
        
def dTdt(T, h, xi, eps, b):
    
    R = gamma * b - c
    dTdt = R * T + gamma * h - eps * (h + b * T) ^ 3 + gamma * xi
    
def dhdt(T, h, xi, b):
    dhdt = - r * h - alpha * b * T - alpha * xi
    
