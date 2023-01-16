# -*- coding: utf-8 -*-
"""
Utilização de Monte Carlo para propagação de incertezas.
"""

import numpy as np # Biblioteca para manipulação númerica
import matplotlib.pyplot as plt # Biblioteca para visualização e gráficos
import scipy.stats as st # Biblioteca de funções estatísticas
import math

def printGraphs(data):
    plt.plot(data, '*')
    plt.show()
    plt.hist(data)
    plt.show()

# Exercício 1
def simulate_ex1(m,sigma,N,graph):
    mat_dados = np.zeros([2,N])
    #print(mat_dados)
    for i in range(N-1):
        #print(i)
        mat_dados[0][i] = m + (sigma * np.random.randn())
        mat_dados[1][i] = math.pi * (mat_dados[0][i] ** 2)
    media = np.mean(mat_dados[1])
    desvpad = np.std(mat_dados[1], ddof=1)
    desvpad_med = desvpad/(math.sqrt(N))
    print("Média: %.7f, Desvpad: %.7f , Desvpad_Média: %.7f" % (media, desvpad, desvpad_med))
    if graph == 1:
        printGraphs(mat_dados[1])

# Exercício 2
def simulate_ex2(m,sigma,N,graph):
    mat_dados = np.zeros([2,N])
    #print(mat_dados)
    for i in range(N-1):
        #print(i)
        mat_dados[0][i] = m + (sigma * np.random.randn())
        mat_dados[1][i] = mat_dados[0][i] ** 3
    media = np.mean(mat_dados[1])
    desvpad = np.std(mat_dados[1], ddof=1)
    desvpad_med = desvpad/(math.sqrt(N))
    print("Média: %.7f, Desvpad: %.7f , Desvpad_Média: %.7f" % (media, desvpad, desvpad_med))
    if graph == 1:
        printGraphs(mat_dados[1])
    
# Exercício 3a
def simulate_ex3a(a,b,sigma_a,sigma_b,N,graph):
    mat_dados = np.zeros([3,N])
    #print(mat_dados)
    for i in range(N-1):
        #print(i)
        mat_dados[0][i] = a + (sigma_a * np.random.randn())
        mat_dados[1][i] = b + (sigma_b * np.random.randn())
        mat_dados[2][i] = mat_dados[0][i]/mat_dados[1][i]
    media = np.mean(mat_dados[2])
    desvpad = np.std(mat_dados[2], ddof=1)
    desvpad_med = desvpad/(math.sqrt(N))
    print("Média: %.7f, Desvpad: %.7f , Desvpad_Média: %.7f" % (media, desvpad, desvpad_med))
    if graph == 1:
        printGraphs(mat_dados[2])

# Exercício 3b e c
def simulate_ex3bc(fix,m_fix,x,sigma,N,graph):
    mat_dados = np.zeros([2,N])
    #print(mat_dados)
    for i in range(N-1):
        #print(i)
        mat_dados[0][i] = x + (sigma * np.random.randn())
        # se fix = 1 fixa o valor de 'a' com m_fix, se fix == 0 fixa o valor de
        # 'b' com m_fix.
        if fix == 1:
            mat_dados[1][i] = m_fix/mat_dados[0][i]
        else:
            mat_dados[1][i] = mat_dados[0][i]/m_fix
    media = np.mean(mat_dados[1])
    desvpad = np.std(mat_dados[1], ddof=1)
    desvpad_med = desvpad/(math.sqrt(N))
    if fix == 1:
        print('a fixado')
    else:
        print('b fixado')
    print("Média: %.7f, Desvpad: %.7f , Desvpad_Média: %.7f" % (media, desvpad, desvpad_med))
    if graph == 1:
        printGraphs(mat_dados[1])