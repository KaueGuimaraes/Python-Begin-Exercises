'''from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior = numeros[0]
menor = numeros[0]
for cont in range(0, 5):
    if numeros[cont] > maior:
        maior = numeros[cont]
    if numeros[cont] < menor:
        menor = numeros[cont]
print(f'Os números sorteados foram {numeros}')
print(f'O maior valor sorteado foi {maior} \nE o menor valor sorteado foi {menor}')
print(f'{min(numeros)}, {max(numeros)}')'''
# ou
from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram {numeros}')
print(f'O mais valor foi {max(numeros)} \nE o menor número foi {min(numeros)}')