print('=-' * 10)
print('SUPER GERADOR DE PA')
print('=-' * 10)

first_term = int(input('Primeiro termo: '))
pa_reason = int(input('Razão da PA: '))

term = first_term
count = 1
total = 0
more_terms = 10

while more_terms != 0:
    total = total + more_terms
    while count <= total:
        print('{} => '.format(term), end='')
        term += pa_reason
        count += 1
    print('PAUSA')
    more_terms = int(input('Quantos termos você quer mostrar a mais? '))

print('Progressão finalizada com {} termos mostrados. '.format(total))
