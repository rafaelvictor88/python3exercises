viagem = float(input('Informe a distância da sua viagem: '))
print('Você está prestes a iniciar uma viagem de {}km.'.format(viagem))
if viagem <= 200:
    preço1 = viagem * 0.50
    print('O valor da sua viagem será R${}.'.format(preço1))
else:
    preço2 = viagem * 0.45
    print('O valor da sua viagem será R${}.'.format(preço2))
