import uno
import random
from os import system

baralho = uno.criarbaralho()
print(len(baralho))
cartaatual = random.choice(baralho)
baralho.remove(cartaatual)
# define a carta inicial

jogador = uno.distribuir_cartas(2)
# distribui as cartas aos jogadores

while True:
    for nj in range(len(jogador)): # define qual o jogador atual
        system('clear')
        print('carta atual: %s' % cartaatual)
       
        if cartaatual.startswith('+2'):
            uno.pescar_carta(jogador[nj], 2)
        if cartaatual.startswith('+4'):
            uno.pescar_carta(jogador[nj], 4)
        if cartaatual.startswith('inverter'):
            uno.inverter(jogador)
        
        if cartaatual.startswith('bloquear'):
            nj = uno.bloquear(nj) # muda o jogador atual (vulgo torcar de jogador)
            
        print('jogador atual: jogador %s' % str(nj+1)) # mostra o jogador atual com base no valor de nj
        maoatual = jogador[nj] # define a mão do jogador atual
        cartasutilizaveis = uno.cartas_utilizaveis(maoatual, cartaatual)
        
        
        
        print('mão atual: %s' % ', '.join(maoatual))
        print('cartas utilizaveis: %s' % ', '.join(cartasutilizaveis))

        jogador[nj], cartaatual = uno.escolher_cartas(maoatual, cartasutilizaveis, cartaatual)
        
        
        system('clear')

        if nj==0:
            proximo = 1
        else: 
            proximo = 2
        
        print('próximo jogador: {}'.format(proximo))
        if len(jogador[nj]) == 0:
            break
        input('pressione qualquer tecla para passar a vez.')

print("Jogador %s é o ganhador!" % nj)