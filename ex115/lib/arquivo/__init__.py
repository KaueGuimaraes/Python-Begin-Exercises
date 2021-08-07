from ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mHouve um erro na criação do arquivo!\033[m')
    else:
        print('Arquivo criado com sucesso')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo!\033[m')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close()

def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('\033[31mOcorreu um ao o tentar cadastrar o usuário!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mOcorreu um erro ao tentar cadastrar o usuário!\033[m')
        else:
            print(f'{nome} foi cadastrado com sucesso!')
    finally:
        a.close()