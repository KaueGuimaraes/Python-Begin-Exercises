num = [[], [], []]
for c in range(1, 8):
    valor = int(input('Digite um valor'))
    if valor % 2 == 0:
        num[0].append(valor)
    elif valor % 2 == 1:
        num[1].append(valor)
    num[2].append(valor)
print(f'Você digitou os valores {num[2]}...')
print(f'Os valores pares em ordem crescente foram {sorted(num[0])}')
print(f'Os valores ímpares em ordem crescente foram {sorted(num[1])}')