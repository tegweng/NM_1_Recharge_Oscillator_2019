# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 16:03:14 2019

@author: 25803263
"""
from parameter_functions import *
from __init__ import *
from time_scheme_RK import *
import matplotlib.pyplot as plt
#ensemble time

def ensemble(enum, perT,perh, nop = 1, dt = 1/60, eps = float(0),mew_wac = 2/3, ac = "no", wsf = "no", T_0 = 1.125 / 7.5, h_0 = float(0)):
    #perT and perH are the magnitude of the perturbation not the exact value
    
    #time to solution
    T = tau_c * nop
    N_t = int(round(T/dt))
    #time vector
    t = np.linspace(0, N_t*dt, N_t+1) 
            
    fig = plt.figure()
    for i in range(enum +1):
        l1 = plt.plot(t *2, var(perT,perh, nop) * 7.5,  'b-')
    
    plt.xlabel('Time in months')
    plt.ylabel('T in K')
    plt.title("t-T diagram for Ensemble")
    plt.show()
    
def var(perT,perh, nop, dt = 1/60, eps = float(0),mew_wac = 2/3, ac = "no", wsf = "no", T_0 = 1.125 / 7.5, h_0 = float(0)):
    
    varT = T_0 + (1 -random()*2)*perT
    varh = h_0 + (1 - random()*2)*perh
        
    q,t = RK4(nop = nop, eps = eps, mew_wac = mew_wac, ac = ac, wsf = ac, T_0 = varT, h_0 = varh)
    T = q[0,:]
    
    return T