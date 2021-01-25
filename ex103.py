def ficha(jogador='<Desconhecido>', gols=0):
    print(f'\nO jogador {jogador} fez {gols} gol(s) no campeonato')


print('========= DESAFIO 103 =========\n')

jogador = str(input('Nome do Jogador: ')).strip()
gols = str(input('Número de Gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if jogador == '':
    ficha(gols=gols)
else:
    ficha(jogador, gols)

print('\nFIM!!')