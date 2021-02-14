ex = str(input('Digite uma expressão: '))
pf = [] # )
pa = [] # (
for l in range(0, len(ex)):
    if ex[l] == '(':
        pa.append(ex[l])
    elif ex[l] == ')':
        pf.append(ex[l])
if len(pa) == len(pf):
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')