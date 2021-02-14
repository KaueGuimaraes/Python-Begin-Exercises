galera = []
cont = 0
conti = ' '
soma = 0
while True:
    galera.append({})
    if cont == 0:
        galera[0]['mulheres'] = []
    galera[cont]['nome'] = str(input('Nome: '))
    galera[cont]['sexo'] = str(input('Sexo: [M/F] ')).upper()
    while galera[cont]['sexo'] not in 'FfMm':
        galera[cont]['sexo'] = str(input('ERRO! Responda apenas M ou F.\nSexo: [M/F] ')).upper()
    galera[cont]['idade'] = int(input('Idade: '))
    soma += galera[cont]['idade']
    if galera[cont]['sexo'] == 'F':
        galera[0]["mulheres"].append(galera[cont]["nome"])
    cont += 1
    conti = str(input('Quer continuar? [S/N] '))
    while conti not in 'SsNn':
        conti = str(input('ERRO! Responda apenas S ou N.\nQuer continuar? [S/N] '))
    if conti in 'Nn':
        break
    conti = ' '
galera[0]['média'] = soma / cont
print(f'A) Ao todo temos {cont} pessoas cadastradas.')
print(f'B) A média de idade é de {galera[0]["média"]:5.2f} anos')
print(f'C) As mulheres cadastradas foram', end='')
for m in range(0, len(galera[0]['mulheres'])):
    print(f' {galera[0]["mulheres"][m]}', end='')
print(f'\nD) Lista das pessoas que estão acima da média: ')
for p in range(0, len(galera)):
    if galera[p]['idade'] > galera[0]['média']:
        print(' ' * 5, f'nome = {galera[p]["nome"]}; sexo = {galera[p]["sexo"]}; idade = {galera[p]["idade"]}')
print('<< ENCERRADO >>')