def valor(* num):
    print('-=' * 30)
    print('Analisando os valores passados...', end='')
    maior = 0
    for c in range(0, len(num)):
        if c == 0:
            maior = num[c]
        if num[c] > maior:
            maior = num[c]
    for n in num:
        print(f' {n}', end='')
    print(f'\nForam informados {len(num)} valores ao todo.')
    print(f'O maior valor passado foi {maior}')
    print('-=' * 30)


valor(0, 5, 2, 6, 11)
valor(0, 5, 2)
valor(0, 5, 1, 209)
valor()