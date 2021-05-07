import time
from random import randint
numeroescolhido = randint(0,5)
n = int(input('Digite um número: '))
print('PROCESSANDO...')
time.sleep(3)
if n == numeroescolhido:
    print('Parabéns você ganhou!')
else:
    print('Você perdeu, meu número foi {}. O computador ganhou!'.format(numeroescolhido))
