a = int(input('Primeiro valor : '))
b = int(input('Segundo valor : '))
c = int(input('Terceiro valor : '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('Menor : {} '.format(menor))
print('Maior : {} '.format(maior))
'''Neste progama o usuário digita três números e o computador
fala qual é o maior número e qual é o menor número'''