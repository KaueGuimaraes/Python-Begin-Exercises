from random import randint
vitorias = 0
while True:
    usuario = int(input('Digite um valor: '))
    usuariop = ' '
    while usuariop not in 'PpIi':
        usuariop = str(input('Par ou Ímpar ? [P/I]: ')).lower()[0]
    if usuariop == 'p':
        computadorp = 'i'
    else:
        computadorp = 'p'
    computador = randint(0, 11)
    resultado = computador + usuario
    if resultado % 2 == 0:
        vencedor = 'PAR'
    else:
        vencedor = 'ÍMPAR'
    print(f'Voce jogou { usuario } e o computador jogou { computador } total de { resultado } deu { vencedor }')
    if vencedor == 'PAR' and usuariop == 'p':
        print('Você VENCEU !')
    elif vencedor == 'ÍMPAR' and usuariop == 'i':
        print('Você VENCEU !')
    else:
        print('Você PERDEU !')
        break
    vitorias += 1
print(f'GAME OVER ! Vocẽ venceu { vitorias } vezes')