from random import shuffle

print('========= DESAFIO 020 =========\n')

n1 = str(input('Primeiro aluno: ')).capitalize().strip()
n2 = str(input('Segundo aluno: ')).capitalize().strip()
n3 = str(input('Terceito aluno: ')).capitalize().strip()
n4 = str(input('Quero aluno: ')).capitalize().strip()

lista = [n1, n2, n3, n4]
shuffle(lista)

print('\nA ordem de apresentação será: ')
print(lista)

print('znFIM!!')