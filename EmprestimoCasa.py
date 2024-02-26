valorCasa = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual o valor do salário do comprador?'))
prazo = int(input('Qual o prazo de pagamento (em anos)?'))

prestacao = valorCasa/(prazo * 12)
if (prestacao <= salario * 0.30):
    print('Parabens!! Empréstimo Concedido!! O valor da sua parcela será de R${:.2f} em {} anos'.format(prestacao,prazo))
else:
    print('O valor das parcelas excedeu os 30% do seu salário (R${:.2f}), infelizmente seu emprestimo foi negado!!'.format(salario*0.3))
    print('Salário: R${:.2f}, Valor da parcela: R${:.2f} em {} anos'.format(salario, prestacao, prazo))