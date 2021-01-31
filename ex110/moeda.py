def aumentar(n = 0, v = 0, format = True):
    '''
    :param n: Número para aumentar.
    :param v: Porcentagem que o Número irá aumentar.
    :param format: (Opcional) Para ou não mostrar o Resultado Formatado.
    '''
    res = n + ((n / 100) * v)

    if(format):
        return moeda(res)
    else:
        return res


def diminuir(n = 0, v = 0, format = True):
    '''
    :param n: Número para diminuir.
    :param v: Porcentagem que o Número irá diminuir.
    :param format: (Opcional) Para ou não mostrar o Resultado Formatado.
    '''
    res = n - ((n / 100) * v)

    if(format):
        return moeda(res)
    else:
        return res


def dobro(n = 0, format = True):
    '''
    :param n: Número para mostrar o dobro.
    :param format: (Opcional) Para ou não mostar o Resultado Formatado.
    '''
    res = n * 2

    if(format):
        return moeda(res)
    else:
        return res


def metade(n = 0, format = True):
    '''
    :param n: Número para mostrar a metade.
    :param format: (Opcional) Para ou não mostrar o Resultado Formatado.
    '''
    res = n / 2

    if(format):
        return moeda(res)
    else:
        return res


def moeda(n = 0, moeda = 'R$'):
    '''
    :param n: Número para ser formatado.
    :param moeda: (Opcional) Moeda para usar na formatação.
    '''
    num = f'{n: >.2f}'
    res = ""

    for c in range(0, len(num)):
        if num[c] == ".":
            res += ","
        else:
            res += num[c]

    res = moeda + res

    return res


def resumo(n = 0, va = 0, vd = 0):
    print('-' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-' * 30)

    print(f'Preço Analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n)}')
    print(f'Metade do preço: \t{metade(n)}')
    print(f'20% de aumento: \t{aumentar(n, va)}')
    print(f'12% de redução: \t{diminuir(n, vd)}')
    print('-' * 30)