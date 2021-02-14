pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['média'] = float(input(f'Média de {pessoa["nome"]}: '))
if pessoa['média'] >= 7:
    pessoa['situação'] = 'Aprovado'
elif 5 <= pessoa['média'] < 7:
    pessoa['situação'] = 'Recuperação'
else:
    pessoa['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in pessoa.items():
    print(' ' * 5, f'- {k} é igual a {v}')