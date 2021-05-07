velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('A sua velocidade é {}. Você foi multado, reduza a velocidade!'.format(velocidade))
    multa = (velocidade - 80)*7
    print('Você deve pagar {}'.format(multa))
else:
    print('Dirija com cuidado, boa viagem!')
