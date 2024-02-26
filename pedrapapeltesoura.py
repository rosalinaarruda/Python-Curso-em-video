from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0]. Pedra 
[1]. Papel
[2]. Tesoura''')
jogador = int(input('Qual a sua jogada? '))
if jogador != 0 != 1 != 2:
    print('Jogada Inválida! Tente novamente')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!')
    sleep(1)
    print('-=' * 11)
    print('O computador jogou {}'.format(itens[computador]))
    print('O jogador jogou {}'.format(itens[jogador]))
    print('-=' * 11)

    if computador == 0:
        if jogador == 0:
            print('EMPATE! Ninguém ganhou, tente novamente')
        elif jogador == 1:
            print('VOCÊ GANHOU! Papel ganha de Pedra!')
        elif jogador == 2:
            print('VOCÊ PERDEU! Pedra ganha de Tesoura!')

    elif computador == 1:
        if jogador == 0:
            print('VOCÊ PERDEU! Papel ganha de Pedra!')
        elif jogador == 1:
            print('EMPATE! Ninguém ganhou, tente novamente')
        elif jogador == 2:
            print('VOCÊ GANHOU! Tesoura ganha de Papel !')

    elif computador == 2:  #TESOURA
        if jogador == 0: #PEDRA
            print('VOCÊ GANHOU! Pedra ganha de Tesoura!')
        elif jogador == 1: #papel
            print('VOCÊ PERDEU! Tesoura ganha de Papel!')
        elif jogador == 2:
            print('EMPATE! Ninguém ganhou, tente novamente')

