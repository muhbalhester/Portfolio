# -*- coding: utf-8 -*-
"""
Essas funções criam conjuntos aleatórios de pontos que respeitam certas funções de distribuição de probabilidade. No método de exclusão gera-se uma região de distribuição uniforme e seleciona-se somente os valores que seguem a função desejada. No método de inversão, utilizamos a função de densidade acumulada da função de distribuição desejada e a invertemos, gerando valores aleatórios entre 0 e 1 e calculando a inversa.
"""
import numpy as np # Biblioteca para manipulação númerica
import matplotlib.pyplot as plt # Biblioteca para visualização e gráficos
import scipy.stats as st # Biblioteca de funções estatísticas
import math

def metodo_exclusao(g,N):
    xmin = -1
    xmax = 1
    ymax = 2
    f = lambda x : ((g+1)/(2*g))*(1-np.abs(x)**g)    
    i = 0
    x = np.zeros(N)
    while i < N:
        x_cand = xmin + (xmax - xmin) * np.random.rand()
        y_test = ymax * np.random.rand()
        if y_test <= f(x_cand):
            x[i] = x_cand
            i += 1
    sx = np.std(x, ddof=1)
    print("média de x: %.6f" % (np.mean(x)))
    print("desvio-padrão amostral de x: %.6f" % (sx))
    print("Frequencia Relativa: %.6f" % (np.sum(np.abs(x)<math.sqrt((g+1)/(3*g+9)))/N))
    
def metodo_inversao(L,N):
    inv_g_pos = lambda g_pos : np.log((2*g)**L)
    inv_g_neg = lambda g_neg : np.log((1/((-2*g)+2))**L)
    x = np.zeros(N)
    for i in range(N-1):
        g = np.random.rand(1)
        if (g<0.5):
            x[i] = inv_g_pos(g)
        else:
            x[i] = inv_g_neg(g)
    sx = np.std(x, ddof=1)
    print("desvio-padrão amostral de x: %.6f" % (sx))
    print("Frequencia Relativa s0: %.6f" % (np.sum(np.abs(x)<(L*math.sqrt(2)))/N))
    

