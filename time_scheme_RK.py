# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:26:13 2019

@author: 25803263
"""
import numpy as np
#Time scheme, RK4 

def RK4(N_t, dt, t):
    #initialise the vector
    q = np.zeros(2, N_t)
    q[:,0] = [T_0, h_0]
    
    for n in range(N_t + 1):
        #check size can work
        k1 = [dTdt(q[0,n],q[1,n], t), dhdt(q[0,n], q[1,n], t)]
        k2 = [dTdt(q[0,n] + k1[0]* dt / 2,q[1,n] + k1[1] * dt /2 , t + dt / 2), 
              dhdt(q[0,n] + k1[0]* dt / 2, q[1,n] + k1[1] * dt /2 , t + dt / 2)]
        k3 = [dTdt(q[0,n] + k2[0]* dt / 2,q[1,n] + k2[1] * dt /2 , t + dt / 2), 
              dhdt(q[0,n] + k2[0]* dt / 2, q[1,n] + k2[1] * dt /2 , t + dt / 2)]
        k4 = [dTdt(q[0,n] + k3[0]* dt / 2,q[1,n] + k3[1] * dt /2 , t + dt), 
              dhdt(q[0,n] + k3[0]* dt / 2, q[1,n] + k3[1] * dt /2 , t + dt)]
        
        q[:,n+1] = q[:, n] + dt * 1/6 * (k1 + 2 * (k2 + k3) + k4)
        
        
def dTdt(T, h, t):
    #need to calculate xi,b and eps here
    R = gamma * b - c
    dTdt = R * T + gamma * h - eps * (h + b * T) ^ 3 + gamma * xi
    
def dhdt(T, h, t):
    #need to calculate b andxi here
    dhdt = - r * h - alpha * b * T - alpha * xi
    
