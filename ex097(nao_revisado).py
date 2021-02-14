def mostrar():
    test = []
    while True:
        continu = ' '
        test.append(str(input('Digite um frase: ')))
        while continu not in 'SsNn':
            continu = str(input('Quer continuar? [S/N] ')).upper()[0]
        if continu in 'Nn':
            break
    for c in range(0, len(test)):
        b = len(test[c]) + 4
        print('-' * b)
        print(f'  {test[c]}  ')
        print('-' * b)


mostrar()