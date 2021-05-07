print('=-' * 10)
print('10 TERMOS DE UMA PA')
print('=-' * 10)

first_term = int(input('Primeiro termo: '))
pa_reason = int(input('Razão da PA: '))

term = first_term
count = 1

while count <= 10:
    print('{}'.format(term), end=' > ')
    term += pa_reason
    count += 1

print('FIM')
