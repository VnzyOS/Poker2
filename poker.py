from combinacao import Mao
from combinacao import Combinacao
from collections import Counter
from combinacao import Repeticao
import random

continuar = True
while continuar:
    Flush = False
    Flush2 = False
    Straight = False
    Straight2 = False
    contador = 0
    contador2 = 0
    z = True
    jogador1 = Combinacao('uma Carta Alta! ')
    jogador2 = Combinacao('uma Carta Alta! ')

    Cartas = ["A", "2", "3", "4", "5", "6", "7", "8", "9",
              "10", "J", "Q", "K"]
    rank = {'um Royal Flush': 9, 'um Straight Flush': 8, 'uma Quadra': 7, 'um Full House': 6,
            'um Flush': 5, 'um Straight': 4, 'uma Trinca': 3, 'dois Pares': 2, 'um Par': 1, 'uma Carta Alta! ': 0}

    Naipes = ["♣", "♥", "♠", "♦"]
    Baralho = [(k, j)for k in Cartas for j in Naipes]
    random.shuffle(Baralho)

    mao1 = Mao(Baralho[1], Baralho[4])
    mao2 = Mao(Baralho[2], Baralho[5])

    rep = Repeticao(0, 0, 0)
    rep2 = Repeticao(0, 0, 0)

    mesa = [Baralho[7], Baralho[8], Baralho[9], Baralho[10], Baralho[11]]
    mNUM = [mesa[0][0], mesa[1][0], mesa[2][0], mesa[3][0], mesa[4][0]]
    mNAIPE = [mesa[0][1], mesa[1][1], mesa[2][1], mesa[3][1], mesa[4][1]]
    j1NUM = list(mNUM)
    j1NAIPE = mNAIPE
    j2NUM = list(mNUM)
    j2NAIPE = mNAIPE

    j1NUM.append(mao1.carta1[0])
    j1NUM.append(mao1.carta2[0])
    
    j2NUM.append(mao2.carta1[0])
    j2NUM.append(mao2.carta2[0])

    j1NAIPE.append(mao1.carta1[1])
    j1NAIPE.append(mao1.carta2[1])
    j2NAIPE.append(mao2.carta1[1])
    j2NAIPE.append(mao2.carta2[1])

    mao1.show_hands()
    
    print('')
    print(f' O Flop é: {mesa[0], mesa[1], mesa[2]}')
    print('')
    x = input('Você deseja pagar a mão e ver o Turn? s/n ')
    if x == 's':
        print(f' O Turn é: {mesa[0], mesa[1], mesa[2],mesa[3]}!')
        print('')
        x = input('Você deseja pagar a mão e ver o River? s/n ')
        if x == 's':
            print(f' O River é: {mesa[0], mesa[1], mesa[2], mesa[3], mesa[4]}!')
            print('')
        else:
            print('Você deu Fold! ')
            x = input('Você deseja jogar novamente? s/n ')
            if x == 'n':
                continuar = False
                break
            else:
                z = False
    else:
        print('Você deu Fold! ')
        x = input('Você deseja jogar novamente? s/n ')
        if x == 'n':
            continuar = False
            break
        else:
            z = False

    contZAP = j1NAIPE.count('♣')
    contESPADA = j1NAIPE.count('♠')
    contOURO = j1NAIPE.count('♦')
    contCOPAS = j1NAIPE.count('♥')
    contZAP2 = j1NAIPE.count('♣')
    contESPADA2 = j1NAIPE.count('♠')
    contOURO2 = j1NAIPE.count('♦')
    contCOPAS2 = j1NAIPE.count('♥')

    if contZAP == 5 or contESPADA == 5 or contOURO == 5 or contCOPAS == 5:
        Flush = True
    if contZAP2 == 5 or contESPADA2 == 5 or contOURO2 == 5 or contCOPAS2 == 5:
        Flush2 = True

    for i in range(len(j1NUM)):
        if j1NUM[i] == 'A':
            j1NUM[i] = 1
        elif j1NUM[i] == 'J':
            j1NUM[i] = 11
        elif j1NUM[i] == 'Q':
            j1NUM[i] = 12
        elif j1NUM[i] == 'K':
            j1NUM[i] = 13
        j1NUM[i] = int(j1NUM[i])
        
        if j2NUM[i] == 'A':
            j2NUM[i] = 1
        elif j2NUM[i] == 'J':
            j2NUM[i] = 11
        elif j2NUM[i] == 'Q':
            j2NUM[i] = 12
        elif j2NUM[i] == 'K':
            j2NUM[i] = 13
        j2NUM[i] = int(j2NUM[i])
        
    j2NUM = sorted(j2NUM)
    j1NUM = sorted(j1NUM)
    
    for i in range(6):
        if j1NUM[i] == j1NUM[i+1] - 1:
            contador += 1
        elif j1NUM[i] == j1NUM[i+1]:
            pass
        else:
            contador = 0
        if contador == 5:
            Straight = True
        
        if j2NUM[i] == j1NUM[i+1] - 1:
            contador2 += 1
        elif j1NUM[i] == j1NUM[i+1]:
            pass
        else:
            contador2 = 0
        
        if contador2 == 5:
            Straight2 = True

    lista = list(j1NUM)
    lista2 = list(j2NUM)
    c = Counter(lista)
    cz = Counter(lista2)
    
    for numero, repeticoes in c.items():
        if repeticoes > 1:
            aparicao = [indice for indice, item in enumerate(lista) if item == numero]
            
            if len(aparicao) == 2:
                rep.par += 1
            if len(aparicao) == 3:
                rep.trinca += 1
            if len(aparicao) == 4:
                rep.quadra += 1
             
    for numero, repeticoes in cz.items():
        if repeticoes > 1:
            aparicao = [indice for indice, item in enumerate(lista2) if item == numero]
            
            if len(aparicao) == 2:
                rep2.par += 1
            if len(aparicao) == 3:
                rep2.trinca += 1
            if len(aparicao) == 4:
                rep2.quadra += 1

    if Flush and Straight:
        if min(j1NUM) == 10:
            jogador1.combinacao = 'um Royal Flush'
        else:
            jogador1.combinacao = 'um Straight Flush'
                    
    elif rep.quadra == 1:
        jogador1.combinacao = 'uma Quadra'
    elif rep.par == 1 and rep.trinca == 1:
        jogador1.combinacao = 'um Full House'
    elif Flush:
        jogador1.combinacao = 'um Flush'
    elif Straight:
        jogador1.combinacao = 'um Straight'
    elif rep.trinca == 1:
        jogador1.combinacao = 'uma Trinca'
    elif rep.par == 2:
        jogador1.combinacao = 'dois Pares'
    elif rep.par == 1:
        jogador1.combinacao = 'um Par'
        
    if Flush2 and Straight2:
        if min(j2NUM) == 10:
            jogador2.combinacao = 'um Royal Flush'
        else:
            jogador2.combinacao = 'um Straight Flush'
                    
    elif rep2.quadra == 1:
        jogador2.combinacao = 'uma Quadra'
    elif rep2.par == 1 and rep2.trinca == 1:
        jogador2.combinacao = 'um Full House'
    elif Flush:
        jogador2.combinacao = 'um Flush'
    elif Straight:
        jogador2.combinacao = 'um Straight'
    elif rep2.trinca == 1:
        jogador2.combinacao = 'uma Trinca'
    elif rep2.par == 2:
        jogador2.combinacao = 'dois Pares'
    elif rep2.par == 1:
        jogador2.combinacao = 'um Par'
        
    if z:
        jogador1.show_combi()
        print(f' As cartas do seu oponente são: {mao2.carta1}, {mao2.carta2}')
        print(f' O seu oponente tem {jogador2.combinacao}!')
        if rank[jogador1.combinacao] > rank[jogador2.combinacao]:
            print(f' Você ganhou!!')
        elif rank[jogador1.combinacao] == rank[jogador2.combinacao]:
            if max(j1NUM) > max(j2NUM):
                print(f' Você ganhou!!')
            else:
                print(f' Você Perdeu!')
        else:
            print(f' Você Perdeu!')
        x = input(' Você deseja Jogar Novamente? s/n ')
        if x == 'n':
            continuar = False
