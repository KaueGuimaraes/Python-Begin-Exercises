palavras = ('CURSO', 'APRENDER', 'PYTHON', 'ESTUDAR', 'ESTOU', 'CURSO', 'EM', 'VIDEO')
for p in palavras:
    print(f'Na palavra {p} temos ', end='')
    for letra in p:
        if letra in 'AEIOUaeiou':
            print(letra.lower(), end='')
    print('\n')