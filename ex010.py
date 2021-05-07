real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 5.63
print('Com R${:.2f} você pode comprar {:.2f} Dólares. '.format(real, dolar))
euro = real / 6.59
print('Com R${:.2f} você pode comprar {:.2f} Euros. '.format(real, euro))
peso = real / 0.074
print('Com R${:.2f} você pode comprar {:.2f} Pesos Argentinos. '.format(real, peso))
