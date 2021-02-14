distancia = float(input('Qaul é a distância da sua viagem ? '))
print('Você está prestes a começar uma viagem de {}Km. '.format(distancia))
if distancia > 200.0:
    resultado = distancia * 0.45
    print('E o preço da sua passagem será de R${} '.format(resultado))
else:
    resultado = distancia * 0.50
    print('E o preço da sua passagem será de R${} '.format(resultado))
'''Este progama pergunta qual será a distância da viagem
do usuário e calcula o preço de viagem considerando que
se a viagem for maior que 200Km terá uma promoção de cada Km
percorrido custará R$00.45 mais se for maior ou igual a 200Km
a cada Km percorrido a viagem custará R$00.50'''