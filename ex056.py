somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher = 0
for pessoa in range (1, 5):
    print('=' * 5, '{}ª PESSOA'.format(pessoa), '=' * 5)
    nome = str(input('Qual o nome? ')).strip()
    idade = int(input('Qual a idade? '))
    sexo = str(input('Qual é o sexo [M/F]? ')).strip()
    somaidade += idade
    if pessoa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {:.0f} anos. '.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}. '.format(maioridadehomem, nomevelho))
print('No grupo temos {} mulheres menores de 20 anos. '.format(mulher))
