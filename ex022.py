print('========= DESAFIO 022 =========\n')

nome = str(input('Qual é o seu nome completo? '))

PrimeiroNome = nome.split()[0]
NomeMaisculo = nome.upper()
NomeMinusculo = nome.lower()

QuantidadePrimeiro = len(PrimeiroNome)
QuantidadeNome = nome.split()
QuantidadeNome = len(''.join(QuantidadeNome))

print('\nAnalisando o seu nome...\n')

print('O seu nome em maiúsculo é: {}'.format(NomeMaisculo))
print('O seu nome em minúsculo é: {}'.format(NomeMinusculo))
print('O seu nome tem ao todo {} letras'.format(QuantidadeNome))
print('O seu primeiro nome é {} e ele tem {} letras'.format(PrimeiroNome, QuantidadePrimeiro))

print('\nFIM!!')