salario = float(input('Qual é o salário do funcionário ? R$'))
if salario < 1250.00 or salario == 1250.00:
    a = salario / 100
    aumento = a * 15
    aumento = aumento + salario
else:
    a = salario / 100
    aumento = a * 10
    auemnto = auemnto + salario
print('Quem ganhava R${} passa a ganhar R${} agora'.format(salario, aumento))
'''Neste progama o usuário digita o salário de algum
funcionário e se o salário for igual ou menor de
R$1250.00 o aumento será de 15% mais se o salário for
menor de R$1250.00 o aumento será de 10%'''