#codigo ansi, sempre com \033[style, fonte, background m
#style: 0 = none; 1 = negrito; 4 = sublinhado 7 = inverte cor de letra e fundo (negative)
#texto: 30 branco, 31 vermelho, 32 verde, 33 amarelo, 34 azul, 35 roxo, 36 verde, 37 cinza
#background 40 fundo branco, 41 vermelho, 42 verde, 43 amarelo, 44 azul, 45 roxo, 46 verde, 47 cinza
#modulo colorise tem mais opções de cores para trabalhar

# \033[0;30;41m
# \033[4;33;44m
# \033[1;35;43m
# \033[30;42m    #o zero não é obrigatorio
# \033[m
# \033[7;30m

print('\033[4;30;45mOlá mundo!!\033[m')
print('\033[1;35;44mOlá mundo!!\033[m')
print('\033[7;30mOlá mundo!!\033[m')
print('\033[7;37mOlá mundo!!\033[m')

a=3
b=5
print('Os valores são \033[1;32m{}\033[m e \033[1;34m{}\033[m'.format(a,b))   #coloquei no final para fechar a cor

nome = 'Lina'
print('Olá!! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

nome2 = 'Lina'
cores = {'limpa': '\033[m',
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'pretoebranco' : '\033[7:30m'}

print('Olá!! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome2, cores['limpa'])) #simplifica a escolha das cores