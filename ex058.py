from random import randint
numeropc = randint(0, 10)
print('=-'* 10, 'JOGO DE ADIVINHAÇÃO', '-='* 10)
print('Eu penso em um número de 0 a 10 e você tenta acertar qual foi..')
'''palpite = int(input('Qual é o seu palpite? '))
cont = 1
while palpite != numeropc:
    print('Número errado, tente novamente...')
    palpite = int(input('Qual é o seu palpite? '))
    cont += 1
print('PARABÉNS: Você precisou de {} tentativas mas... ACERTÔ MIZERÁVI.'.format(cont))'''
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == numeropc:
        acertou = True
    else:
        if jogador < numeropc:
            print('Mais... tente novamente.')
        elif jogador > numeropc:
            print('Menos... tente novamente.')
print('PARABÉNS: Você precisou de {} tentativas mas... ACERTÔ MIZERÁVI.'.format(palpites))
