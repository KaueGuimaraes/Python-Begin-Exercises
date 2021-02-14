continuar = ' '
alunos = []
segund = []
média = 0
cont = -1
c = []
while continuar not in 'Nn':
    continuar = ' '
    alunos.append(segund[:])
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    for p in range(0, len(alunos)):
        if len(alunos[p]) == 0:
            alunos[p].append(nome)
            alunos[p].append(nota1)
            alunos[p].append(nota2)
    cont += 1
    c.append(cont)
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] '))[0]
print('-' * 30, '\nNo.  NOME', ' ' * 10, 'MÉDIA', '\n', '-' * 30)
for aluno in range(0, len(alunos)):
    média = (alunos[aluno][1] + alunos[aluno][2]) / 2
    print(f'{aluno}', ' ' * 3, f'{alunos[aluno][0]}', ' ' * 15, f'{média}')
while True:
    mostrar = int(input('\nMostrar nota de qual aluno? (999 interrompe): '))
    print('\n', '-=' * 15)
    if mostrar == 999:
        break
    elif mostrar not in c:
        print('INVÁLIDO TENTE NOVAMENTE!')
    else:
        print(f'As notas de {alunos[mostrar][0]} foram {alunos[mostrar][1]}, {alunos[mostrar][2]}')
    print('-=' * 15)
print('Obrigado por usar meu programa :3')