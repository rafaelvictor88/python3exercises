print('{:=^40}'.format(' VICTOR STORE '))
preço = float(input('Qual é o preço do produto? R$'))
print('''OPÇÕES DE PAGAMENTO:
[1] À VISTA DINHEIRO/CHEQUE.
[2] À VISTA NO CARTÃO.
[3] ATÉ 2X NO CARTÃO.
[4] 3X OU MAIS NO CARTÃO.''')
opção = int(input('Sua opção: '))
if opção == 1:
    valorfinal = preço - (preço * 10 / 100)
    print('O valor do produto com 10% de desconto será R${:.2f}.'.format(valorfinal))
elif opção == 2:
    valorfinal = preço - (preço * 5 / 100)
    print('O valor do produto com 5% de desconto será R${:.2f}.'.format(valorfinal))
elif opção == 3:
    valorfinal = preço / 2
    print('Nessa forma de pagamento não temos descontos ', end=''
          'e você pagará o produto em 2 parcelas de R${:.2f}.'.format(valorfinal))
elif opção ==4:
    valorfinal = preço + (preço * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    prestações = valorfinal / parcelas
    print('''O preço do produto com juros de 20% será R${:.2f}.
Você pagará em {}x de R${:.2f}.'''.format(valorfinal, parcelas, prestações))
else:
    print('OPÇÃO INVÁLIDA, tente novamente!')
