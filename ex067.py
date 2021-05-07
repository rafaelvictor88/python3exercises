number = 0

while True:
    number = int(input('Digite um número para ver sua tabuada: '))
    print('=' * 12)
    if number < 0:
        print('Programa de tabuada encerrado. Volte sempre!')
        break
    for c in range(1, 11):
       # product = number * c
       # print(f'{number} x {c} = {product}')
        print(f'{number} x {c} = {number * c}')
    print('=' * 12)
