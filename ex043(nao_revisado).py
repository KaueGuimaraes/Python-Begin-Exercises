peso = float(input('Qual é o seu peso ? (Kg) '))
altura = float(input('Qual é a sua altura '))
imc = peso / (altura ** 2)
print('O IMC dassa pessoa é de {:.1f}'.format(imc))
print('Você está ', end='')
if imc < 18.5:
    print('\033[31mABAIXO DO PESO')
elif imc < 25:
    print('no\033[32m PESO IDEAL')
elif imc < 30:
    print('em\033[32m SOBREPESO')
elif imc < 40:
    print('em\033[31m OBESIDADE')
else:
    print('em\033[31m OBESIDADE MÓRBIDA')