salário = float(input('Qual o valor do salário do funcionário? R$'))
if salário > 1250:
    novo = salário + (salário * 10 / 100)
else:
    novo = salário + (salário * 15 / 100)
print('O seu salário passará a ser de R${:.2f}.'.format(novo))
