soma = 0
cont = 0
for n in range (1,7):
    num = int(input('Digite o {}º numero: '.format(n)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} pares e a soma dos números é: {}'.format(cont, soma))