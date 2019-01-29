# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 16:17:23 2019

@author: 25803263
"""
import matplotlib.pyplot as plt

from parameter_functions import *
from __init__ import *
from time_scheme_RK import *


T,h = RK4()

print(T)

print(h)

fig = plt.figure()
l1 = plt.plot(T * 7.5, h * 150,  'b-')
plt.xlabel('T - redimenionalised')
plt.ylabel('h - redimensionalised')
plt.title("Ocean Recharge Oscillator")
plt.show()