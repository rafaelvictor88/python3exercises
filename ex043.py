peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O seu IMC é \033[1:35m{:.1f}\033[m.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal!')
elif imc >= 25 and imc < 30:
    print('Você está com Sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Você está Obeso!')
else:
    print('Você está com Obesidade Mórbida!')
