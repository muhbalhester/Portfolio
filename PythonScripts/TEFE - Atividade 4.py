# -*- coding: utf-8 -*-
"""
Monte Carlo para simulação de experimentos e propagação de incerteza.
"""
import numpy as np # Biblioteca para manipulação númerica
import matplotlib.pyplot as plt # Biblioteca para visualização e gráficos
import scipy.stats as st # Biblioteca de funções estatísticas
import math

def ex1(x0,s_x,N):
    x = x0 + (s_x*np.random.randn(N))
    y = np.sin((x*math.pi)/180)
    print("Média: %.6f" % (np.mean(y)))
    print("Desvpad: %.6f" % (np.std(y, ddof=1)))
    print("Incerteza: %.6f" % (np.std(y, ddof=1)/(math.sqrt(N))))
    
def ex2(x0,eA,eS,n,M):
    z = np.zeros(M-1)
    for i in range(M-1):
        eS_i = eS*np.random.randn(1)
        x = x0 + eS_i + eA*np.random.randn(n) 
        z[i] = np.mean(x)
    s_z = np.std(z, ddof=1)
    print("Incerteza de M Experimentos: %.6f" % (s_z))
    print("Experimentos acima da x0: %.0f" % (np.sum(z>x0)))
    print("Diferença entre x e x0 menor que a incerteza: %.0f" % (np.sum(np.abs(z-x0)<s_z)))

def ex3(x0,eA,n,M):
    z = np.zeros(M-1)
    for i in range(M-1):
        x = x0 + eA*np.random.randn(n) 
        z[i] = np.mean(x)
    a = (2*34)/(z**2)
    s_a = np.std(a, ddof=1)
    a_real = (2*34)/(x0**2)
    print("Incerteza de M Experimentos: %.6f" % (s_a))
    print("Experimentos acima da x0: %.0f" % (np.sum(a>a_real)))
    print("Diferença entre x e x0 menor que a incerteza: %.0f" % (np.sum(np.abs(a-a_real)<s_a)))
    
def ex4(x0,eA,n,M):
    z = np.zeros(M-1)
    for i in range(M-1):
        x = x0 + eA*np.random.randn(n) 
        a_i = (2*34)/(x**2)
        z[i] = np.mean(a_i)
    s_a = np.std(z, ddof=1)
    a_real = (2*34)/(x0**2)
    print("Incerteza de M Experimentos: %.6f" % (s_a))
    print("Experimentos acima da x0: %.0f" % (np.sum(z>a_real)))
    print("Diferença entre x e x0 menor que a incerteza: %.0f" % (np.sum(np.abs(z-a_real)<s_a)))




