from datetime import date
nasc = int(input('Ano de nascimento : '))
atual = date.today().year
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação : MIRIM')
elif idade <= 14:
    print('Classificação : INFANTIL')
elif idade <=  19:
    print('Classificação : JUNIOR')
elif idade <= 20:
    print('Classificação : SÊNIOR')
else:
    print('Classificação : MASTER')