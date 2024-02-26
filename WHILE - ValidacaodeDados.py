sexo = str(input('Digite o sexo: [M/F]')).strip().upper()[0]           #tira os espaços, coloca tudo maiusculo e pega apenas a primeira letra
while sexo != 'M' != 'F':      #outra forma: while sexo not in 'MmFf
    sexo = str(input('Dados inválidos. Por favor, digite seu sexo: ')).strip().upper()[0]

print('Sexo {} registrado com sucesso'.format(sexo))