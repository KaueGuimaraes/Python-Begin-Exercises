from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['ano de nascimento'] = int(input('Ano de Nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
pessoa['idade'] = datetime.now().year - pessoa['ano de nascimento']
if not pessoa['ctps'] == 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = (pessoa['contratação'] - pessoa['ano de nascimento']) + 35
print('-=' * 30)
for k, v in pessoa.items():
    print(' ' * 5, f'- {k} tem o valor {v}')