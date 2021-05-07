reta1 = float(input('Digite a medida da primeira reta: '))
reta2 = float(input('Digite a medida da segunda reta: '))
reta3 = float(input('Digite a medida da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As retas podem formar um triângulo ', end='')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO.')
    elif reta1 != reta2 != reta3 != reta1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('As retas não podem formar um triângulo. ')