num = digitados = soma = 0
while not num == 999:
    num = int(input('Digite um número [999 para parar]: '))
    digitados += 1
    soma += num
soma -= 999
digitados -= 1
print('Você digitou {} números, e a soma de todos os números é igual á {}'.format(digitados, soma))