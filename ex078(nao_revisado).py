num = []
for c in range(0, 5):
    num.append(int(input(f'Digite um número para a posição {c}: ')))
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {max(num)} nas posições: ', end='')
for pos in range(0, len(num)):
    if num[pos] == max(num):
        print(f' {pos}...', end='')
print(f'\nO menor valor digitado foi {min(num)} nas posições: ', end='')
for pos in range(0, len(num)):
    if num[pos] == min(num):
        print(f' {pos}...', end='')