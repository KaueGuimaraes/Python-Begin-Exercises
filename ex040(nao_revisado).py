nota1 = float(input('Primeira nota : '))
nota2 = float(input('Segunda nota : '))
média = (nota1 + nota2) / 2
print('tirando {} e {}, a média do aluno é {}'.format(nota1, nota2, média))
if média == 7.0 or média > 7.0:
    print('O aluno está \033[32mAPROVADO\033[m !')
elif média > 5.0 or média == 5.0:
    print('O aluno está em \033[31mRECUPERAÇÂO\033[m !')
else:
    print('O aluno está \033[31mREPROVADO\033[m !')