salário = float(input('Digite seu salário R$'))
novo = salário + (salário * 15 / 100)
print('Seu salário que era R${:.2f}, com 15% de aumento, passou a ser R${:.2f}. '.format(salário, novo))
