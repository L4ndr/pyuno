import uno
import random
from os import system

baralho = uno.criarbaralho()
print(len(baralho))
cartaatual = random.choice(baralho)
baralho.remove(cartaatual)

jogador = uno.distribuir_cartas(2)
print(len(baralho))
while True:
    for nj in range(len(jogador)):
        system('cls')
        print('carta atual: %s' % cartaatual)
        if cartaatual.startswith('bloquear'):
            uno.bloquear(nj)
            
        print('jogador atual: jogador %s' % str(nj+1))
        maoatual = jogador[nj]
        cartasutilizaveis = uno.cartas_utilizaveis(maoatual, cartaatual)
        
        if cartaatual.startswith('+2'):
            uno.pescar_carta(jogador[nj], 2)
        if cartaatual.startswith('+4'):
            uno.pescar_carta(jogador[nj], 4)
        
        print('mão atual: %s' % ', '.join(maoatual))
        print('cartas utilizaveis: %s' % ', '.join(cartasutilizaveis))
        jogador[nj], cartaatual = uno.escolher_cartas(maoatual, cartasutilizaveis, cartaatual)
        system('cls')
        if nj == 0:
            proximojogador = 2
        else:
            proximojogador = 1
        print('próximo jogador: %s' % proximojogador)
        input('pressione qualquer tecla para passar a vez.')