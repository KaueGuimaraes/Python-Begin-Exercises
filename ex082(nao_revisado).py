continuar = ' '
num = []
pares = []
impares = []
while True:
    continuar = ' '
    num.append(int(input('Digite um valor: ')))
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] '))[0]
    if continuar in 'Nn':
        break
for n in range(0, len(num)):
    if num[n] % 2 == 0:
        pares.append(num[n])
    else:
        impares.append(num[n])
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')