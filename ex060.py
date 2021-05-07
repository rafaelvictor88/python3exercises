number = int(input('Informe um número: '))

count = number
factorial = 1

print('Calculando {}! = '.format(number), end='')

for c in range(number, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    factorial *= count
    count -= 1

print('{}'.format(factorial), end='')

#while count > 0:
   # print('{}'.format(count), end='')
  #  print(' x ' if count > 1 else ' = ', end='')
 #   factorial *= count
#    count -= 1

#print('{}.'.format(factorial))

#from math import factorial

#n = int(input('Digite um número para calcular seu Fatorial: '))
#f = factorial(n)
#print('O Fatorial de {} é {}. '.format(n, f))


