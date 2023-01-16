def le_percepcao(a):
  if a == 0:
    cel_content = ''
  if a == 1:
    cel_content = 'R'
  if a == 10:
    cel_content = 'B'
  if a == 100:
    cel_content = 'F'
  if a == 11:
    cel_content = 'BR'
  if a == 101:
    cel_content = 'FR'
  if a == 110:
    cel_content = 'FB'
  if a == 111:
    cel_content = 'FBR'
  if a == -1:
    cel_content = '?'
  return cel_content
      
def le_mundo():
  mapa_arq = open('entrada.txt', 'r')         # Abre o arquivo do mapa da caverna.
  places = mapa_arq.readlines()               # Cria uma lista com os objetos do mapa.
  N = int(places[0][0:1])                     # Extrai o tamanho da caverna.
  mundo = []                                  # Inicia uma matriz para o mapa que sera manipulado.
  l = 0
  while l < (N):                              # Loop para criar as linhas do mapa.
    linha = []                                # Inicia a linha l para incluir as celulas.
    c = 0
    while c < N:                              # Loop para incluir as celulas c da linha atual l.
      linha.append(0)                         # Adiciona a celula a linha com valor 0.
      c+=1
    mundo.append(linha)                       # Adiciona a linha montada ao mapa.
    l+=1
  i = 1
  while i < len(places):                      # Loop pelas linhas do arquivo para adicionar os objetos no mapa.
    mundo[int(places[i][0:1])-1][int(places[i][2:3])-1] = int(places[i][4:5])
    i+=1
  mapa_arq.close                              # Fecha o arquivo do mapa da caverna.
  return mundo                                # Retorna o mapa 

def imprime_mundo(mundo):
  div = '-'                               # Guarda a divisao entre as linhas do mapa.
  t = 0
  while t < len(mundo):                   # Cria a divisao das linhas do mapa do tamanho certo.
    div = div + '--------'
    t+=1
  print(div)
  l = 0
  while l < len(mundo):                   # Loop para exibir as linhas.
    linha = '|'                           # Inicia a linha l.
    c = 0
    while c < len(mundo[l]):              # Loop para adicionar as celulas a linha atual l.
      if mundo[l][c] == 0:                # Se o mapa mostra 0, adiciona um espaco vazio a exibicao.
        linha = linha + '       |'
      if mundo[l][c] == 1:                # Se o mapa mostra 1, adiciona um poco.
        linha = linha + '   P   |'
      if mundo[l][c] == 2:                # Se o mapa mostra 2, adiciona o Wumpus.
        linha = linha + '   W   |'
      if mundo[l][c] == 3:                # Se o mapa mostra 3, adiciona o Ouro.
        linha = linha + '   O   |'
      c+=1
    print(linha)
    print(div)
    l+=1

def imprime_percepcao(percebe, agente):
  div = '-'
  for t in percebe:
    div = div + '--------'
  print(div)
  for l in range(len(percebe)):
    linha = '|'
    cel = ''
    for c in range(len(percebe[l])):
      cel = le_percepcao(percebe[l][c])
      if l == agente[0] and c == agente[1]:
        cel = agente[2] + cel
      if len(cel) == 0:
        cel_str = '       |'
      if len(cel) == 1:
        cel_str = '   '+cel+'   |'
      if len(cel) == 2:
        cel_str = '  '+cel+'   |'
      if len(cel) == 3:
        cel_str = '  '+cel+'  |'
      if len(cel) == 4:
        cel_str = ' '+cel+'  |'
      linha = linha + cel_str
    print(linha)
    print(div)

def atualiza_percepcaoEagente(percebe, mundo, acao, agente, estado):
  alertas = [0,0,0,0,0]                                       # 0: Choque, 1: Urro, 2: Morte [P,W], 3: ouro, 4: Saida
  if acao == 'M' or acao == 'm':
    if agente[2] == '^':
      if agente[0]-1 >= 0:
        agente[0]-=1
      else:
        alertas[0] = 1
    else:
      if agente[2] == '>':
        if agente[1]+1 <= len(mundo)-1:
          agente[1]+=1
        else:
          alertas[0] = 1
      else:
        if agente[2] == 'v':
          if agente[0]+1 <= len(mundo)-1:
            agente[0]+=1
          else:
            alertas[0] = 1
        else:
          if agente[2] == '<':
            if agente[1]-1 >= 0:
              agente[1]-=1
            else:
              alertas[0] = 1
    if mundo[agente[0]][agente[1]] == 1:
      alertas[2] = 'P'
    if mundo[agente[0]][agente[1]] == 2 and estado[0] == 1:
      alertas[2] = 'W'
    if alertas[0] == 0 and alertas[2] == 0:
      sentido = 0
      brisa = 0
      fedor = 0
      reflexo = 0
      if agente[0]+1 < len(mundo)-1:
        if mundo[agente[0]+1][agente[1]] == 1:
          brisa = 1
        if mundo[agente[0]+1][agente[1]] == 2 and estado[0] == 1:
          fedor = 1
      if agente[0]-1 >= 0:
        if mundo[agente[0]-1][agente[1]] == 1:
          brisa = 1
        if mundo[agente[0]-1][agente[1]] == 2 and estado[0] == 1:
          fedor = 1
      if agente[1]+1 < len(mundo)-1:
        if mundo[agente[0]][agente[1]+1] == 1:
          brisa = 1
        if mundo[agente[0]][agente[1]+1] == 2 and estado[0] == 1:
          fedor = 1
      if agente[1]-1 >= 0:
        if mundo[agente[0]][agente[1]-1] == 1:
          brisa = 1
        if mundo[agente[0]][agente[1]-1] == 2 and estado[0] == 1:
          fedor = 1
      if mundo[agente[0]][agente[1]] == 3 and estado[2] == 1:
        reflexo = 1
      if brisa == 1:
        sentido = sentido + 10
      if fedor == 1:
        sentido = sentido + 100
      if reflexo == 1:
        sentido = sentido + 1
      percebe[agente[0]][agente[1]] = sentido
  if acao == 'T' or acao == 't':
    if estado[1] == 1:
      estado[1] = 0
      if agente[2] == '^':
        i = agente[0]
        while i >= 0:
          if mundo[i][agente[1]] == 2:
            estado[0] = 0
            alertas[1] = 1
          i-=1
      else: 
        if agente[2] == '>':
          i = agente[1]
          while i < len(mundo)-1:
            if mundo[agente[0]][i] == 2:
              estado[0] = 0
              alertas[1] = 1
            i+=1
        else:
          if agente[2] == 'v':
            i = agente[0]
            while i < len(mundo)-1:
              if mundo[i][agente[1]] == 2:
                estado[0] = 0
                alertas[1] = 1
              i+=1
          else:
            if agente[2] == '<':
              i = agente[1]
              while i >= 0:
                if mundo[agente[0]][i] == 2:
                  estado[0] = 0
                  alertas[1] = 1
                i-=1
  if acao == 'D' or acao == 'd':
    if agente[2] == '^':
      agente[2] = '>'
    else:
      if agente[2] == '>':
        agente[2] = 'v'
      else:
        if agente[2] == 'v':
          agente[2] = '<'
        else:
          if agente[2] == '<':
            agente[2] = '^'
  if acao == 'E' or acao == 'e':
    if agente[2] == '^':
      agente[2] = '<'
    else:
      if agente[2] == '>':
        agente[2] = '^'
      else:
        if agente[2] == 'v':
          agente[2] = '>'
        else:
          if agente[2] == '<':
            agente[2] = 'v'
  if acao == 'G' or acao == 'g':
    if mundo[agente[0]][agente[1]] == 3:
      if estado[2] == 1:
        alertas[3] = 1
        estado[2] = 0
        percebe[agente[0]][agente[1]]-=1
      else:
        alertas[3] = -1
    else:
      alertas[3] = -1
  if acao == 'S' or acao == 's':
    if agente[0] == len(mundo)-1 and agente[1] == 0:
      alertas[4] = 1
    else:
      alertas[4] = -1
  if alertas[1] == 1:
    estado[3]+=50
  if alertas[4] == 1:
    if estado[2] == 0:
      estado[3]+=100
    else:
      estado[3]-=10000
  if alertas[2] != 0:
    estado[3]-=10000
  if acao != 'S' or acao != 's':
    estado[3]-=1
  return percebe, agente, estado, alertas

def main():
  mundo = le_mundo()
  percebe = []
  for l in range(len(mundo)):
    percebe.append([])
    for c in range(len(mundo[l])):
      if l == (len(mundo)-1) and c == 0:
        percebe[l].append(0)
      else:
        percebe[l].append(-1)
  agente = [len(mundo)-1, 0, '^']
  estado = [1, 1, 1, 0]
  game_state = 0
  print('Percepcao apos a ultima acao:')
  print('[]')
  print('Mundo do Wumpus conhecido pelo agente:')
  imprime_percepcao(percebe, agente)
  acao = input('Digite a acao desejada (M/T/D/E/G/S):')
  while game_state == 0:
    percebe, agente, estado, alertas = atualiza_percepcaoEagente(percebe, mundo, acao, agente, estado)
    percebe_str = le_percepcao(percebe[agente[0]][agente[1]])
    if alertas[0] == 1:
      percebe_str+='C'
    if alertas[1] == 1:
      percebe_str+='U'
    if alertas[2] != 0:
      if alertas[2] == 'P':
        game_state = 1
        print('Mundo Completo!')
        imprime_mundo(mundo)
        print('Fim de Jogo! Voce caiu num poco.')
        print('Pontuacao: ', estado[3])
      if alertas [2] == 'W':
        game_state = 1
        print('Mundo Completo!')
        imprime_mundo(mundo)
        print('Fim de Jogo! Voce foi pego pelo Wumpus.')
        print('Pontuacao: ', estado[3])
    else:
      if alertas[4] == 1:
        if estado[2] == 0:
          game_state = 1
          print('Mundo Completo!')
          imprime_mundo(mundo)
          print('Fim de Jogo! Você saiu da caverna com o ouro!')
          print('Pontuacao: ', estado[3])
        else:
          game_state = 1
          print('Mundo Completo!')
          imprime_mundo(mundo)
          print('Fim de Jogo! Você saiu da caverna sem o ouro.')
          print('Pontuacao: ', estado[3])
      else:
        if alertas[4] == -1:
          print('Nao e possivel sair da caverna por essa sala')
          print('Percepcao apos a ultima acao:')
          print('['+percebe_str+']')
          print('Mundo do Wumpus conhecido pelo agente:')
          imprime_percepcao(percebe, agente)
          acao = input('Digite a acao desejada (M/T/D/E/G/S):')
        else:
          print('Percepcao apos a ultima acao:')
          print('['+percebe_str+']')
          print('Mundo do Wumpus conhecido pelo agente:')
          imprime_percepcao(percebe, agente)
          acao = input('Digite a acao desejada (M/T/D/E/G/S):')

main()