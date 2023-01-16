# -*- coding: utf-8 -*-
"""
Erros sistemáticos e Covariância.
"""

import numpy as np # Biblioteca para manipulação númerica
import matplotlib.pyplot as plt # Biblioteca para visualização e gráficos
import scipy.stats as st # Biblioteca de funções estatísticas
import math as ma

def ex_1(N):
    x0 = 110
    y0 = 100
    sC = 4
    sL = 3
    r = [np.random.randn(N),np.random.randn(N),np.random.randn(N)]
    eC = sC*r[0]
    x = x0 + eC + (sL*r[1])
    y = y0 + eC + (sL*r[2])
    n = np.sum((x0-x)*(y0-y)>0)
    f = n/N
    sf = (ma.sqrt(N*f*(1-f)))
    print('frequencia relativa: %.6f # %.6f' % (f,sf/N))
    Vxy = (1/(N-1))*np.sum((np.mean(x)-x)*(np.mean(y)-y))
    R = Vxy/(np.std(x, ddof=1)*np.std(y, ddof=1))
    sV = (np.std(x, ddof=1)*np.std(y, ddof=1))*ma.sqrt((1+R**2)/(N-1))
    sR = (1-R**2)/ma.sqrt(N-1)
    w = x + y
    saw = np.std(w,ddof=1)
    sw = saw/(ma.sqrt(2*(N-1)))
    z = x - y
    saz = np.std(z,ddof=1)
    sz = saz/(ma.sqrt(2*(N-1)))
    print('Vab = %.6f # %.6f' % (Vxy,sV))
    print('R = %.6f # %.6f' % (R,sR))
    print('Desvio-padrão Amostral da soma: %.6f # %.6f' % (saw,sw))
    print('Desvio-padrão Amostral da diferença: %.6f # %.6f' % (saz,sz))
    plt.plot(x,y,'*')
    plt.show()
    
def ex_2(N,M):
    d0 = 200
    sS = 4
    sA = 3
    exp = np.zeros(M)
    for i in range(M):
        eS = np.random.randn()*sS
        eA = np.random.randn(N)*sA
        di = d0 + eS + eA
        exp[i] = np.mean(di)
    sdm = np.std(exp,ddof=1)
    sdm_inc = sdm/(ma.sqrt(2*(M-1)))
    print('Incerteza dos valores médios: %.6f # %.6f' % (sdm,sdm_inc))
    return di
    
    