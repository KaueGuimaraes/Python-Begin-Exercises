from interface import *
from arquivo import *
from time import sleep

arq = 'lista.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    escolha = menu(['Ver pessoas cadastradas', 'Cadastrar uma nova pessoa', 'Sair'])

    if escolha == 1:
        cabeçario('PESSOAS CADASTRADAS')
        lerArquivo(arq)
    elif escolha == 2:
        cabeçario('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif escolha == 3:
        cabeçario('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! DIGITE UM OPÇÃO VÁLIDA\033[m')

    sleep(2)