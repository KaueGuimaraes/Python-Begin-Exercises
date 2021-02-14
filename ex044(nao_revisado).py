print('{:=^40}'.format(' LOJAS KAUÊ '))
preço = float(input('Preço das compras : R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcão = int(input('Qual é a sua opção ? '))
if opcão == 1:
    desconto = (preço / 100) * 10
    print('Sua compra será à vista no dinheiro ou cheque com desconto de 10%')
elif opcão == 2:
    desconto = (preço / 100) * 5
    print('Sua compra será à vista no cartão com desconto de 5%')
elif opcão == 3:
    desconto = preço
    print('Sua compra será 2x no cartão com o preço normal')
elif opcão == 4:
    desconto = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas parcelas ? '))
    parcela = desconto / totalparc
    print('Sua compra será parcelada em {}x de R${}'.format(totalparc, parcela))
else:
    desconto = 0
    print('\033[31mOPÇÂO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE !')
print('Sua compra de {} vai custar {} no final.'.format(preço, desconto))