from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
print('Valores sorteados:')
for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(1, 6)
    print(f'jogador{c} tirou {jogadores[f"jogador{c}"]} no dado.')
    sleep(1)
ranking = list()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('RANKING:')
for c in range(1, 5):
    print(f'{c} lugar: {ranking[c - 1][0]} com {ranking[c - 1][1]}')
    sleep(1)