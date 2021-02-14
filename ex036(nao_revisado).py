cores = {'branco':'\033[30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul escuro':'\033[34m',
         'roxo':'\033[35m',
         'azul claro':'\033[36m',
         'cinza':'\033[37m',
         'fim':'\033[m'}
casa = float(input('Valor da casa : R$'))
salário = float(input('Salário do comprador : R$'))
anos = int(input('Quantos anos de financiamento'))
mínimo  = salário * 30 / 100
prestação = casa / (anos * 12)
print('Para pagar uma casa de {}R${:.2f}{} em {} anos'.format(cores['verde'],casa, cores['fim'], anos), end='')
print(' a prestação será de {}R${:.2f}{}'.format(cores['verde'], prestação, cores['fim']))
if prestação == mínimo or prestação <= mínimo:
    print('Empréstimo pode ser {}CONCEDIDO ! {}'.format(cores['verde'], cores['fim']))
else:
    print('Empréstimo {}NEGADO ! {}'.format(cores['vermelho'], cores['fim']))