print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
total = 0
cont = 1
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} => '.format(termo),end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar?'))
print('Progressão finalizada com {} termos mostrados'.format(total))