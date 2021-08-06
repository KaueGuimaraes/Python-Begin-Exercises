def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido\033[m')
            continue
        else:
            return num

def leiaFloat(msg):
    while True:
        while True:
            num = str(input(msg)).replace(',', '.')

            try:
                return float(num)
            except (ValueError, TypeError):
                print('\033[31mERRO: Por favor, digite um número inteiro válido\033[m')
                continue