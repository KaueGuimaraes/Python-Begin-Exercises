m1k = tot = cont = 0
while True:
    cont += 1
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$:'))
    if cont == 1:
        barato = nome
        baratop = preço
    if preço >= 1000:
        m1k += 1
    if preço < baratop:
        barato = nome
        baratop = preço
    tot += preço
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Você quer continuar? [S/N] '))[0]
    if continuar in 'Nn':
        break
print(f'Total de gastos: R$:{ tot }')
print(f'Produtos que custam mais de R$:1.000: { m1k }')
print(f'Produto mais barato: { barato } custando R$:{ baratop }')