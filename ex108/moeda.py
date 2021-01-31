def aumentar(n = 0, v = 0):
    res = n + ((n / 100) * v)
    return res


def diminuir(n = 0, v = 0):
    res = n - ((n / 100) * v)
    return res


def dobro(n = 0):
    res = n * 2
    return res


def metade(n = 0):
    res = n / 2
    return res

def moeda(n = 0, moeda = 'R$'):
    num = f'{n: >.2f}'
    res = ""

    for c in range(0, len(num)):
        if num[c] == ".":
            res += ","
        else:
            res += num[c]

    res = moeda + res

    return res