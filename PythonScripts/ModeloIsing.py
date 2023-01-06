# Importação das bibliotecas necessárias. Numpy para manipular matrizes e Matplotlib
# para a impressão dos gráficos
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#kb: é a constante de Boltzmann
kb = 1
#exc: constante de exclusão, indica a porcentagem inicial de varreduras a descartar
exc = 0.1
#seed: seed da configuração aleatória
seed = 99

'''
 metro(N,t,h,J,Nvar): é a função que executa o algoritmo de Metropolis, utilizando
uma configuração aleatória de spins a cada execução. Retorna 4 matrizes:
matriz 1: magnetização média dos Nvar*exc últimos valores de magnetização da rede.
matriz 2: energia média dos Nvar*exc últimos valores de energia da rede.
matriz 3: magnetização média quadrática dos Nvar*exc últimos valores de magnetização da rede.
matriz 4: energia média quadrática dos Nvar*exc últimos valores de energia da rede.
dados os parãmetros:
N: é o tamanho do lado da rede, ou seja, cria uma rede de NxN spins.
t: é a temperatura da simulação.
h: é a intensidade do campo externo.
J: é o fator de interação de curto alcance entre os spins.
Nvar: é o número de varreduras a ser realizado sobre a rede.
'''
def metro(N,t,h,J,Nvar):
  m = np.zeros(Nvar)
  e = np.zeros(Nvar)
  # configuração incial aleatória
  np.random.seed(seed)
  s = np.random.choice([-1,1],(N,N))
  # calculo da energia inicial
  s_l = np.roll(s,-1,1)
  s_r = np.roll(s,1,1)
  s_u = np.roll(s,-1,0)
  s_d = np.roll(s,1,0)
  e[0] = (-J*(np.sum(s*s_l)+np.sum(s*s_r)+np.sum(s*s_u)+np.sum(s*s_d))-h*np.sum(s))/2
  m[0] = (np.sum(s))
  # Algoritmo de Metropolis
  for n in range(1,Nvar):
    e[n] = e[n-1]
    for i in range(-1,N-1):
      for j in range(-1,N-1):
        eflip = 2*J*s[i,j]*(s[i,j-1]+s[i,j+1]+s[i+1,j]+s[i-1,j])+2*h*s[i,j]
        if (eflip<0):
          e[n] += 2*s[i,j]*(J*(s[i,j-1]+s[i,j+1]+s[i+1,j]+s[i-1,j])+h)
          s[i,j] = -s[i,j]
        else:
          pflip = np.exp(-eflip/(kb*t))
          if (np.random.uniform(0,1) < pflip):
            e[n] += 2*s[i,j]*(J*(s[i,j-1]+s[i,j+1]+s[i+1,j]+s[i-1,j])+h)
            s[i,j] = -s[i,j]
    m[n] = (np.sum(s))
  # média de energia e magnetização
  e = e/(N**2)
  m = m/(N**2)
  return np.mean(m[int(round(Nvar*exc)):]),np.mean(e[int(round(Nvar*exc)):]),np.mean(m[int(round(Nvar*exc)):]**2),np.mean(e[int(round(Nvar*exc)):]**2)

'''
 metro_dominio(N,t,h,J,Nvar): é a função que executa o algoritmo de Metropolis, utilizando
uma configuração aleatória de spins a cada execução. Retorna 1 matriz:
matriz 1: magnetização a cada varredura
dados os parãmetros:
N: é o tamanho do lado da rede, ou seja, cria uma rede de NxN spins.
t: é a temperatura da simulação.
h: é a intensidade do campo externo.
J: é o fator de interação de curto alcance entre os spins.
Nvar: é o número de varreduras a ser realizado sobre a rede.
'''
def metro_dominio(N,t,h,J,Nvar):
  m = np.zeros(Nvar)
  # configuração incial aleatória
  np.random.seed(seed)
  s = np.random.choice([-1,1],(N,N))
  m[0] = (np.sum(s))
  # Algoritmo de Metropolis
  for n in range(1,Nvar):
    for i in range(-1,N-1):
      for j in range(-1,N-1):
        eflip = 2*J*s[i,j]*(s[i,j-1]+s[i,j+1]+s[i+1,j]+s[i-1,j])+2*h*s[i,j]
        if (eflip<0):
          s[i,j] = -s[i,j]
        else:
          pflip = np.exp(-eflip/(kb*t))
          if (np.random.uniform(0,1) < pflip):
            s[i,j] = -s[i,j]
    m[n] = (np.sum(s))
  return m

'''
 dominios(N,t,h,J,Nvar): Função utilizada para exibir a magnetização média por varredura.
dados os parãmetros:
N: é o tamanho do lado da rede, ou seja, cria uma rede de NxN spins.
Ti,Tf,dT: temperatura inicial, final e passo de temperatura.
h: é a intensidade do campo externo.
J: é o fator de interação de curto alcance entre os spins.
Nvar: é o número de varreduras a ser realizado sobre a rede.
'''
def dominios(N,Ti,Tf,dT,h,J,Nvar):
  T = np.arange(Ti,Tf,dT)
  plt.rc('font', size=16)
  fig, ax = plt.subplots(len(T)-1,1,figsize=(8,21))
  for ii in range(len(T)-1):
    M = np.zeros(Nvar)
    M = metro_dominio(N,T[ii],h,J,Nvar)
    ax[ii].scatter(np.arange(0,Nvar,1), M/(N**2), s=30)
    ax[ii].set_ylabel('Magnetização média - <m>')
    ax[ii].set_title('Magnetização a campo nulo - T='+str("{:.2f}".format(T[ii])))
    ax[ii].set_xlabel('Evolução temporal da Simulação (n-ésima Varredura)')
  plt.show()

'''
 termo(N,t,h,J,Nvar): Função utilizada para calcular e exibir os parametros magnetização média,
energia média, calor especifico, susceptibilidade magnetica e expoente critico beta, dado um range
de temperaturas e tamanho de rede.
dados os parãmetros:
Ti,Tf,dT: temperatura inicial, final e passo de temperatura.
Ni,Nf,dN: Tamanho de rede inicial, final e incremento de N.
h: é a intensidade do campo externo.
J: é o fator de interação de curto alcance entre os spins.
Nvar: é o número de varreduras a ser realizado sobre a rede.
'''
def termo(Ti,Tf,Ni,Nf,dN,dT,h,J,Nvar):
  T = np.arange(Ti,Tf,dT)
  N = np.arange(Ni,Nf,dN)
  M = np.zeros((len(N),len(T)))
  E = np.zeros((len(N),len(T)))
  M2 = np.zeros((len(N),len(T)))
  E2 = np.zeros((len(N),len(T)))
  for ni,n in np.ndenumerate(N):
    for ti,t in np.ndenumerate(T):
      M[ni,ti], E[ni,ti], M2[ni,ti], E2[ni,ti] = metro(n,t,h,J,Nvar)
  # Magnetização média
  plt.rc('font', size=16)
  fig, ax = plt.subplots(figsize=(8,7))
  for ii in range(len(N)):
    ax.scatter(T, np.abs(M[ii]), label='N='+str(N[ii]), s=30)
  ax.axvline(x=2.269, color='black', linestyle='dashed', label=r'$T_c$')
  ax.set_xlabel('Temperatura - T')
  ax.set_ylabel('Magnetização média - <m>')
  ax.set_title('Magnetização a campo nulo')
  ax.legend(title='Rede')
  plt.show()
  # Energia média
  plt.rc('font', size=16)
  fig, ax = plt.subplots(figsize=(8,7))
  for ii in range(len(N)):
    ax.scatter(T, E[ii], label='N='+str(N[ii]), s=30)
  ax.axvline(x=2.269, color='black', linestyle='dashed', label=r'$T_c$')
  ax.set_xlabel('Temperatura - T')
  ax.set_ylabel('Energia média - <E>')
  ax.set_title('Energia média em função da Temperatura')
  ax.legend(title='Rede')
  plt.show()
  # Calor Específico
  plt.rc('font', size=16)
  fig, ax = plt.subplots(figsize=(8,7))
  for ii in range(len(N)):
    ax.plot(T, (N[ii]**2)*(E2[ii]-(E[ii]**2))/((T**2)), label='N='+str(N[ii]))
  ax.axvline(x=2.269, color='black', linestyle='dashed', label=r'$T_c$')
  ax.set_xlim(2,2.9)
  ax.set_ylim(0,3)
  ax.set_xlabel('Temperatura - T')
  ax.set_ylabel('Calor Específico')
  ax.set_title('Calor Específico')
  ax.legend(title='Rede')
  plt.show()
  # Susceptibilidade Magnética
  plt.rc('font', size=16)
  fig, ax = plt.subplots(figsize=(8,7))
  for ii in range(len(N)):
    ax.plot(T, (N[ii]**2)*(M2[ii]-(M[ii]**2))/((T)), label='N='+str(N[ii]))
  ax.axvline(x=2.269, color='black', linestyle='dashed', label=r'$T_c$')
  ax.set_xlim(2,2.9)
  ax.set_ylim(0,100)
  ax.set_xlabel('Temperatura - T')
  ax.set_ylabel(r'$\chi$')
  ax.set_title('Susceptibilidade Magnética')
  ax.legend(title='Rede')
  plt.show()
  # Ajuste linear do expoente crítico beta
  plt.rc('font', size=16)
  fig, ax = plt.subplots(figsize=(12,7))
  for ii in range(len(N)):
    T2 = np.argwhere((T-2.269)/2.269 <0).flatten()
    Tn = np.abs((T[T2]-2.269)/2.269)
    linear_model=np.polyfit(np.log10(Tn),np.log10(np.abs(M[ii,T2])),1)
    linear_model_fn=np.poly1d(linear_model)
    ax.plot(Tn,(Tn**(linear_model_fn[1])*(10**linear_model_fn[0])))
    ax.scatter(Tn, M[ii,T2], label=r'N='+str(N[ii])+r', $\beta= $'+str("{:.4f}".format(linear_model_fn[1])), s=30)
  ax.set_xscale('log')
  ax.set_yscale('log')
  ax.set_xlabel('Temperatura - log(T)')
  ax.set_ylabel('Magnetização média - log(<m>)')
  ax.set_title('Expoente Crítico de magnetização a campo nulo')
  ax.legend(title='Rede - Expoente')
  plt.show()

'''
 campo_externo(Ti,Tf,Hi,Hf,dH,dT,N,J,Nvar): Função utilizada para calcular a magnetização média
da rede sob a influência de um campo externo h, num range especificado em um range de temperatura
especificado, imprimindo o resultado.
dados os parãmetros:
Ti,Tf,dT: temperatura inicial, final e passo de temperatura.
Hi,Hf,dH: intesidade inicial, final e incremento do campo externo
N: é o tamanho da rede.
J: é o fator de interação de curto alcance entre os spins.
Nvar: é o número de varreduras a ser realizado sobre a rede.
'''
def campo_externo(Ti,Tf,Hi,Hf,dH,dT,N,J,Nvar):
  T = np.arange(Ti,Tf,dT)
  H = np.arange(Hi,Hf,dH)
  M = np.zeros((len(H),len(T)))
  E = np.zeros((len(H),len(T)))
  M2 = np.zeros((len(H),len(T)))
  E2 = np.zeros((len(H),len(T)))
  for hi,h in np.ndenumerate(H):
    for ti,t in np.ndenumerate(T):
      M[hi,ti], E[hi,ti], M2[hi,ti], E2[hi,ti] = metro(N,t,h,J,Nvar)
  plt.rc('font', size=16)
  fig, ax = plt.subplots(figsize=(8,7))
  for ii in range(len(H)):
    ax.plot(T, np.abs(M[ii]), label='H='+str(H[ii]))
  ax.axvline(x=2.269, color='black', linestyle='dashed', label=r'$T_c$')
  ax.axhline(y=0, color='black', linestyle='dashed')
  ax.set_xlabel('Temperatura - T')
  ax.set_ylabel('Magnetização média - <m>')
  ax.set_title('Magnetização a campo não nulo')
  ax.legend(title='Intensidade Campo')
  plt.show()

# mostrar a mudança de domínios.
dominios(20,2,2.7,0.2,0,1,10000)
# mostrar os parâmetros do sistema.
termo(1,3,20,41,5,0.1,0,1,1500)
# mostrar a influencia do campo externo.
campo_externo(0.5,4,0,5,1,0.1,20,1,1500)