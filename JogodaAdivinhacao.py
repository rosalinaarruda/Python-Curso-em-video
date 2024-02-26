from random import randint
from time import sleep

cores = {'limpa': '\033[m',
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'roxo' : '\033[35m',
         'pretoebranco' : '\033[7:30m'}

computador = randint(0,5)   #faz o computador 'pensar'
print('*--*' * 20)
print('Vou pensar num número entre 1 e 5. Tente adivinhar...')
print('*--*' * 20)
jogador = int(input('Em que número eu pensei? '))  #jogador tenta adivinhar

print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('Parabens!! Você acertou!!')

else:
    print('Eita!! Você errou!! Pensei no número {}{}{} e não no número {}{}{}!'.format(cores['azul'], computador, cores['limpa'], cores['roxo'],jogador, cores['limpa'] ))

print('FIM')