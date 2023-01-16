# -*- coding: utf-8 -*-
"""
Testes estatísticos 't' e 'z'
"""

import numpy as np # Biblioteca para manipulação númerica
import matplotlib.pyplot as plt # Biblioteca para visualização e gráficos
import scipy.stats as st # Biblioteca de funções estatísticas
import math as ma

def experimento(N):
    x0 = 50
    s0 = 10
    x = np.zeros(N)
    x = x0 + s0*np.random.randn(N)
    xm = np.mean(x)
    xs = (np.std(x,ddof=1)/(ma.sqrt(N)))
    xms0 = s0/(ma.sqrt(N))
    z = (xm-x0)/xms0
    t = (xm-x0)/xs
    return t,z

def nExp(nRep,N):
    tt = float(input('Qual o parâmetro de comparacao t?'))
    zt = float(input('Qual o parâmetro de comparacao z?'))
    t = np.zeros(nRep)
    z = np.zeros(nRep)
    for i in range(nRep):
        t[i],z[i] = experimento(N)
    t2 = np.sum(np.abs(t)<=tt)
    z2 = np.sum(np.abs(z)<=zt)
    t2_fr = t2/nRep
    z2_fr = z2/nRep
    t2_i = ma.sqrt(nRep*t2_fr*(1-t2_fr))/nRep
    z2_i = ma.sqrt(nRep*z2_fr*(1-z2_fr))/nRep
    print('------------------------------------------')
    print("freq. rel. t2: %.6f (%.6f)" % (t2_fr,t2_i))
    print("freq. rel. z2: %.6f (%.6f)" % (z2_fr,z2_i))

