# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 16:14:07 2019

@author: 25803263
"""

#Parameter library
import numpy as np
from math import sqrt

#CONSTANTS

#high end value of the coupling parameter
b_0 = 2.5

#feedback of the thermocline gradient on the SST gradient
gamma = 0.75

#damping rate of SST anomalies
c = float(1)

#damping of upper heat content
r = 0.25

#relates enchanced easterly wind stress to the recharge of the ocean heat content
alpha = 0.125

#frequency
omega_c = sqrt(3 / 32)
#period (nondimensionalised)
tau_c = 2 * np.pi / omega_c










