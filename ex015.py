print('========= DESAFIO 015 =========\n')

dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km você andou nesse carro? '))

m = dias * 60.0
k = km * 0.15
p = k + m

print('\nO valor de aluguel a pagar será de R${} '.format(p))

print('\nFIM!!')

'''

English Version

print('========= CHALLENGE 015 =========\n')

dias = int(input('How many days have you rented this car? '))
km = float(input('How many Km you rode this car? '))

m = dias * 60.0
k = km * 0.15
p = k + m

print('\nThe value that you need to pay is ${} '.format(p))

print('\nEND!!')

'''

'''
Desafio: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
         quais ele foi alugado, Calcule o preço a pagar, sabendo que o carro custa R$60.00 por dia e R$0.15 por Km rodado.

Challenge: Make a program that asks the amount of Km traveled by a rental car and the number of days which ones it was rented
           calculate the price to pay, the car costs $60.00 per day and $0.15 per km drived.
'''