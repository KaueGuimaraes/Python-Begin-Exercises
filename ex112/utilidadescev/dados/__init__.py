def leiaDinheiro(msg):
    while True:
        v = str(input(msg)).strip().replace(',', '.')
        if v.isalpha() or v == '':
            print(f'\033[31mERRO! {v} é um preço inválido!\033[m')
        else:
            break

    return float(v)