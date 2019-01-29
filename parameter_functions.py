# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:05:00 2019

@author: 25803263
"""
import numpy as np
from random import random

def mew(t, b_0 = 2.5 mew_wac = 2/3, mew_0 = 0.75, mew_ann = 0.2, eps = 0.1, tau = (12/2),
        ac = "yes"):
    
    #with annual cycle
    if ac == "yes":
        mew = mew_0 * (1 + mew_ann * np.cos((2 * np.pi * t / tau) - (5 * np.pi / 6)))
    
    #without annual cycle
    else:
        mew = mew_wac
        
    #relates stronger thermocline gradient to stronger easterly wind stress
    b = b_0 * mew
    return b

def xi(t, dt, wsf = "yes", f_ann = 0.02, f_ran = 0.2, eps = 0.1, mew_0 = 0.75, 
       mew_ann = 0.2, tau = (12/2), tau_cor = 1/(30*2)):
    
    #with wind stress forcing 
    if wsf == "yes":
        W = -1 + (random()*2)
    
        xi = f_ann * np.cos(2 * np.pi * t / tau) + f_ran * W * (tau_cor / dt)
    
    #without wind stress forcing
    else:
        xi = 0
    
    return xi