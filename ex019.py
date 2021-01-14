from random import choice

print('========= DESAFIO 019 =========\n')

n1 = str(input('Primeiro aluno : ')).capitalize().strip()
n2 = str(input('Segundo aluno : ')).capitalize().strip()
n3 = str(input('Terceiro aluno : ')).capitalize().strip()
n4 = str(input('Quarto aluno : ')).capitalize().strip()

lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print('\naluno escolhido foi {} '.format(escolhido))

print('\nFIM!!')