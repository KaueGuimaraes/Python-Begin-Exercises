matriz = [[], [], [], []]
valor = 0
pos = 0
cont = 0
soma = 0
for c in range(0, 9):
    valor = int(input(f'Digite um valor para a posição [{pos}, {cont}]'))
    if pos == 0:
        matriz[0].append(valor)
    elif pos == 1:
        matriz[1].append(valor)
    else:
        matriz[2].append(valor)
    cont += 1
    if cont == 3:
        cont = 0
        pos += 1
    if valor % 2 == 0:
        matriz[3].append(valor)
print(f'[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]')
print(f'[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]')
print(f'[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]')
for n in matriz[3]:
    soma += n
print(f'\nA soma dos valores pares é {soma}')
soma = 0
soma = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha foi {max(matriz[1])}')