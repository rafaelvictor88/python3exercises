number = int(input('Informe um número [999 para parar]: '))

count = 0
final_sum = 0
end = 999

while number != end:
    count += 1
    final_sum += number
    number = int(input('Informe um número [999 para parar]: '))

print('Você informou {} números e a soma de todos é {}. '.format(count, final_sum))


