from datetime import date
anoatual = date.today().year
nascimento = int(input('Qual o ano de nascimento do atleta? '))
idade = anoatual - nascimento
print('O atleta tem {} anos de idade.'.format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM.')
elif idade <= 14:
    print('Sua categoria é INFANTIL.')
elif idade <= 19:
    print('Sua categoria é JÚNIOR.')
elif idade <= 25:
    print('Sua categoria é SÊNIOR.')
else:
    print('Sua categoria é MASTER.')
