# -*- coding: utf-8 -*-
"""
Distribuição Binomial e estimativa de pi por Monte Carlo
"""

import numpy as np # Biblioteca para manipulação númerica
import matplotlib.pyplot as plt # Biblioteca para visualização e gráficos
import scipy.stats as st # Biblioteca de funções estatísticas
import math as ma

def ex1(N):
    p = np.random.rand(N,2)
    i = 0
    n = 0
    while i < N:
        z = p[i][0]**2 + p[i][1]**2
        if (z <= 1):
            n+=1
        i+=1
    sigma = ma.sqrt(n*(1-(n/N)))
    pi = 4*(n/N)
    sigma_pi = 4*(sigma)/N
    print("n: %.0f" % (n))
    print("sigma: %.6f" % (sigma))
    print("pi: %.6f" % (pi))
    print("sigma pi: %.6f" % (sigma_pi))
    
def ex2(N):
    p = np.random.rand(N,3)
    i = 0
    n = 0
    while i < N:
        z = p[i][0]**2 + p[i][1]**2 + p[i][2]**2
        if (z <= 1):
            n+=1
        i+=1
    sigma = ma.sqrt(n*(1-(n/N)))
    pi = 6*(n/N)
    sigma_pi = 6*(sigma)/N
    print("n: %.0f" % (n))
    print("sigma: %.6f" % (sigma))
    print("pi: %.6f" % (pi))
    print("sigma pi: %.6f" % (sigma_pi))