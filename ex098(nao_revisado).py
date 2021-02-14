from time import sleep
def contagem(a, b, c):
    print('-=' * 30)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if c == 0:
        c = 1
    if a > b:
        c = -c
        b -= 1
    else:
        c = +c
        b += 1
    for c in range(a, b, c):
        print(f'{c}', end=' ')
        sleep(0.5)
    print('FIM')


contagem(1, 10, 1)
contagem(10, 0, 2)
contagem(int(input('Começo: ')), int(input('Fim: ')), int(input('Passo: (não coloque número negativo) ')))