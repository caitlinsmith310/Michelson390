# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:39:48 2020

@author: caitl
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from uncertainties import ufloat
from uncertainties import unumpy
import scipy.linalg as linalg
from scipy.optimize import curve_fit
from matplotlib.patches import Polygon
from scipy.integrate import quad
import scipy.integrate as integrate
import scipy.special as special
from scipy.integrate import quad
import matplotlib
matplotlib.axes.Axes.errorbar
matplotlib.pyplot.errorbar

start=np.array([6.195,6.370,5.310,6.000])
end=np.array([6.330,6.510,5.445,6.140])
error=np.array([0.0025,0.0025,0.0025,0.0025])

start=unumpy.uarray(start, error)
end=unumpy.uarray(end, error)

width=start-end
print(width)

average=sum(abs(width))/4
print(average)
R=2*average*10**-3/(100*546*10**-9)
print(R)

"""
"""

start=np.array([6.155,6.010,5.855,6.000])
end=np.array([6.010,5.850,6.005,6.150])
error=np.array([0.0025,0.0025,0.0025,0.0025])
fringes=np.array([100,102,100,100])

start=unumpy.uarray(start, error)
end=unumpy.uarray(end, error)

width=abs(start-end)
dpon=width/fringes
avedpon=sum(width/fringes)/4
print(dpon)
print(avedpon)


wavelength=2*avedpon*10**-3/R
print(wavelength)
print("wavelength, nm=",wavelength*10**9)



thickness=ufloat(1.4133,0.0014)/(R*1000)
print(thickness)
dlambda=wavelength**2/(2*thickness)
print(dlambda*10**9)

dp=ufloat((5.130-4.705),0.004)
n=ufloat(1.52,0.01)
ans=(dp/(R*(n-1)))
print(ans)

a=ufloat(0.162,0.004)
b=ufloat(0.151,0.004)
print((a+b)/2)