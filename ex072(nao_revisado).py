'''numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoite', 'dezenove', 'vinte')
num = int(input('Digite um número entre [0, 20] '))
while num > 20 or num < 0:
    num = int(input('INVÁLIDO. Digite um número entre [0, 20] '))
print(f'Você digitou o número {numeros[num]}.')'''
#Infinito
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', ' seis',
          'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
          'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre [0, 20] '))
    while num > 20 or num < 0:
        num = int(input('INVÁLIDO. Digite um número entre [0, 20] '))
    print(f'Você digitou {numeros[num]}')
    s = str(input('Você quer continuar? [S/N] '))[0].upper()
    while s not in 'SsNn':
        s = str(input('INVÁLIDO.Você quer continuar? [S/N] '))[0].upper()
    if s in 'Nn':
        break