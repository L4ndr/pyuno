import random

baralho = open('cartas.txt', 'r').read().strip('\n').split('\n')
random.shuffle(baralho)
semcor = ['+4', 'trocar cor']

def criar_baralho():
    return baralho

def distribuir_cartas(numjogadores):
    jogadores = []
    for i in range(numjogadores):
        jogadores.append([])
        for _ in range(7):
            jogadores[i].append(baralho[0])
            baralho.pop(0)
    return jogadores

def cartas_utilizaveis(jogador, cartaatual):
    utilizaveis = []
    if cartaatual in semcor:
        for carta in jogador:
            utilizaveis.append(carta)
    for carta in jogador:
        if carta in semcor or (carta.endswith(cartaatual.split()[len(cartaatual.split())-1]) or carta.startswith(cartaatual.split()[0])):
            utilizaveis.append(carta)
    return utilizaveis
    
def escolher_cartas(maoatual, utilizaveis, cartaatual):
    print('Escolha uma opção abaixo digitando um dos números:')
    for i in range(len(utilizaveis)):
        print('[%s] %s' % (str(i+1), str(utilizaveis[i])))
    print('[%s] pescar carta' % str(len(utilizaveis)+1))
    choice = int(input())
    if choice == len(utilizaveis)+1:
        pescar_carta(maoatual, 1)
        cartaatual = cartaatual
    else:
        cartaatual = utilizaveis[choice-1]
        maoatual.remove(cartaatual)
    return maoatual, cartaatual

def pescar_carta(jogador, numerodecartas,):
    for _ in range(numerodecartas):
        jogador.append(baralho[0])
        baralho.pop(0)

def bloquear(nj):
    if nj == 0:
        nj = 1
    else:
        nj = 0
    return nj

def inverter(jogador):
    jogador.reverse()
    return jogador

def trocar_cor(ca):
    print("Escolha uma cor digitando um dos números abaixo:\n[1]Amarelo\n[2]Azul\n[3]Verde\n[4]Vermelho")
    cor_nova = int(input(""))
    dic = {
        1:"amarelo",
        2:"azul",
        3:"verde",
        4:"vermelho"
    }
    ca = ca.replace(ca.split()[1], dic[cor_nova])
    return ca
