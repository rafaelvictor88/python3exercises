stop = 'S'
count = average = sum = higher = lower = 0

while stop in 'Ss':
    number = int(input('Digite um número: '))
    count += 1
    sum += number
    if count == 1:
        higher = lower = number
    else:
        if number > higher:
            higher = number
        if number < lower:
            lower = number
    stop = str(input('Quer continuar? [S/N] '))

average = sum / count

print('Você digitou {} números e a média entre eles é {}. '.format(count, average))
print('O maior número foi {} e o menor número foi {}. '.format(higher, lower))
