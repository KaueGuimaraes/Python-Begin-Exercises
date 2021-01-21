from datetime import date

def voto(nascimento):
    idade = date.today().year - nascimento

    print(f'com {idade} anos: ', end='')
    if(idade >= 70 or idade >= 16 and idade <= 18):
        print('VOTO OPCIONAL')
    elif(idade < 16):
        print('VOTO NEGADO')
    elif(idade > 18 and idade < 70):
        print('VOTO OBRIGATÓRIO')

print('========= DESAFIO 101 =========\n')

voto(int(input('Em que ano você nasceu? ')))

print('\nFIM!!')
