def aumentar(n, v):
    res = n + ((n / 100) * v)
    return res


def diminuir(n, v):
    res = n - ((n / 100) * v)
    return res


def dobro(n):
    res = n * 2
    return res


def metade(n):
    res = n / 2
    return res

def moeda(n):
    num = str(n)
    res = ""

    for c in range(0, len(num)):
        if num[c] == ".":
            res += ","
        else:
            res += num[c]

    res = "R$" + res

    return res