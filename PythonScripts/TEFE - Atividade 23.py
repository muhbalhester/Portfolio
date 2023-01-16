# -*- coding: utf-8 -*-
"""
Covariância entre parâmetros ajustados.
"""

import numpy as np # Biblioteca para manipulação númerica
import matplotlib.pyplot as plt # Biblioteca para visualização e gráficos
import scipy.stats as st # Biblioteca de funções estatísticas
import math as ma

t = np.array([1,2,3,4,5])
X = np.array([3]*5)
t = t-X
h = np.array([1.7 ,3 ,4.2 ,4.8 ,5.4])
hs = np.array([0.2]*5)

M = np.zeros([2,2])
g = np.array([[1]*5,t])

def normal(M,g,gs,y):
    b = np.zeros(len(M[0]-1))
    for i in range(len(M)):
        for j in range(len(M[i])):
            M[i][j] = np.sum(g[i]*g[j]/(gs**2))
        b[i] = np.sum((g[i]*y)/(gs**2))
    return M,b

M,b = normal(M,g,hs,h)
M_inv = np.linalg.inv(M)
param = M_inv @ b

rho = M_inv[0][1]/(ma.sqrt(M_inv[0][0])*ma.sqrt(M_inv[1][1]))
chi = np.sum(((h-(param[0]+param[1]*t))/hs)**2)

print('a : %.6f (%.6f) cm' % (param[0],ma.sqrt(M_inv[0][0])))
print('b : %.6f (%.6f) cm' % (param[1],ma.sqrt(M_inv[1][1])))
print('cov(a,b): %.6f cm2/s' % M_inv[0][1])
print('rho: %.6f' % rho)
print('chi: %.6f' % chi)
print('NGL: %.6f' % (len(h)-len(param)))

t1 = -1.5
t2 = 3

h1 = param[0] + t1*param[1]
h1_inc = ma.sqrt(M_inv[0][0] + (t1*ma.sqrt(M_inv[1][1]))**2 + 2*t1*M_inv[0][1])

h2 = param[0] + t2*param[1]
h2_inc = ma.sqrt(M_inv[0][0] + (t2*ma.sqrt(M_inv[1][1]))**2 + 2*t2*M_inv[0][1])

print('h(%.2f): %.6f (%.6f) cm' % (t1,h1,h1_inc))
print('h(%.2f): %.6f (%.6f) cm' % (t2,h2,h2_inc))

plt.plot(t,h,"*")
plt.plot(t,(param[0] + param[1]*t),'-')
plt.show