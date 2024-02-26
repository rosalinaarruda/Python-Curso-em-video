r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')

    elif r1 != r2 != r3 != r1:
        print('ESCALENO')

    else:
        print('ISOSCELES')

else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo')