jogador = {}
segund = []
soma = 0
jogador['gols'] = 0
jogador['nome'] = str(input('Nome do Jogador: '))
cont = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, cont):
    segund.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {c}? ')))
    jogador['gols'] = segund[:]
for i in range(0, len(jogador['gols'])):
    soma += jogador['gols'][i]
jogador['total'] = soma
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {cont} partidas.')
for c in range(0, len(jogador["gols"])):
    print(' ' * 5, f'=> Na partida {c} ele fez {jogador["gols"][c]} gols')
print(f'Foi um total de {jogador["total"]} gols')