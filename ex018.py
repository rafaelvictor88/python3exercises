from math import radians, sin, cos, tan
ang = float(input('digite um ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O ângulo é {}.'.format(ang))
print('O seno é {:.2f}.'.format(sen))
print('O cosseno é {:.2f}.'.format(cos))
print('A tangente é {:.2f}.'.format(tan))
