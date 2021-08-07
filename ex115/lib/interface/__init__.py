def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido\033[m')
            continue
        else:
            return num

def linha(simb='-', num=42):
    return simb * num

def cabeçario(msg='Nenhum valor digitado.'):
    print(linha())
    print(msg.center(42))
    print(linha())

def menu(lista):
    cabeçario('MENU PRINCIPAL')

    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())

    opc = leiaInt('\033[33mEscolha a sua opção: \033[m')
    return opc