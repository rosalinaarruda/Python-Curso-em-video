print('{:=^40}'.format('Lojas Guanabara'))        #40 = para centralizar
compras = float(input('Qual o valor das compras: R$ '))
print('''FORMAS DE PAGAMENTO:
[1]. à vista dinheiro/cheque
[2]. à vista no cartão
[3]. 2x no cartão
[4]. 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    preco = compras - (compras * 0.10)
elif opcao == 2:
    preco = compras - (compras * 0.05)
elif opcao == 3:
    preco = compras
    parcela = preco / 2
    print('Sua compra será parcelada em 2x sem juros de R${:.2f}'.format(parcela))
elif opcao == 4:
    preco = compras + (compras * 0.20)
    totalparc = int(input('Quantas parcelas? '))
    parcela = preco / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totalparc, parcela))

else:
    preco = compras
    print('Opção inválida de pagamento, tente novamente')

print('O valor das compras é de R${:.2f}, o valor a ser pago é de: R${:.2f}'.format(compras, preco))