resp = 'S'
soma = qtde = media = 0
while resp in 'Ss':

    numero = int(input('Digite um número: '))
    soma += numero
    qtde += 1
    if qtde == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    resp = str(input('Quer continuar? [S/N] ').upper().strip()[0])

media = soma/qtde
print('Você digitou {} numeros e a média é: {}'.format(qtde,media))
print('O maior número foi {} e o menor foi {}'.format(maior,menor))
print('ACABOU')
