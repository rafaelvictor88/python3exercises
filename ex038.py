num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 == num2:
    print('Não existe valor maior, os dois são iguais!')
elif num1 > num2:
    print('O \033[1;32mPRIMEIRO\033[m valor é maior!')
else:
    print('O \033[1;36mSEGUNDO\033[m valor é maior!')
