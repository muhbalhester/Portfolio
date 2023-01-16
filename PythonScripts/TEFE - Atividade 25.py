# -*- coding: utf-8 -*-
"""
Ajuste de dados por MMQ e Monte Carlo
"""

import numpy as np # Biblioteca para manipulação númerica
import matplotlib.pyplot as plt # Biblioteca para visualização e gráficos
import scipy.stats as st # Biblioteca de funções estatísticas
import math as ma

def matrizCov(M,g,gs):
    for i in range(len(M)):
        for j in range(len(M[i])):
            M[i][j] = np.sum(g[i]*g[j]/(gs**2))
    return M

def vetorB(M,g,gs,y):
    b = np.zeros(len(M[0]-1))
    for i in range(len(M)):
        b[i] = np.sum((g[i]*y)/(gs**2))
    return b

def parteA():
    t = np.array([0,1,2,3,4,5,6,7,8,9,10])
    sL = 0.5
    M = np.zeros([2,2])
    g = np.zeros([2,len(t)])
    for i in range(len(t)):
        g[0][i] = 1
        g[1][i] = t[i]
    M = matrizCov(M,g,sL)
    M_inv = np.linalg.inv(M)
    sa = ma.sqrt(M_inv[0][0])
    sb = ma.sqrt(M_inv[1][1])
    rho = M_inv[0][1]/(sa*sb)
    a0 = 20
    b0 = 3
    y = (a0 + t*b0) + sL*np.random.randn(len(t))
    b = vetorB(M,g,sL,y)
    param = np.array(2)
    param = M_inv @ b
    chi = np.sum(((y-(param[0]*g[0]+param[1]*g[1]))/sL)**2)
    Ri = y - (param[0]*g[0] + param[1]*g[1])
    print('a : %.6g (%.6g) cm' % (param[0],sa))
    print('b : %.6g (%.6g) cm/s' % (param[1],sb))
    print('cov(a,b): %.6g cm2' % M_inv[0][1])
    print('rho: %.3f' % rho)
    print('chi: %.6f' % chi)
    print('NGL: %.6f' % (len(y)-len(param)))
    plt.plot(t,y,"*")
    plt.plot(t,(param[0]*g[0] + param[1]*g[1]),'-')
    plt.title('Ajuste dos Dados')
    plt.ylabel('Distância - cm')
    plt.xlabel('Tempo - s')
    plt.show()
    plt.plot(t,Ri,"-")
    plt.title('Resíduos')
    plt.ylabel('Distância - cm')
    plt.xlabel('Tempo - s')
    plt.show()
    
def parteB():
    t = np.array([0,1,2,3,4,5,6,7,8,9,10])
    sL = 0.5
    M = np.zeros([2,2])
    g = np.zeros([2,len(t)])
    for i in range(len(t)):
        g[0][i] = 1
        g[1][i] = t[i]
    M = matrizCov(M,g,sL)
    M_inv = np.linalg.inv(M)
    a0 = 20
    b0 = 3
    y = (a0 + t*b0) + sL*np.random.randn(len(t))
    b = vetorB(M,g,sL,y)
    param = np.array(2)
    param = M_inv @ b
    chi = np.sum(((y-(param[0]*g[0]+param[1]*g[1]))/sL)**2)
    return param,chi

def parteC(nRep):
    E = np.zeros([3,nRep])
    for i in range(nRep):
        p,c = parteB()
        E[0][i] = p[0]
        E[1][i] = p[1]
        E[2][i] = c
    am = np.mean(E[0])
    sa = np.std(E[0], ddof=1)
    ams = sa/ma.sqrt(nRep)
    ssa = sa/(ma.sqrt(2*(nRep-1)))
    bm = np.mean(E[1])
    sb = np.std(E[1], ddof=1)
    bms = sb/ma.sqrt(nRep)
    ssb = sb/(ma.sqrt(2*(nRep-1)))
    cov = np.sum((E[0]-am)*(E[1]-bm))/(nRep-1)
    R = cov/(sa*sb)
    sR = (1-R**2)/(ma.sqrt(nRep-1))
    chim = np.mean(E[2])
    schim = np.std(E[2])/(ma.sqrt(nRep))
    print('a        : %.6g (%.2g) cm' % (am,ams))
    print('desvpad a: %.6g (%.2g) cm' % (sa,ssa))
    print('b        : %.6g (%.2g) cm/s' % (bm,bms))
    print('desvpad b: %.6g (%.2g) cm/s' % (sb,ssb))
    print('Covariancia: %.6f' % (cov))
    print('Correlação: %.6g (%.2g)' % (R,sR))
    print('chi2     : %.6g (%.2g)' % (chim,schim))
    plt.plot(E[0],E[1],'*')
    plt.title('Dispersão entre alfa e beta')
    plt.ylabel('Beta (cm/s)')
    plt.xlabel('Alfa (cm)')
    plt.show()
    plt.hist(E[0])
    plt.title('Histograma - Parâmetro Alfa')
    plt.ylabel('# de Ocorrências')
    plt.xlabel('Canais de Alfa - cm')
    plt.show()
    plt.hist(E[1])
    plt.title('Histograma - Parâmetro Beta')
    plt.ylabel('# de Ocorrências')
    plt.xlabel('Canais de Beta - cm/s')
    plt.show()
    plt.hist(E[2])
    plt.title('Histograma - Chi2')
    plt.ylabel('# de Ocorrências')
    plt.xlabel('Canais de Chi2')
    plt.show()