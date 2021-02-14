jogador = {}
segund = []
jogadores = []
soma = 0
c = 0
terc = []
continu = ' '
while True:
    jogadores.append(jogador.copy())
    jogadores[c]['nome'] = str(input('Nome do Jogador: '))
    cont = int(input(f'Quantas partidas {jogadores[c]["nome"]} jogou? '))
    for t in range(0, cont):
        segund.append(int(input(f'Quantos gols {jogadores[c]["nome"]} fez na partida {t + 1}? ')))
        jogadores[c]['gols'] = segund[:]
    for i in range(0, len(jogadores[c]['gols'])):
        soma += jogadores[c]['gols'][i]
    jogadores[c]['total'] = soma
    terc.append(c)
    c += 1
    segund.clear()
    continu = str(input('Quer continuar? [S/N] ')).upper()[0]
    while continu not in 'SsNn':
        print('ERRO! Digite apenas S ou N.')
        continu = str(input('Quer continuar? [S/N] ')).upper()[0]
    if continu in 'Nn':
        break
print('-=' * 30)
print('cod', ' nome', ' ' * 10, 'gols', ' ' * 10, 'total')
print('-' * 50)
for c in range(0, len(jogadores)):
    print(f'  {c + 1} {jogadores[c]["nome"]}', ' ' * 10, f'{jogadores[c]["gols"]}', f' ' * 10, f'{jogadores[c]["total"]}')
while True:
    m = int(input('Mostrar dados de qual jogador? (999 para parar) ')) - 1
    if m + 1 == 999:
        break
    if m not in terc:
        print('ERRO! Digite um valor válido.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[m]["nome"]} --')
        for j in range(0, len(jogadores[m]['gols'])):
            print(' ' * 5, f'No jogo {j + 1} fez {jogadores[m]["gols"][j]}')