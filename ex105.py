def notas(*num, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param num: Uma ou mais notas.
    :param sit: Para mostrar se a situação é "boa", "Ruim" ou "Razoável".
    :return: Retorna um Dicionário com informações sobre as notas.
    '''
    n = dict()
    maior = 0
    menor = 0
    cont = 0
    total = 0
    media = 0

    for c in range(0, len(num)):
        cont += 1
        total += num[c]

        if c == 0:
            menor = num[c]

        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]

    media = total / cont
    n = {'Total': cont, 'Maior': maior, 'Menor': menor, 'Média': media}

    if sit:
        if media < 5:
            situ = 'RUIM'
        elif media < 7:
            situ = 'RAZOÁVEL'
        else:
            situ = 'BOA'

        n['Situação'] = situ

    return n


print('========= DESAFIO 105 =========\n')

resp = notas(10, 9.2, 10, 10, 20, 2.3, sit=True)
print(resp)

print('\nFIM!!')