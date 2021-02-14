num = int(input('Digite um número: '))
cont = 0
t1 = 0
t2 = 1
print('{} -> {} -> '.format(t1, t2), end='')
cont += 2
while cont <= num:
    t3 = t1 + t2
    print(' {} ->'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' FIM')