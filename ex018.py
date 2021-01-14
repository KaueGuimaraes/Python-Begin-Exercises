from math import radians, sin, cos, tan

print('========= DESAFIO 018 =========\n')

an = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))

print('\nO ângulo de {} tem o SENO de {:.2f}'.format(an, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, tangente))

print('\nFIM!!')

'''

English Version

from math import radians, sin, cos, tan

print('========= CHALLENGE 018 =========\n')

an = float(input('Type the angle that you wanna: '))

seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))

print('\nThe SINE of {} is {:.2f}'.format(an, seno))
print('The COSINE of {} is {:.2f}'.format(an, cosseno))
print('The TANGENT of {} is {:.2f}'.format(an, tangente))

print('\nEND!!')

'''

'''
Desafio: Faça um programa que leia um ângulo qualquer e mostre na tela
         o valor do seno, cosseno e tangente desse ângulo.
Challenge: Write a program that reads a angle, and shows in the screen
           sine, cosine and tangent of this angle.
'''