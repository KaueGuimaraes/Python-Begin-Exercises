import moeda

print('========= DESAFIO 107 =========\n')

dinheiro = float(input('Digite o preço: R$'))
print(f'A metade de R${dinheiro} é R${moeda.metade(dinheiro)}')
print(f'O dobro de R${dinheiro} é {moeda.dobro(dinheiro)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(dinheiro, 10)}')
print(f'Diminuindo 10%, temos R${moeda.diminuir(dinheiro, 10)}')

print('\nFIM!!')