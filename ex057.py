sex = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]

while sex not in 'MmFf':
    sex = str(input('Resposta inválida, tente novamente. Qual é o seu sexo? [M/F] ')).strip().upper()[0]

print('Sexo {} resgistrado com sucesso. '.format(sex))
