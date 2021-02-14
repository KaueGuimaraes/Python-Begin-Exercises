from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
computador = randint(0, 2)
jogador = int(input('Qual é a sua jogada ? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-' * 11)
print('Computador escolheu {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=-' * 11)
if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('\033[31mEMPATE')
    elif jogador == 1:
        print('\033[32mJOGADOR VENCE')
    elif jogador == 2:
        print('\033[31mCOMPUTADOR VENCE')
    else:
        print('\033[31mJOGADA INVÁLIDA!')
elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print('\033[31mCOMPUTADOR VENCE')
    elif jogador == 1:
        print('\033[31mEMPATE')
    elif jogador == 2:
        print('\033[32mJOGADOR VENCE')
    else:
        print('\033[31mJOGADA INVÁLIDA!')
elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print('\033[32mJOGADOR VENCE')
    elif jogador == 1:
        print('\033[31mCOMPUTADOR VENCE')
    elif jogador == 2:
        print('\033[31mEMPATE')
    else:
        print('\033[31mJOGADA INVÁLIDA!')
''' Minha resposta :

from random import choice
from time import sleep
lista = ['pedra', 'papel', 'tesoura']
pensamento = choice(lista)
pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'
print('\033[35mJokenpô ')
b = input('\033[35m: ').lower().strip()
if b == pensamento:
    print('\033[31mEMPATOU\033[mEu também escolhi {} !'.format(pensamento))
if b == tesoura and pensamento == pedra or b == papel and pensamento == tesoura or b == pedra and pensamento == papel:
    print('\033[31mHAHA ! EU GANHEI !\033[31m EU ESCOLHI {} E VOCÊ ESCOLHEU {} HAHA ! '.format(pensamento, b))
elif b == tesoura and pensamento == papel or b == papel and pensamento == pedra or b == pedra and pensamento == tesoura:
    print('\033[32mPARABÉNS ! Você vençeu ! você escolheu {} e eu escolhi {} '.format(b, pensamento))'''