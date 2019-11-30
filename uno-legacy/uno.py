import random

numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
cores = ['vermelho', 'amarelo', 'verde', 'azul']
especial = ['+2', 'bloquear', 'inverter']  # cartas possiveis
semcor = ['+4', 'trocar cor']


def criar_baralho():
    baralho = list([])  # lista vazia para podermos adicionar as cartas mais tarde

    for _ in range(2):
        for numero in numeros:  # gerar cartas de números (ex: 6 verde)
            for cor in cores:
                baralho.append('%s %s' % (numero, cor))

    for _ in range(2):
        for carta in especial:  # gerar cartas especiais (ex: bloquear amarelo)
            for cor in cores:
                baralho.append('%s %s' % (carta, cor))

    for _ in range(4):
        for carta in semcor:  # gerar cartas sem cor (+4 e trocar cor)
            baralho.append(carta)

    return baralho


def distribuir_cartas():
    baralho = open('cartas.txt', 'r').read().split('\n')
    random.shuffle(baralho)
    jogador = list([list([]), list([])])

    for c in range(7):
        jogador[0].append(baralho[c])
        jogador[1].append(baralho[c + 1])
        baralho.pop(0)
        baralho.pop(1)

    return jogador[0], jogador[1], baralho


def cartas_utilizaveis(jogador, cartaatual):
    cartasutilizaveis = []
    for carta in jogador:
        if carta.endswith(cartaatual.split()[1]):
            cartasutilizaveis.append(carta)
        elif carta in semcor:
            cartasutilizaveis.append(carta)
        elif carta.startswith(cartaatual.split()[0]):
            cartasutilizaveis.append(carta)
        else:
            pass
    if len(cartasutilizaveis) > 0:
        pass
    else:
        cartasutilizaveis = 'Você não tem nenhuma carta utilizável.'
    return cartasutilizaveis


def escolher_carta(utilizaveis, baralho, cartaatual):
    while True:
        try:
            if type(utilizaveis) != str:
                for c in range(len(utilizaveis)):
                    print('[%d] %s' % (c, utilizaveis[c]))
                    if c + 1 == len(utilizaveis):
                        print('[%s] passar a vez' % len(utilizaveis))
            carta = int(input())
            if carta == c + 1:
                cartaatual = cartaatual
                pass
            else:
                cartaatual = utilizaveis[carta]
                baralho.remove(utilizaveis[carta])
            return cartaatual, baralho
            break
        except IndexError:
            continue
