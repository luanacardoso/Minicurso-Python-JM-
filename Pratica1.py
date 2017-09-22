#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 11:28:32 2017

@author: labsim
"""

import numpy as np
import matplotlib.pyplot as plt

print("hello world")

i1,i2 = 0.8,0.3

theta = np.linspace(-3,3,1000) #de -10 a 10 com 1000 amostras

L11 = (3+np.cos(2*theta))*10e-3
L22 = 0.3*np.cos(theta)
L12 = (30+10*np.cos(2*theta))

W = 0.5*L11*i1**2 + L12*i1*i2 + 0.5*L22*i2**2
W_relutancia = 0.5*L11*i1**2 + 0.5*L22*i2**2
W_mutuo = L12*i1*i2

T_total = np.diff(W) #derivada de W
T_r = np.diff(W_relutancia)
T_m = np.diff(W_mutuo)

#plt.plot(theta,W,'b')

#Tem q "indexar" pq T_r tem 999 (por causa da derivada) e theta tem 1000

plt.figure(1,[10,7]) #1:Separar figuras // 10 pol de comprimento e 7 de altura
plt.subplot(311) #3 linhas 1 coluna
plt.plot(theta[0:len(theta)-1],T_total,'b')
plt.title("torque total")
plt.ylabel("Torque [N-m]")
plt.xlabel("$\Theta$ [radianos]")
plt.grid()

plt.subplot(312)
plt.plot(theta[0:len(theta)-1],T_r,'y')
plt.title("torque relutancia")
plt.ylabel("Torque [N-m]")
plt.xlabel("$\Theta$ [radianos]")
plt.grid()

plt.subplot(313)
plt.plot(theta[0:len(theta)-1],T_m,'g')
plt.title("torque mutuo")
plt.ylabel("Torque [N-m]")
plt.xlabel("$\Theta$ [radianos]")
plt.grid()

plt.tight_layout()
plt.show()



