from datetime import date
ano = int(input('Que ano quer analisar ? Coloque 0 para analisar o ano atual : '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO '.format(ano))
else:
    print('O ano {} não é BISSEXTO '.format(ano))
'''Este progama analisa se o número é bissexto ou não
e se o usuario digitar 0 mostrará se o ano atual é ou
não é bissexto'''