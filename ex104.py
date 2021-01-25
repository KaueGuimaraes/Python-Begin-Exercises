def leiaInt(string):
    n = str(input(string)).strip()

    while n.isnumeric() == False:
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        n = str(input(string)).strip()

    return n


print('========= DESAFIO 104 =========\n')

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

print('\nFIM!!')