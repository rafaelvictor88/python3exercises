from time import sleep


option_user = 0

def printline():
    print('=-' * 15)
def numbers():
    number1 = int(input('Digite um valor: '))
    number2 = int(input('Digite outro valor: '))
def options():
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior Valor
    [4] Digitar novos valores
    [5] Sair do programa''')
    option_user = int(input('Qual a sua opção? '))

number1 = int(input('Digite um valor: '))
number2 = int(input('Digite outro valor: '))

while option_user != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior Valor
    [4] Digitar novos valores
    [5] Sair do programa''')

    option_user = int(input('Qual a sua opção? '))

    if option_user == 1: #sum
        sum = number1 + number2
        print('A soma de {} + {} é {}. '.format(number1, number2, sum))
        printline()

    elif option_user == 2: #multiplication
        product = number1 * number2
        print('O produto de {} x {} é {}. '.format(number1, number2, product))
        printline()

    elif option_user == 3: #bigger value
        if number1 != number2:
            if number1 > number2:
                print('Entre {} e {} o maior valor é {}. '.format(number1, number2, number1))
            else:
                print('Entre {} e {} o maior valor é {}. '.format(number1, number2, number2))
        else:
            print('Os valores são iguais, não existe número maior.')
        printline()

    elif option_user == 4: #reboot value
        numbers()
        printline()

    elif option_user > 5: #invalid option
        print('Opção inválida, tente novamente.')

print('Finalizando o programa...')
sleep(1)
print('Programa encerrado com sucesso, volte sempre!')
