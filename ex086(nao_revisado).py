matriz = [[], [], []]
valor = pos = cont = 0
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
print(f'[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]')
print(f'[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]')
print(f'[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]')