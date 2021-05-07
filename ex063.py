def print_line():
    print('-' * 25)

print_line()
print('SEQUÊNCIA DE FIBONACCI')
print_line()

how_many_terms = int(input('Quantos termos você quer mostrar? '))

first_term = 0
second_term = 1

print('{} => {} => '.format(first_term, second_term), end='')

count = 3

while count <= how_many_terms:
    third_term = first_term + second_term
    print('{} => '.format(third_term), end='')
    first_term = second_term
    second_term = third_term
    count += 1

print('FIM')