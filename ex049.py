n = int(input('Digite um número e saiba sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, c*n))