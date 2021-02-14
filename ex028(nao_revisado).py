from random import randint
from time import sleep
n = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar... ')
print('-=-' * 20)
m = int(input('Em que número eu pensei ? '))
print('PROCESSANDO...')
sleep(3)
if m == n:
    print('PARABÉNS ! Você acertou eu pensei em {} ! '.format(n))
else:
    print('Você perdeu eu pensei em {} ! '.format(n))
'''Este progama é tipo um joguinho naverdade é
o computador pensa em um número de 0 a 5 e pede para você adivinhar se você acertar o progama mostrará essa mensagem :
PARABÉNS ! Você acertou eu pensei em {}
mais se você não acertar ele mostrará essa mensagem
Você perdeu eu pensei em {} !'''