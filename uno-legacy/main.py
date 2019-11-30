import uno
from os import system

jjb = (uno.distribuir_cartas())
jogador = list(jjb[0]), list(jjb[1])
baralho = jjb[2]
cores = ['vermelho', 'amarelo', 'verde', 'azul'] 
enter = 'Pressione enter para continuar'

while True:
    try:
        cartaatual = baralho[0]
        baralho.pop(0)
        if cartaatual.split()[1] in cores:
            print('Carta atual: %s ' % cartaatual)
            break
        else:
            continue
    except IndexError:
        continue

while True:
    system('cls')
    print('Carta atual: %s' % cartaatual)
    print('Mão atual: %s' % jogador[0])
    if type(uno.cartas_utilizaveis(jogador[0], cartaatual)) == str:
        print('Cartas utilizaveis: %s' % uno.cartas_utilizaveis(jogador[0], cartaatual))
    else:
        print('Cartas utilizáveis:')

    cartaatual, jogador[0] = uno.escolher_carta(uno.cartas_utilizaveis(jogador[0], cartaatual), jogador[0], cartaatual)
    input(enter)

    system('cls')
    print('Carta atual: %s' % cartaatual)
    print('Mão atual: %s' % ', '.join(jogador[1]))
    if type(uno.cartas_utilizaveis(jogador[1], cartaatual)) == str:
        print('Cartas utilizaveis: %s' % uno.cartas_utilizaveis(jogador[1], cartaatual))
    else:
        print('Cartas utilizáveis:')

    cartaatual, jogador[1] = uno.escolher_carta(uno.cartas_utilizaveis(jogador[1], cartaatual), jogador[1], cartaatual)
    input(enter)
