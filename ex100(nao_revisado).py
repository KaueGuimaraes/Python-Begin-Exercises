def sorteia(lista):
    from random import randint
    for c in range(0, 5):
        lista.append(randint(0, 9))


def somaPar(num):
    segund = []
    soma = 0
    for c in range(0, len(num)):
        if num[c] % 2 == 0:
            soma += num[c]
    print(f'Na soma dos valores pares de {num} temos {soma}')


numero = list()
sorteia(numero)
somaPar(numero)