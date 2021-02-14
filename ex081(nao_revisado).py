continuar = ' '
num = []
while continuar not in 'Nn':
    continuar = ' '
    num.append(int(input('Digite um valor: ')))
    while continuar not in 'SsNn':
        continuar = str(input('Você quer continuar? [S/N] '))[0]
print(f'Você digitou {len(num)} elementos.')
num.sort(reverse=True)
print(f'Os valores em ordem decrescente são {num}')
if 5 in num:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista.')