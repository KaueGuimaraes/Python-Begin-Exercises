ter = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
mostrar = 10
PA = ter
mostrados = 0
while mostrar != 0:
    print('{} -> '.format(PA), end='')
    mostrar -= 1
    PA += ra
    if mostrar == 0:
        print('PAUSA')
        mostrar = int(input('Quantos termos você quer mostrar a mais? '))
    mostrados += 1
print('Progressão finalizada com {} termos mostrados.'.format(mostrados))