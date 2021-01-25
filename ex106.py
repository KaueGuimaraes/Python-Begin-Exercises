from time import sleep

c = {'None': '\033[m',
     'Red': '\033[0;30;41m',
     'Green': '\033[0;30;42m',
     'Yellow': '\033[0;30;43m',
     'Blue': '\033[0;30;44m',
     'Purple': '\033[0;30;45m',
     'White': '\033[7;30m'
     }


def Titulo(msg, cor='None'):
    print(f'{c[cor]}', end='')
    print('~' * (len(msg) + 4))
    print(f'  {msg}  ')
    print('~' * (len(msg) + 4))
    print(f'{c["None"]}', end='')


print('========= DESAFIO 106 =========\n')

while True:
    Titulo('SISTEMA DE AJUDA PyHELP', 'Yellow')

    sleep(0.3)
    func = str(input('Função ou Biblioteca> '))

    if func.upper() == 'FIM':
        break

    Titulo(f'Acessando o Manual do comando: "{func}"', 'Blue')
    sleep(1.2)

    print(f'{c["White"]}', end='')
    help(func)
    print(f'{c["None"]}', end='')
    sleep(0.9)

Titulo('FIM!!', 'Red')