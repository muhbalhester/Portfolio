# -*- coding: utf-8 -*-
"""
Incerteza em contagens
"""

import numpy as np # Biblioteca para manipulação númerica
import matplotlib.pyplot as plt # Biblioteca para visualização e gráficos
import scipy.stats as st # Biblioteca de funções estatísticas
import math as ma

def gen_fdp(N):
    xmin = 0
    xmax = 5
    ymax = (5**3)/125
    f = lambda x : (3/125)*(x**2)  
    i = 0
    x = np.zeros(N)
    while i < N:
        x_cand = xmin + (xmax - xmin) * np.random.rand()
        y_test = ymax * np.random.rand()
        if y_test <= f(x_cand):
            x[i] = x_cand
            i += 1
    return x

def ex1(N):
    x = gen_fdp(200)
    y = np.zeros(5)
    a = np.sum(x<1)
    b = np.sum(x<2) -a
    c = np.sum(x<3) -a -b
    d = np.sum(x<4) -a -b -c
    e = N -a -b -c -d
    y[0] = a
    y[1] = b
    y[2] = c
    y[3] = d
    y[4] = e
    #print("0->1: %.6f" % (a))
    #print("1->2: %.6f" % (b))
    #print("2->3: %.6f" % (c))
    #print("3->4: %.6f" % (d))
    #print("4->5: %.6f" % (e))
    return y
    
def ex2(nREP,N):
    z = np.zeros((5,nREP))
    i = 0
    while i < nREP:
        y = ex1(N)
        z[0][i] = y[0]
        z[1][i] = y[1]
        z[2][i] = y[2]
        z[3][i] = y[3]
        z[4][i] = y[4]
        i+=1
    print("0->1, n médio: %.6f" % (np.mean(z[0])))
    print("0->1, incerteza: %.6f" % (np.std(z[0])/ma.sqrt(nREP)))
    print("0->1, desv-pad: %.6f" % (np.std(z[0])))
    print("1->2, n médio: %.6f" % (np.mean(z[1])))
    print("1->2, incerteza: %.6f" % (np.std(z[1])/ma.sqrt(nREP)))
    print("1->2, desv-pad: %.6f" % (np.std(z[1])))
    print("2->3, n médio: %.6f" % (np.mean(z[2])))
    print("2->3, incerteza: %.6f" % (np.std(z[2])/ma.sqrt(nREP)))
    print("2->3, desv-pad: %.6f" % (np.std(z[2])))
    print("3->4, n médio: %.6f" % (np.mean(z[3])))
    print("3->4, incerteza: %.6f" % (np.std(z[3])/ma.sqrt(nREP)))
    print("3->4, desv-pad: %.6f" % (np.std(z[3])))
    print("4->5, n médio: %.6f" % (np.mean(z[4])))
    print("4->5, incerteza: %.6f" % (np.std(z[4])/ma.sqrt(nREP)))
    print("4->5, desv-pad: %.6f" % (np.std(z[4])))
        











