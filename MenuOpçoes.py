from time import sleep

primeiro = int(input('Entre com o primeiro número: '))
segundo = int(input('Entre com o segundo número: '))
opcao = 0

while opcao != 5:

    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('Qual a sua opção: '))
    if opcao == 1:
        soma = primeiro + segundo
        print('A Soma entre {} + {} é: {}'. format(primeiro,segundo,soma))

    elif opcao == 2:
        produto = primeiro * segundo
        print('O produto entre {} * {} é: {}'.format(primeiro, segundo, produto))

    elif opcao == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo
        print('Entre {} e {}, o maior valor é {}'.format(primeiro,segundo,maior))

    elif opcao == 4:
        print('Informe os numeros novamente: ')
        primeiro = int(input('Entre com o primeiro número: '))
        segundo = int(input('Entre com o segundo número: '))

    elif opcao == 5:
        print('Finalizando...')

    else:
        print('Opção inválida. Tente novamente!!')

    print('=-=' * 10)
    sleep(1)
print('Fim do programa!!')
