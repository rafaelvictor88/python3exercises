print('=' * 30)
print('{:^30}'.format(' BANCO RVGS '))
print('=' * 30)

value = int(input('Qual valor você quer sacar? R$ '))
total = value
ballot = 50
total_ballot = 0

while True:
    if total >= ballot:
        total -= ballot
        total_ballot += 1
    else:
        if total_ballot > 0:
            print(f'Total de {total_ballot} cédulas de {ballot} reais.')
        if ballot == 50:
            ballot = 20
        elif ballot == 20:
            ballot = 10
        elif ballot == 10:
            ballot = 1
        total_ballot = 0
        if total == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO RVGS! Tenha um bom dia!')