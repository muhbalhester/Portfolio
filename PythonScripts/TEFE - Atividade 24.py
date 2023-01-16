# -*- coding: utf-8 -*-
"""
Ajuste de dados por MMQ.
"""

import numpy as np # Biblioteca para manipulação númerica
import matplotlib.pyplot as plt # Biblioteca para visualização e gráficos
import scipy.stats as st # Biblioteca de funções estatísticas
import math as ma

dados_arq = open('dados_osciloscopio.txt', 'r')
linhas = dados_arq.readlines()
t = np.zeros(len(linhas))
y = np.zeros(len(linhas))
for i in range(len(linhas)):
    T = linhas[i].split()
    t[i] = float(T[0])
    y[i] = float(T[1])

si = np.array([0.06]*(len(t)))
f = 2
angle = 2*f*ma.pi*t

M = np.zeros([2,2])
g = np.zeros([2,len(t)])
for i in range(len(t)):
    g[0][i] = ma.cos(angle[i])
    g[1][i] = ma.sin(angle[i])

def normal(M,g,gs,y):
    b = np.zeros(len(M[0]-1))
    for i in range(len(M)):
        for j in range(len(M[i])):
            M[i][j] = np.sum(g[i]*g[j]/(gs**2))
        b[i] = np.sum((g[i]*y)/(gs**2))
    return M,b

M,b = normal(M,g,si,y)
M_inv = np.linalg.inv(M)
param = M_inv @ b

rho = M_inv[0][1]/(ma.sqrt(M_inv[0][0])*ma.sqrt(M_inv[1][1]))
chi = np.sum(((y-(param[0]*g[0]+param[1]*g[1]))/si)**2)
A = ma.sqrt(param[0]**2 + param[1]**2)
sA = ma.sqrt(((param[0]*ma.sqrt(M_inv[0][0]))/A)**2 + ((param[1]*ma.sqrt(M_inv[1][1]))/A)**2 + ((4*param[0]*param[1]*M_inv[0][1])/A**2))
Ri = y - (param[0]*g[0] + param[1]*g[1])

print('a : %.6g (%.6g) V' % (param[0],ma.sqrt(M_inv[0][0])))
print('b : %.6g (%.6g) V' % (param[1],ma.sqrt(M_inv[1][1])))
print('cov(a,b): %.6g V2' % M_inv[0][1])
print('rho: %.6f' % rho)
print('Amplitude: %.6g (%.6g) V' % (A,sA))
print('chi: %.6f' % chi)
print('NGL: %.6f' % (len(y)-len(param)))

plt.plot(t,y,"*")
plt.plot(t,(param[0]*g[0] + param[1]*g[1]),'-')
plt.title('Ajuste dos Dados')
plt.ylabel('Tensão - V')
plt.xlabel('Tempo - s')
plt.show()
plt.plot(t,Ri,"-")
plt.title('Resíduos')
plt.ylabel('Tensão - V')
plt.xlabel('Tempo - s')
plt.show()