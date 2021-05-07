count = sum = 0

while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    count += 1
    sum += num
print(f'A soma dos {count} números é {sum}.')
print('Programa finalizado!')
