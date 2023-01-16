# -*- coding: utf-8 -*-
"""
Geração de dados correlacionados
"""

import numpy as np # Biblioteca para manipulação númerica
import matplotlib.pyplot as plt # Biblioteca para visualização e gráficos
import scipy.stats as st # Biblioteca de funções estatísticas
import math as ma


def ex_1(N,rho):
    a0 = 30
    sa = 2
    b0 = 20
    sb = 2
    M = np.zeros([5,N])
    r1 = np.random.randn(N)
    r2 = np.random.randn(N)
    n = 0
    i = 0
    while i < N:
        M[0][i] = a0 + sa*r1[i]
        M[1][i] = b0 + sb*(rho*r1[i] + ma.sqrt(1-rho**2)*r2[i])
        M[2][i] = (a0 - M[0][i])*(b0 - M[1][i])
        M[3][i] = M[0][i] + M[1][i]
        M[4][i] = M[0][i] - M[1][i]
        if ( (M[0][i]-a0)*(M[1][i]-b0) > 0 ):
            n+=1
        i+=1
    am = np.mean(M[0])
    bm = np.mean(M[1])
    M[2] = (M[0] - am)*(M[1] - bm)
    Vab = (1/(N-1))*np.sum(M[2])
    R = Vab/(np.std(M[0], ddof=1)*np.std(M[1], ddof=1))
    sV = (np.std(M[0], ddof=1)*np.std(M[1], ddof=1))*ma.sqrt((1+R**2)/(N-1))
    sR = (1-R**2)/ma.sqrt(N-1)
    saw_soma = np.std(M[3], ddof=1)
    sw_soma = saw_soma/(ma.sqrt(2*(N-1)))
    saw_dif = np.std(M[4], ddof=1)
    sw_dif = saw_dif/(ma.sqrt(2*(N-1)))
    sn = ma.sqrt(N*(n/N)*(1-(n/N)))
    print('n= %.0i # %.1f' % (n,sn))
    print('frequencia relativa de n: %.6f # %.6f' % ((n/N),(sn/N)))
    print('Vab = %.6f # %.6f' % (Vab,sV))
    print('R = %.6f # %.6f' % (R,sR))
    print('Desvio-padrão Amostral da soma: %.6f # %.6f' % (saw_soma,sw_soma))
    print('Desvio-padrão Amostral da diferença: %.6f # %.6f' % (saw_dif,sw_dif))
    plt.plot(M[0],M[1], '*')
    plt.show()