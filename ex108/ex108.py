import moeda

print('========= DESAFIO 108 =========\n')

dinheiro = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(dinheiro)} é {moeda.moeda(moeda.metade(dinheiro))}')
print(f'O dobro de {moeda.moeda(dinheiro)} é {moeda.moeda(moeda.dobro(dinheiro))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(dinheiro, 10))}')
print(f'Diminuindo 10%, temos {moeda.moeda(moeda.diminuir(dinheiro, 10))}')

print('\nFIM!!')