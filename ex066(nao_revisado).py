cont = tot = 0
while True:
    num = int(input('Digite um número [999 parar]: '))
    if num == 999:
        break
    cont += 1
    tot += num
print(f'Você digitou { cont } números, e no total deu { tot }')