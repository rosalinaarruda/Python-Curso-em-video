print('='*30)
print('10 TERMOS DE UMA PA')
print('='*30)

primTermo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primTermo + (10-1) * razao

for c in range (primTermo,decimo + razao, razao):
    print('{} '.format(c), end = ' -> ')
print('ACABOU')
