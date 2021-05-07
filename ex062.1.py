def print_line():
    print('=-=' * 7)

print_line()
print('SUPER GERADOR DE PA')
print_line()

first_term = int(input('Primeiro termo: '))
pa_reason = int(input('Razão da PA: '))

term = first_term
count = 1
total = 0
more_terms = 10


while more_terms != 0:
    total = total + more_terms

    while count <= total:
        term += pa_reason
        count += 1
        print(' {} =>'.format(term), end='')
    print(' PAUSA')
    print_line()
    more_terms = int(input('Quantos termos você quer mostrar a mais? '))

print('Progressão finalizada com {} termos. '.format(total))
