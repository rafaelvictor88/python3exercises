imóvel = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos anos será o pagamento? '))
prestação = imóvel / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(imóvel, anos, prestação))
aprovação = salário * 30 / 100
if prestação > aprovação:
    print('O empréstimo foi \033[1;31mREPROVADO\033[m!')
else:
    print('O empréstimo foi \033[1;32mAPROVADO\033[m!')
