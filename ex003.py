n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
texto = 'A soma de \033[1;30m{}\033[m e \033[1;31m{}\033[m vale \033[1;32m{}\033[m. '
print(texto.format(n1, n2, s))
