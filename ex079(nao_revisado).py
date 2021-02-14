num = []
continuar = ' '
while True:
    while continuar not in'Nn':
        continuar = ' '
        t = int(input('Digite um número: '))
        if t in num:
            print('Valor duplicado! não vou adicionar...')
        else:
            num.append(t)
            print('Valor adicionado com sucesso...')
            while continuar not in 'SsNn':
                continuar = str(input('Você quer continuar? [S/N] '))[0]
print(f'Os valores digitados em ordem crescente foi {sorted(num)}')