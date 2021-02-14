temp = []
princ = []
continuar = ' '
maior = menor = 0
while continuar not in 'Nn':
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        menor = maior = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] '))[0]
print(f'Ao todo, você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi {maior} de', end='')
for p in princ:
    if p[1] == maior:
        print(f' {p[0]}', end='')
print(f'\nO menor peso foi {menor} de', end='')
for p in princ:
    if p[1] == menor:
        print(f' {p[0]}', end='')