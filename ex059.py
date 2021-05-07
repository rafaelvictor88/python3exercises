from time import sleep


options = 0

n1 = int(input('Me diga um valor: '))
n2 = int(input('Me diga mais um valor: '))
print('=-' * 15)

while options != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    options = int(input('Qual a sua opção? '))

    if options == 1: #sum
        sum = n1 + n2
        print('A soma de {} e {} é {}.'.format(n1, n2, sum))
        print('=-' * 15)

    if options == 2: #multiplication
        produto = n1 * n2
        print('A multiplicação de {} e {} é {}.'.format(n1, n2, produto))
        print('=-' * 15)

    if options == 3: #bigger value
        if n1 != n2:
            if n1 < n2:
                print('Entre {} e {} o maior é o número {}.'.format(n1, n2, n2))
            if n1 > n2:
                print('Entre {} e {} o maior é o número {}.'.format(n1, n2, n1))
            print('=-' * 15)
        else:
            print('Os números {} e {} são iguais.'.format(n1, n2))
            print('=-' * 15)

    if options == 4: #reboot value
        n1 = int(input('Me diga um valor: '))
        n2 = int(input('Me diga mais um valor: '))
        print('=-' * 15)

    if options > 5: #invalid option
        print('Opção inválida, tente mais uma vez.')
        print('=-' * 15)

print('Encerrando o programa...')
sleep(1)
print('Programa finalizado, volte sempre.')
