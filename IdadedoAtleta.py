from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('É um Atleta Mirim')

elif idade <= 14:
    print('É um Atleta Infantil')

elif idade <= 19:
    print('É um Atleta Junior')

elif idade <= 25:
    print('É um Atleta Sênior')

else:
    print('É um Atleta Master')


