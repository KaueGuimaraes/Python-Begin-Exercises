# minha resposta :
num1 = int(input('Primeiro número : '))
num2 = int(input('Segundo número : '))
if num1 > num2:
    print('O \033[32mPRIMEIRO\033[m valor é maior')
elif num1 < num2:
    print('O \033[32mSEGUNDO\033[m valor é maior')
else:
    print('Não existe valor maior  os dois valores são \033[32mIGUAIS\033[m.')