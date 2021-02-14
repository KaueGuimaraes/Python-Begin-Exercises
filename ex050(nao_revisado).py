cont = 0
soma = 0
for c in range(1, 6 + 1):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma entre todos os {} valores pares é {}'.format(cont, soma))