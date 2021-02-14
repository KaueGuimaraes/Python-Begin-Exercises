valor = int(int(input('Que valor você quer sacar? R$')))
ced = 50
totced = 0
total = valor
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if ced == 50:
            ced = 20
        elif total >= ced:
            total -= ced
        else:
            if ced == 20:
                ced = 10
            elif total >= ced:
                total -= ced
                totced += 1
            else:
                if ced == 10:
                    ced == 1
                elif total >= ced:
                    total -= ced
                    totced += 1
    if total == 0:
        break
print(f'{valor} dão {totced} cédualas')