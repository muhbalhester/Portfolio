# Exercício Programa - Calculo Numérico
# Murilo Balhester de Andrade  NUSP 11224682


# Utilizo a biblioteca math somente para usar o valor da exponencial no
# calculo da solução analitica.
import math

#------------------------------------------------------------------------
# Caso queira a saida do calculo da equação logistica em um arquivo .txt, 
# descomente as linhas abaixo e as linhas 131 a 137.

# output = open("Saida.txt", "r+")
# output.truncate(0)
# output.close()

#------------------------------------------------------------------------

# Defino as variáveis globais do programa.

e = math.e
animais = ['coelho','lebre','raposa']

# Abre o arquivo com os dados e inicia as matrizes que vão manter esses dados.
# Essa variáveis são definidas globalmente e serão chamadas diretamente pelas
# funções.
dados_arq = open('EP - Calculo Numérico - Dados.txt', 'r')
linhas = dados_arq.readlines()
m = int(linhas[0].split()[0])
tf = float(linhas[0].split()[1])
i = 1
X0 = []
B = []
A = []

# Salva os dados do arquivo nas matrizes.
while i < len(linhas):
    T = linhas[i].split()
    j = 0
    Ai = []
    while j < len(T):
        if (j == 0):
            X0.append(float(T[j]))
        if (j == 1):
            B.append(float(T[j]))
        if (j > 1):
            Ai.append(float(T[j]))
        j+=1
    A.append(Ai)
    i+=1

# Pergunta o valor de n inicial e o erro máximo para os casos Presa-Predador
if (m != 1):
    print("Digite o n inicial:")
    alfa = int(input())
    print("Digite a precisão:")
    precisao = float(input())

# Essa função inicia a resolução do sistema. Ela é chamado no final do programa.
def solve():
    # Verifica se deve resolver a equação Logística(m=1) ou Presa-Predador(m>1).
    if(m == 1):
        # n é a matriz que define as iterações de refinamento dos intervalos.
        n = [10,20,40,80,160,320,640]
        # d conta quantas iterações foram realizadas.
        d = 0
        # Resultados guarda as soluções.
        Resultados = []
        # Esse bloco faz as iterações de refinamento. 
        for i in n:
            # Dados_n guarda os resultados para a iteração com n partições.
            Dados_n = []
            t = range(i+1)
            # x_A é a matriz que guarda os valores analiticos.
            x_A = analitico(i)
            # x_RK é a matriz que guarda os resultados por Runge-Kutta.
            x_RK = runge(i)
            # x_E é a matrix que guarda os resultados por Euler.
            x_E = euler(i)
            # As mattrizes erro_E e erro_RK, guardam a diferença entre o valor
            # analitico e cada simulação para cada passo t da iteração.
            erro_E = []
            erro_RK = []
            for k in t:
                erro_E.append(abs(x_E[0][k]-x_A[k]))
                erro_RK.append(abs(x_RK[0][k]-x_A[k]))
            # Guardo os resultados finais para essa iteração.
            Dados_n.append(i)
            Dados_n.append(x_A)
            Dados_n.append(x_E)
            Dados_n.append(x_RK)
            Dados_n.append(erro_E)
            Dados_n.append(erro_RK)
            Resultados.append(Dados_n)
            # Exibe o número de partições n, os erros máximos para cada método
            # e a razão entro o maior erro de cada método para essa iteração e
            # iteração anterior
            print("-------------------------------------------------------------")
            print("Para n= %.0i" % i)
            print("Analitico -> População final: %.6f" % x_A[-1])
            print("Runge-Kutta -> População final: %.6f" % x_RK[0][-1])
            print("Euler -> População final: %.6f" % x_E[0][-1])
            print("Norma Máxima do Erro (Método Runge-Kutta): %.6f" % max(erro_RK))
            print("Norma Máxima do Erro (Método Euler): %.6f" % max(erro_E))
            if (d > 0):
                raz_erro_RK = max(Resultados[d][5])/max(Resultados[d-1][5])
                raz_erro_E = max(Resultados[d][4])/max(Resultados[d-1][4])
                print("Razão do Erro (Método de Runge-Kutta): %.6f" % (raz_erro_RK))
                print("Razão do Erro (Euler): %.6f" % (raz_erro_E))
            #------------------------------------------------------------------
            # Abaixo imprime os valores para cada n em um arquivo .txt
            # 
            # output = open("Saida.txt", "a")
            # titulo = '\n{:^5}|{:^14}|{:^14}|{:^14}'.format("n","Analitico","Runge-Kutta","Euler")
            # output.write(titulo)
            # for r in t:
            #     linha = '\n{:>5}|{:>14.4f}|{:>14.4f}|{:>14.4f}'.format(r,Resultados[d][1][r],Resultados[d][3][0][r],Resultados[d][2][0][r])
            #     output.write(linha)
            # output.close()
            # 
            #------------------------------------------------------------------
            # Abaixo imprime os resultados para cada passo n
            #
            # print('{:^5}|{:^14}|{:^14}|{:^14}'.format("n","Analitico","Runge-Kutta","Euler"))
            # for r in t:
            #     print('{:>5}|{:>14.4f}|{:>14.4f}|{:>14.4f}'.format(r,Resultados[d][1][r],Resultados[d][3][0][r],Resultados[d][2][0][r]))
            #------------------------------------------------------------------
            d+=1
        # Aqui termina a execução para o caso da Equação Logística
    else:
        # Aqui começa a resolução do sistema Presa-Predador.
        # i_RK conta as iterações do método de Runge-Kutta
        i_RK = 0
        # Resultados_RK guarda o resultado de todas as iterações por esse método em
        # uma matriz em que o índice representa o i-ésimo refinamento do resultado.
        # Cada refinamento guarda é matriz com os dados desse refinamento.
        # O índice [0] guarda o valor de n utilizado.
        # O índice [1] guarda a matriz retornada pela função que calcula a solução do
        # sistema pelo método Runge-Kutta, sendo o primeiro índice a i-esima população
        # e o segundo índice é a população no passo t.
        # O índice [2] guarda uma matriz com uma sequência numérica até n que pode ser 
        # utilizada para impressão de gráficos.
        Resultados_RK = []
        # erro_RK é 0 se a iteração ainda não atingiu a precisão e muda
        # para 1 quando atinge, parando as iterações.
        erro_RK = 0
        while erro_RK == 0:
            # n inicia no valor de n inicial solicitado e dobra a cada iteração.
            n = alfa*(2**i_RK)
            t = range(n+1)
            # x_RK guarda os resultados do método de Runge-Kutta para n passos.
            x_RK = runge(n)
            # Guarda os resultados dessa iteração. Resultados_RK guarda os 
            # resultados de todas as iterações.
            Dados_n = []
            Dados_n.append(n)
            Dados_n.append(x_RK)
            Dados_n.append(t)
            Resultados_RK.append(Dados_n)
            # dif guarda as diferenças entre iterações seguidas para cada
            # população no instante final.
            dif = []
            if (len(Resultados_RK) == 1):
                a = 0
                while a < m:
                    dif.append(abs(Resultados_RK[i_RK][1][a][-1] - X0[a]))
                    a+=1
            else:
                a = 0
                while a < m:
                    dif.append(abs(Resultados_RK[i_RK][1][a][-1] - Resultados_RK[i_RK-1][1][a][-1]))
                    a+=1
            # Se o maior valor das diferenças entre essa iteração e a anterior
            # for menor que a precisão definida, muda erro_RK para 1 parando as
            # iterações.
            if (max(dif) <= precisao):
                erro_RK = 1
            # Printa os resultados do método de Runge-Kutta para cada n.
            print("-------------------------------------------------------------")
            print("Runge-Kutta -> n= %.0i" % n)
            for c in range(m):
                print("População de %s: %0.6f" % (animais[c],Resultados_RK[-1][1][c][-1]))
            i_RK+=1
    print("-------------------------------------------------------------")
    print("Fim do programa")

# A função analitico(n) calcula o valor analitico da equação logística nos n
# passos.
def analitico(n):
    # i conta os passos
    i = 0
    # h é o tamanho dos passos.
    h = (tf)/n
    # M e l são constantes da equação.
    M = B[0]/A[0][0]
    l = 1/B[0]
    # xt guarda os valores da função para cada i
    xt = []
    while i <= n:
        # Calcula e guarda o valor da função no ponto t.
        t = (i)*h
        xt.append(M/(1+((M/X0[0])-1)*e**(-l*t)))
        i+=1
    return xt

# A função runge(n) calcula a solução do sistema pelo método de Runge-Kutta de
# 4 ordem para n passos.
def runge(n):
    # Ft guarda os valores de cada população em cada momento t.
    Ft = []
    # Ft = [[x(0),x(1), ... , x(n)],
    #       [y(0),y(1), ... , y(n)],
    #        ...]
    i = 0
    while i < m:
        Ft.append([X0[i]])
        i+=1
    # h é o tamanho dos passos.
    h = (tf)/n
    # conta os passos até n iniciando em 1 pois 0 é o valor de X0.
    t = 1
    while t <= n:
        # Calcula os valores de k utilizados pelo método de Runge-Kutta. Como
        # as equações a serem aproximadas dependem da quantidade de variáveis
        # então fazemos duas recorrências, um para adicionar os termos a cada 
        # equação e outra para montar cada equação e já calculando os k.
        i = 0
        while i < m:
            k1 = []
            k2 = []
            k3 = []
            k4 = []
            # Abaixo é o calculo de k1 fazendo a iteração por todos os componentes
            # do sistema.
            i = 0
            while i < m:
                k1.append(B[i])
                j = 0
                while j < m:
                    k1[i] -= (A[i][j]*Ft[j][t-1])
                    j+=1
                k1[i] = k1[i]*Ft[i][t-1]
                i+=1
            # Abaixo é o calculo de k2 fazendo a iteração por todos os componentes
            # do sistema.
            i = 0
            while i < m:
                k2.append(B[i])
                j = 0
                while j < m:
                    k2[i] -= (A[i][j]*(Ft[j][t-1]+(0.5*h*k1[j])))
                    j+=1
                k2[i] = k2[i]*(Ft[i][t-1]+(0.5*h*k1[i]))
                i+=1
            # Abaixo é o calculo de k3 fazendo a iteração por todos os componentes
            # do sistema.
            i = 0
            while i < m:
                k3.append(B[i])
                j = 0
                while j < m:
                    k3[i] -= (A[i][j]*(Ft[j][t-1]+(0.5*h*k2[j])))
                    j+=1
                k3[i] = k3[i]*(Ft[i][t-1]+(0.5*h*k2[i]))
                i+=1
            # Abaixo é o calculo de k4 fazendo a iteração por todos os componentes
            # do sistema.
            i = 0
            while i < m:
                k4.append(B[i])
                j = 0
                while j < m:
                    k4[i] -= (A[i][j]*(Ft[j][t-1]+(h*k3[j])))
                    j+=1
                k4[i] = k4[i]*(Ft[i][t-1]+(h*k3[i]))
                i+=1
            # Abaixo é o calculo do vetor i+1 fazendo a iteração por todos os componentes
            # do sistema.
            i = 0
            while i < m:
                Ft[i].append(Ft[i][t-1]+(h*(k1[i]+(2*k2[i])+(2*k3[i])+k4[i])/6))
                i+=1
        t+=1
    return Ft

# A função euler(n) calcula a solução do sistema pelo método de Euler de
# para n passos.
def euler(n):
    # Ft guarda os valores de cada população em cada momento t.
    Ft = []
    # Ft = [[x(0),x(1), ... , x(n)],
    #       [y(0),y(1), ... , y(n)],
    #        ...]
    i = 0
    while i < m:
        Ft.append([X0[i]])
        i+=1
    # conta os passos até n iniciando em 1 pois 0 é o valor de X0.
    t = 1
    # h é o tamanho dos passos.
    h = tf/n
    while t <= n:
        # Monta as equações a serem utilizadas por recorrência.
        i = 0
        while i < m:
            g = B[i]*Ft[i][t-1]
            j = 0
            while j < m:
                g = g - A[i][j]*Ft[i][t-1]*Ft[j][t-1]
                j+=1
            # Calcula o valor da função para esse t usando a equação montada 
            # nessa iteração para cada i-ésima população.
            Ft[i].append(Ft[i][t-1] + h*g)
            i+=1
        t+=1
    return Ft

# Chama a função que inicia a solução do sistema.
solve()
