# -*- coding: utf-8 -*-
"""
Estimativas amostrais de desvio-padrão e variância
"""

import numpy as np # Biblioteca para manipulação númerica
import matplotlib.pyplot as plt # Biblioteca para visualização e gráficos
import scipy.stats as st # Biblioteca de funções estatísticas
import math as ma

x0 = 0
s0 = 1
M = 10000
N = [2,3,4,5,10,50,100]
print('------------------------------------')
for j in N:
    s = np.zeros(M)
    V = np.zeros(M)
    for i in range(M):
        x = x0 + s0*np.random.randn(j)
        xm = np.mean(x)
        v = (x-xm)**2
        s[i] = ma.sqrt((1/(j-1))*np.sum(v))
        V[i] = s[i]**2
    plt.hist(s)
    plt.title('Histograma de s, N=%.0i' % (j))
    plt.show()
    plt.hist(V)
    plt.title('Histograma de V, N=%.0i' % (j))
    plt.show()
    sm = np.mean(s)
    sm_s = np.std(s,ddof=1)/ma.sqrt(M)
    Vm = np.mean(V)
    Vm_s = np.std(V,ddof=1)/ma.sqrt(M)
    s_cont = np.sum(s<=s0)
    s_inc = ma.sqrt(s_cont*(1-(s_cont/M)))
    V_cont = np.sum(V<=(s0**2))
    V_inc = ma.sqrt(V_cont*(1-(V_cont/M)))
    print('N=%.0i' % j)
    print('s médio: %.6f # %.6f' % (sm,sm_s))
    print('V médio: %.6f # %.6f' % (Vm,Vm_s))
    print('Valores de s menores que s0: %.6f # %.6f' % (s_cont,s_inc))
    print('Valores de V menores que s0^2: %.6f # %.6f' % (V_cont,V_inc))
    print('------------------------------------')
