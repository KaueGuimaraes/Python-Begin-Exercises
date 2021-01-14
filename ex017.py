from math import hypot

print('========= DESAFIO 017 =========\n')

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('COmprimento do cateto adjacente: '))

hi = (co ** 2 + ca ** 2) ** (1/2) #Primeiro jeito.
hi = hypot(co, ca) #Segundo jeito.

print('\nA hipotenusa vai medir {:.2f}'.format(hi))

print('\nFIM!!')

'''

English Version

from math import hypot

print('========= CHALLENGE 017 =========\n')

co = float(input('Opposite side length: '))
ca = float(input('Adjacent side length: '))

hi = (co ** 2 + ca ** 2) ** (1/2) #First Mode.
hi = hypot(co, ca) #Second Mode.

print('\nThe hypotenuse measure is {:.2f}'.format(hi))

print('\nEND!!')

'''

'''
Desafio: Faça um programa que leia o comprimento do cateto oposto e do cateto
         adjacente de um triângulo retângulo, calcule e mostre o comprimento
         da hipotenusa.
Challenge: Make a program that reads the Opposite side length and the adjacent
           side length of a triangle, shows its hypotenuse length.
'''