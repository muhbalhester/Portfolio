# -*- coding: utf-8 -*-
"""
Propagação de Incerteza em planejamento de experimentos.
"""
import numpy as np # Biblioteca para manipulação númerica
import matplotlib.pyplot as plt # Biblioteca para visualização e gráficos
import scipy.stats as st # Biblioteca de funções estatísticas
import math as ma

def ex_1a(x0,y0,sx,sy,M):
    x = x0 + sx*np.random.randn(M)
    y = y0 + sy*np.random.randn(M)
    w = x*y
    wm = np.mean(w)
    ws = np.std(w, ddof=1)
    winc = ws/(ma.sqrt(M))
    print("média de x: %.6f # %.6f" % (wm,winc))
    print("desvio-padrão amostral de x: %.6f" % (ws))

def ex_1b(x0,y0,sx,sy,M):
    x1 = x0 + sx*np.random.randn(M)
    x2 = x0 + sx*np.random.randn(M)
    xm = np.zeros(M)
    i = 0
    while i<M:
        xm[i] = np.mean((x1[i],x2[i]))
        i+=1
    y = y0 + sy*np.random.randn(M)
    w = xm*y
    wm = np.mean(w)
    ws = np.std(w, ddof=1)
    winc = ws/(ma.sqrt(M))
    print("média de x: %.6f # %.6f" % (wm,winc))
    print("desvio-padrão amostral de x: %.6f" % (ws))
    
def ex_1c(x0,y0,sx,sy,M):
    x = x0 + sx*np.random.randn(M)
    y1 = y0 + sy*np.random.randn(M)
    y2 = y0 + sy*np.random.randn(M)
    ym = np.zeros(M)
    i = 0
    while i<M:
        ym[i] = np.mean((y1[i],y2[i]))
        i+=1
    w = x*ym
    wm = np.mean(w)
    ws = np.std(w, ddof=1)
    winc = ws/(ma.sqrt(M))
    print("média de x: %.6f # %.6f" % (wm,winc))
    print("desvio-padrão amostral de x: %.6f" % (ws))
    
def ex_2(x0,y0,sx,sy,N,M):
    i = 0
    Nx = 1
    Ny = N - 1
    while i<(N-1):
        j = 0
        w = np.zeros(M)
        while j<M:
            x = x0 + sx*np.random.randn(Nx)
            xm = np.mean(x)
            y = y0 + sy*np.random.randn(Ny)
            ym = np.mean(y)
            w[j] = xm*ym
            j+=1
        wm = np.mean(w)
        ws = np.std(w, ddof=1)
        winc = ws/(ma.sqrt(M))
        print("----------------------------------")
        print("Nx = %.0f , Ny = %.0f" % (Nx,Ny))
        print("média de w: %.6f # %.6f" % (wm,winc))
        print("desvio-padrão amostral de w: %.6f" % (ws))
        Nx+=1
        Ny = N - Nx
        i+=1










