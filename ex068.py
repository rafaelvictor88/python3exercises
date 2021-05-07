from random import randint

count_victory = 0 #contador de vitórias

while True:
    player = int(input('Jogue um número: '))
    computer = randint(0, 10)
    total = player + computer
    choice = ' '
    while choice not in 'PI':
        choice = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {player} e o computador jogou {computer}, a soma é {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if choice == 'P': #par
        if total % 2 == 0:
            print('Boa jogada, VOCÊ VENCEU!')
            count_victory += 1
        else:
            print('Que pena, VOCÊ PERDEU!')
            break
    elif choice == 'I': #ímpar
        if total % 2 == 1:
            print('Boa jogada, VOCÊ VENCEU!')
            count_victory += 1
        else:
            print('Que pena, VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'Você venceu {count_victory} vezes.')
