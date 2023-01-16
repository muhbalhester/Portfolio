# -*- coding: utf-8 -*-
"""
Efeitos de correlações entre grandezas calculadas.
"""

import numpy as np # Biblioteca para manipulação númerica
import matplotlib.pyplot as plt # Biblioteca para visualização e gráficos
import scipy.stats as st # Biblioteca de funções estatísticas
import math as ma

N = 100
nREP = 10000
x0 = 50
s0 = 1
xm = np.zeros(nREP)
xmd = np.zeros(nREP)
xsa = np.zeros(nREP)
n = np.zeros(nREP)
m = np.zeros(nREP)
for i in range(nREP):
    x = x0 + s0*np.random.randn(N)
    xm[i] = np.mean(x)
    xmd[i] = np.median(x)
    xsa[i] = np.std(x, ddof=1)
    n[i] = np.sum(np.abs(x-x0)<=s0)
    m[i] = np.sum(np.abs(x-xm[i])<=xsa[i])
z = (xm+xmd)/2
zs = np.std(z,ddof=1)
print('Desvio-padrão amostral de xm: %.6f # %.6f metros' % (np.std(xm),np.std(xm)/(ma.sqrt(nREP))))
print('Desvio-padrão amostral de xmd: %.6f # %.6f metros' % (np.std(xmd),np.std(xmd)/(ma.sqrt(nREP))))
print('Desvio-padrão de z: %.6f # %.6f metros' % (zs,zs/(ma.sqrt(nREP))))
print('valor médio de n: %.6f # %.6f' % (np.mean(n),np.std(n)/ma.sqrt(nREP)))
print('valor médio de m: %.6f # %.6f' % (np.mean(m),np.std(m)/ma.sqrt(nREP)))
b = N*0.6826
ndp = np.std(n,ddof=1)
mdp = np.std(m,ddof=1)
suc_dp = ma.sqrt(N*0.6826*(1-0.6826))
print('Valor esperado de sucessos em N: %0.6f' % (b))
print('Desvio-padrão de n: %0.6f # %.6f' % (ndp,ndp/(ma.sqrt(2*nREP))))
print('Desvio-padrão de m: %0.6f # %.6f' % (mdp,mdp/(ma.sqrt(2*nREP))))
print('Desvio-padrão esperado no # de sucessos em N: %0.6f' % (suc_dp))