# -*- coding: utf-8 -*-
"""
Monte Carlo e estudo de diferentes funções de densidade de probabilidade.
"""

import numpy as np # Biblioteca para manipulação númerica
import matplotlib.pyplot as plt # Biblioteca para visualização e gráficos
import scipy.stats as st # Biblioteca de funções estatísticas
import math

def ex1(x0,s0,N):
    x = x0 + s0*np.random.randn(N)
    xm = np.mean(x)
    sxm = np.std(x, ddof=1)/(math.sqrt(N))
    sx = np.std(x, ddof=1)
    x_i = np.sum(np.abs(x-xm)<sx)
    x_2i = np.sum(np.abs(x-xm)<2*sx)
    x_3i = np.sum(np.abs(x-xm)<3*sx)
    print("x médio: %.6f +/- %.6f" % (xm,sxm))
    print("desvio-padrão amostral de x: %.6f" % (sx))
    print("x em 1 sigma: %.6f" % (x_i))
    print("x em 2 sigma: %.6f" % (x_2i))
    print("x em 3 sigma: %.6f" % (x_3i))
    
def ex2(s0,N):
    x = -s0 + np.random.rand(N)
    xm = np.mean(x)
    sxm = np.std(x, ddof=1)/(math.sqrt(N))
    sx = np.std(x, ddof=1)
    x_i = np.sum(np.abs(x-xm)<sx)
    x_2i = np.sum(np.abs(x-xm)<2*sx)
    x_3i = np.sum(np.abs(x-xm)<3*sx)
    print("x médio: %.6f +/- %.6f" % (xm,sxm))
    print("desvio-padrão amostral de x: %.6f" % (sx))
    print("x em 1 sigma: %.6f" % (x_i))
    print("x em 2 sigma: %.6f" % (x_2i))
    print("x em 3 sigma: %.6f" % (x_3i))
    plt.plot(x,'*')

def ex3(s0,N):
    x = -s0 + np.random.rand(N) + np.random.rand(N)
    xm = np.mean(x)
    sxm = np.std(x, ddof=1)/(math.sqrt(N))
    sx = np.std(x, ddof=1)
    x_i = np.sum(np.abs(x-xm)<sx)
    x_2i = np.sum(np.abs(x-xm)<2*sx)
    x_3i = np.sum(np.abs(x-xm)<3*sx)
    print("x médio: %.6f +/- %.6f" % (xm,sxm))
    print("desvio-padrão amostral de x: %.6f" % (sx))
    print("x em 1 sigma: %.6f" % (x_i))
    print("x em 2 sigma: %.6f" % (x_2i))
    print("x em 3 sigma: %.6f" % (x_3i))
    plt.plot(x,'*')