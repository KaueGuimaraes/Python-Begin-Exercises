carro = int(input('Qual é a velocidade atual do carro ? ')) #Coletando informações
if carro == 80:
    print('Tenha um bom dia! Dirija com segurança! ')
if carro <= 80:
    print('Tenha um bom dia! Dirija com segurança! ')
else:
    carro = carro - 80 #Se o usuário utrapassar 80KM/h ele terá que pagar uma multa a cada KM acima do limitre o usuário pagará R$7.00 mas se não Tenha um bom dia! Dirija com segurança!
    carro = carro * 7.0
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h \n Você deve pagar uma multa de R${}! \n Tenha um bom dia! Diriga com segurança!'.format(carro))