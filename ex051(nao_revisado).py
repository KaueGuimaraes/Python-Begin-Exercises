print('=' * 20)
print('10 termos de uma PA')
print('=' * 20)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
pula = termo + (10 - 1) * razao
for PA in range(termo, pula + razao, razao):
    print('{} '.format(PA), end='')
print('ACABOU')