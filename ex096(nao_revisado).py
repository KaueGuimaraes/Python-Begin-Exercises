def vezes(a, b):
    c = a * b
    print(f'A área de um terreno {a}x{b} é de {c}')


print('Controle de terrenos')
print('-' * 40)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
vezes(largura, comprimento)