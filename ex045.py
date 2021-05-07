from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2) #jogada do computador
print('{:=^50}'.format(' JOKENPÔ '))
print('''Vamos jogar JOKENPÔ?
Escolha uma das opções abaixo:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual sua jogada? ')) #jogada do usuário
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 15)
print('O computador escolheu {}.'.format(itens[computador]))
print('O Jogador escolheu {}.'.format(itens[jogador]))
print('-=' * 15)
if computador == 0: # Computador joga PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
elif computador == 1: # Computador joga PAPEL
    if jogador == 0:
        print('Computador VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador VENCE')
elif computador == 2: # Computador joga TESOURA
    if jogador == 0:
        print('Jogador VENCE')
    elif jogador == 1:
        print('Computador VENCE')
    elif jogador == 2:
        print('EMPATE')
