frase = str(input('Digite uma frase : ')).upper().strip() #Coletando informações
print('A letra A aparece {} vez(s) na frase '.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição {} '.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {} '.format(frase.rfind('A')+1))
'''Neste progama o usuário digita uma frase e o progama diz informações sobre a frase digitada'''