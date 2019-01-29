# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:26:13 2019

@author: 25803263
"""

from parameter_functions import *
from __init__ import *
from time_scheme_RK import *


import numpy as np
#Time scheme, RK4 

def RK4(nop = 1, dt = 1/60, eps = float(0), ac = "no", wsf = "no"):
    # in this space dt = 1 is equal to 2 months so 1/60 is one day
    
    #time to solution
    T = tau_c * nop
    N_t = int(round(T/dt))

    #time vector
    t = np.linspace(0, N_t*dt, N_t+1) 
    
    #initialise the vector
    q = np.zeros((int(2), N_t + 1))
    q[:,0] = [T_0, h_0]
    
    for n in range(N_t):
        #check size can work
        k1 = [dTdt(q[0,n],q[1,n], t[n], ac, wsf, eps), dhdt(q[0,n], q[1,n], t[n], ac, wsf)]
        
        k2 = [dTdt(q[0,n] + k1[0]* dt / 2,q[1,n] + k1[1] * dt /2 , t[n] + dt / 2, ac, wsf, eps), 
              dhdt(q[0,n] + k1[0]* dt / 2, q[1,n] + k1[1] * dt /2 , t[n] + dt / 2, ac, wsf)]
        
        k3 = [dTdt(q[0,n] + k2[0]* dt / 2,q[1,n] + k2[1] * dt /2 , t[n] + dt / 2, ac, wsf, eps), 
              dhdt(q[0,n] + k2[0]* dt / 2, q[1,n] + k2[1] * dt /2 , t[n] + dt / 2, ac, wsf)]
        
        k4 = [dTdt(q[0,n] + k3[0]* dt / 2,q[1,n] + k3[1] * dt /2 , t[n] + dt, ac, wsf, eps), 
              dhdt(q[0,n] + k3[0]* dt / 2, q[1,n] + k3[1] * dt /2 , t[n] + dt,ac, wsf)]
        
        for i in range(2):
            q[i,n+1] = q[i, n] + dt * 1/6 * (k1[i] + 2 * (k2[i] + k3[i]) + k4[i])
        
    return q
        
        
def dTdt(T, h, t, ac, wsf, eps):
    #need to calculate xi,b
    
    R = gamma * mew(t, ac) - c
    dTdt = R * T + gamma * h - eps * (h + mew(t, ac) * T)**3 + gamma * xi(t, dt, wsf)
    
    return dTdt
    
def dhdt(T, h, t, ac, wsf):
    #need to calculate b andxi here

    dhdt = - r * h - alpha * mew(t, ac) * T - alpha * xi(t, dt, wsf)
    
    return dhdt
    
