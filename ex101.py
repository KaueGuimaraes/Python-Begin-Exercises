def voto(nascimento):
    from datetime import date

    idade = date.today().year - nascimento
    if(idade >= 70 or idade >= 16 and idade < 18):
        return f'\ncom {idade} anos: VOTO OPCIONAL'
    elif(idade < 16):
        return f'\ncom {idade} anos: VOTO NEGADO'
    else:
        return f'\ncom {idade} anos: VOTO OBRIGATÓRIO'


print('========= DESAFIO 101 =========\n')

print(voto(int(input('Em que ano você nasceu? '))))

print('\nfim!!')
