from random import randint


correct = False
guests = 0
computer = randint(0, 10)

print('=-=' * 5, 'JOGO DA ADIVINHAÇÃO', '=-=' * 5)
print('Vou pensar em número de 0 a 10 e você tem que adivinhar qual foi...')

while not correct:
    userguest = int(input('Qual o seu palpite? '))
    guests += 1

    if userguest == computer:
        correct = True

    else:
        if userguest > computer:
            print('Menos... tente novamente.')
        elif userguest < computer:
            print('Mais... tente novamente.')

print('Você precisou de {} tentativas mas, ACERTÔ MISERÁVI...'.format(guests))