from random import randint
from time import sleep
princ = []
segund = []
cont = int(input('Quantos jogos você quer que eu s19orteie? '))
for c in range(0, cont):
    princ.append(segund[:])
    for l in range(0, 6):
        while True:
            num = randint(1, 60)
            if num not in princ[c]:
                princ[c].append(num)
                break
    print(f'Jogo {c + 1}: {princ[c]}')
    sleep(0.5)
print(f'BOA SORTE !!')