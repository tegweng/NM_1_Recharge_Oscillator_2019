# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 16:14:07 2019

@author: 25803263
"""

#Parameter library
import numpy as np
from math import sqrt
from random import random
#CONSTANTS

#high end value of the coupling parameter
b_0 = 2.5

#feedback of the thermocline gradient on the SST gradient
gamma = 0.75

#damping rate of SST anomalies
c = 1

#damping of upper heat content
r = 0.25

#relates enchanced easterly wind stress to the recharge of the ocean heat content
alpha = 0.125

#frequency
omega_c = sqrt(3 / 32)

#INITIAL CONDITIONS (non-dimensionalised)
h_0 = 0
T_0 = 1.125 / 7.5

#PARAMETERS

#coupling coefficient
mew = 2/3

#relates stronger thermocline gradient to stronger easterly wind stress
b = b_0 * mew

#describes Bjerknes positive feedback process
R = (gamma * b) - c 

#varies the degree of nonlinearity
eps = 0

#additional wind forcing
xi = 0

#period (nondimensionalised)
tau_c = 2 * np.pi / omega_c

#FUNCTIONS
def mew(t, mew_0 = 0.75, mew_ann = 0.2, eps = 0.1, tau = (12/2)):
    
    mew = mew_0 * (1 + mew_ann * np.cos((2 * np.pi * t / tau) - (5 * np.pi / 6)))
    
    return mew

def xi(t, dt, f_ann = 0.02, f_ran = 0.2, eps = 0.1, mew_0 = 0.75, mew_ann = 0.2, tau = (12/2), tau_cor = 1/(30*2)):
    W = -1 + (random()*2)
    
    xi = f_ann * np.cos(2 * np.pi * t / tau) + f_ran * W * (tau_cor / dt)
    
    return xi



