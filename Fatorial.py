#primeira forma, usando o módulo math
#from math import factorial
#n = int(input('Digite um número para calcular o fatorial: '))
#f = factorial(n)
#print(('O fatorial de {} é {}'.format(n, f)))

#forma tradicional
n = int(input('Digite um número para calcular o fatorial: '))
c = n
f = 1
print('Calculando {}! ='.format(n),end=' ')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=" ")
    f *= c
    c -= 1

print('{}'.format(f))