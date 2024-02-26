frase = str(input('Digite uma frase: ')).strip().upper()  #strip tira os espaços e upper coloca tudo em maiusculo
palavras = frase.split()  #separa a frase em palavras
junto = ''.join(palavras)  #junta as palavras substituindo os espaços pelo que vc colocar entre os ''
inverso = ''
#outra forma: inverso = junto [::-1] - dessa forma não usa o for
for letra in range (len(junto) - 1, -1, -1):      #pega o numero de letras menos 1, até a letra -1 e vai voltando 1 letra
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palindromo!')
else:
    print('A frase digitada não é um palindromo')