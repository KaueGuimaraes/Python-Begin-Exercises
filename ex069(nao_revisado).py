mais18 = mulheres = homens = 0
while True:
    sexo = str(input('Qual é o sexo dessa pessoa? [M/F] ')).upper()[0]
    while sexo not in 'MmFf':
        print('RESPOSTA INVÁLIDA')
        sexo = str(input('Qual é o sexo dessa pessoa? [M/F] ')).upper()[0]
    idade = int(input('Qual é a idade dessa pessoa? '))
    if idade >= 18 :
        mais18 += 1
    if idade < 20 and sexo == 'F':
        mulheres += 1
    if sexo == 'M':
        homens += 1
    cont = str(input('Você quer continuar? [S/N] '))
    while cont not in 'SsNn':
        print('RESPOSTA INVÁLIDA')
        cont = str(input('Você quer continuar? [S/N] ')).upper()[0]
    if cont in 'Nn':
        break
print(f'{ mais18 } pessoas tem mais de 18 anos \ntem { mulheres } mulheres menores de 20 anos \ne tem { homens } homens.')