ter = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
PA = ter
cont = 0
while cont < 10:
   print('{} -> '.format(PA), end='')
   PA += ra
   cont += 1
print('FIM')