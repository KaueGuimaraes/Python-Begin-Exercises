continu = 's'
cont = d = num = maior = menor = 0
while continu == 's':
    num = int(input('Digite um número: '))
    continu = str(input('Quer continua [s/n] ')).lower().strip()[0]
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    d += num
print('Você digitou {} números e a média foi {}'.format(cont, d / cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))