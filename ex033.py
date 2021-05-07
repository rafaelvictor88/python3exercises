a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
# verificando o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c
print('menor valor {}.'.format(menor))
# verificando o maior valor
maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
print('maior valor {}.'.format(maior))
