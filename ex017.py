from math import hypot
cato = float(input('comprimento do cateto oposto: '))
cata = float(input('comprimento do cateto adjacente: '))
hip = hypot(cato, cata)
print('A hipotenusa vai ser {:.2f}'.format(hip))
