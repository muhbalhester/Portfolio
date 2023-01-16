# -*- coding: utf-8 -*-
"""
Atividade sobre teorema central do limite e intervalos de confiança.
"""

import numpy as np # Biblioteca para manipulação númerica
import matplotlib.pyplot as plt # Biblioteca para visualização e gráficos
import scipy.stats as st # Biblioteca de funções estatísticas
import math

def ex1(N):
    xmin = -1
    xmax = 1
    ymax = 1
    f = lambda x : (3/2)*x**2  
    i = 0
    x = np.zeros(N)
    while i < N:
        x_cand = xmin + (xmax - xmin) * np.random.rand()
        y_test = ymax * np.random.rand()
        if y_test <= f(x_cand):
            x[i] = x_cand
            i += 1
    print("n valores a 1 sigma: %.6f " % (np.sum(np.abs(x)<(math.sqrt(3/5)))))
    print("n valores a 1.5 sigma: %.6f " % (np.sum(np.abs(x)<1.5*(math.sqrt(3/5)))))
    print("n valores a 2 sigma: %.6f " % (np.sum(np.abs(x)<2*(math.sqrt(3/5)))))
    print("n valores a 2.5 sigma: %.6f " % (np.sum(np.abs(x)<2.5*(math.sqrt(3/5)))))
    print("n valores a 3 sigma: %.6f " % (np.sum(np.abs(x)<3*(math.sqrt(3/5)))))
    
def ex2(N):
    xmin = -1
    xmax = 1
    ymax = 1
    f = lambda x : (3/2)*x**2  
    i = 0
    j = 0
    x1 = np.zeros(N)
    x2 = np.zeros(N)
    while i < N:
        x1_cand = xmin + (xmax - xmin) * np.random.rand()
        y1_test = ymax * np.random.rand()
        if y1_test <= f(x1_cand):
            x1[i] = x1_cand
            i += 1
    while j < N:
        x2_cand = xmin + (xmax - xmin) * np.random.rand()
        y2_test = ymax * np.random.rand()
        if y2_test <= f(x2_cand):
            x2[j] = x2_cand
            j += 1
    y = x1 + x2
    sy = math.sqrt(6/5)
    print("n valores a 1 sigma: %.6f " % (np.sum(np.abs(y)<(sy))))
    print("n valores a 1.5 sigma: %.6f " % (np.sum(np.abs(y)<1.5*(sy))))
    print("n valores a 2 sigma: %.6f " % (np.sum(np.abs(y)<2*(sy))))
    print("n valores a 2.5 sigma: %.6f " % (np.sum(np.abs(y)<2.5*(sy))))
    print("n valores a 3 sigma: %.6f " % (np.sum(np.abs(y)<3*(sy))))
    
def ger_exp(N):
    xmin = -1
    xmax = 1
    ymax = 1
    f = lambda x : (3/2)*x**2  
    i = 0
    x = np.zeros(N)
    while i < N:
        x_cand = xmin + (xmax - xmin) * np.random.rand()
        y_test = ymax * np.random.rand()
        if y_test <= f(x_cand):
            x[i] = x_cand
            i += 1
    return x

def ex3(N,M):
    S = np.zeros(N)
    i = 0
    while i < M:
        S = S + ger_exp(N)
        i += 1
    sS = math.sqrt(M*(3/5))
    plt.hist(S)
    plt.show()
    print("n valores a 1 sigma: %.6f " % (np.sum(np.abs(S)<(sS))))
    print("n valores a 1.5 sigma: %.6f " % (np.sum(np.abs(S)<1.5*(sS))))
    print("n valores a 2 sigma: %.6f " % (np.sum(np.abs(S)<2*(sS))))
    print("n valores a 2.5 sigma: %.6f " % (np.sum(np.abs(S)<2.5*(sS))))
    print("n valores a 3 sigma: %.6f " % (np.sum(np.abs(S)<3*(sS))))

def ex4(N):
    S = np.random.randn(N)
    sS = np.std(S, ddof=1)
    plt.hist(S)
    plt.show()
    print("n valores a 1 sigma: %.6f " % (np.sum(np.abs(S)<(sS))))
    print("n valores a 1.5 sigma: %.6f " % (np.sum(np.abs(S)<1.5*(sS))))
    print("n valores a 2 sigma: %.6f " % (np.sum(np.abs(S)<2*(sS))))
    print("n valores a 2.5 sigma: %.6f " % (np.sum(np.abs(S)<2.5*(sS))))
    print("n valores a 3 sigma: %.6f " % (np.sum(np.abs(S)<3*(sS))))
    
    
    
    
    
    
    