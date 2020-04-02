# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:08:39 2020

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
import time

#everything in nanometers




l1=np.sin(589*x)
l2=np.sin(589.6*x)
plt.plot(x,l1,x,l2)
plt.plot(x,(l1+l2), )
plt.legend()
  

#didnt use, not clear enought
x=np.arange(0,900000,300)
x_axis=x/10**6

l1=np.sin((2*np.pi)*x/589)
l2=np.sin((2*np.pi)*x/589.6)
s=(l1+l2)
l=(0.5*l1+l2)
plt.plot(x_axis,s, label="Superimposed")
plt.plot(x_axis,l, label="Superimposed")


plt.plot(x_axis,l1,label="$\lambda=589.0nm$")
plt.plot(x_axis,l2,label="$\lambda=589.6nm$")

plt.xlabel("Distance, mm")
print(n)
plt.legend()



#fringe locations
n=np.array([0,1,2,3])
red=635*n/2
green=490*n/2
yellow=560*n/2
orange=590*n/2
blue=450*n/2
purple=400*n/2
x1=np.array([0,0,0,0])
x2=np.array([1,1,1,1])
x3=np.array([1,1,1,1])

plt.subplot(6,1,1)
plt.scatter(red,x2, color="red")
plt.scatter(blue, x2, color="blue")
plt.scatter(orange, x2, color="orange")
plt.scatter(green, x2, color="green")
plt.scatter(yellow, x2, color="yellow")
plt.scatter(purple,x3,color="purple")
plt.xlabel("Distance from zero path length, nm")

plt.subplot(2,1,1)
plt.scatter(red,635*x2, color="red")
plt.scatter(green, 490*x2, color="green")
plt.scatter(blue, 450*x2, color="blue")
plt.scatter(orange, 590*x2, color="orange")
plt.scatter(green, 490*x2, color="green")

plt.scatter(yellow, 560*x2, color="yellow")

plt.scatter(purple,400*x3,color="purple")
plt.xlabel("Distance from zero path length, nm")
plt.ylabel("Wavelength, nm")


