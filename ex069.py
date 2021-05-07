more18 = totalMale = femaleU20 = 0

while True:
    age = int(input('Idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo: [M/F]')).strip().upper()[0]
    if age >= 18:
        more18 += 1
    if sex == 'M':
        totalMale += 1
    if sex == 'F' and age < 20:
        femaleU20 += 1

    stop = ' '
    while stop not in 'SN':
        stop = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if stop == 'N':
        break

print(f'Pessoas cadastradas com mais de 18 anos: {more18}.')
print(f'Total de homens cadastrados: {totalMale}.')
print(f'Total de mulheres com menos de 20 anos cadastradas: {femaleU20}.')
#
# stop = 'SN'
# female_U20 = male = age_more_18 = 0
#
# while True:
#     age = int(input('Informe a idade da pessoa: '))
#     # aqui eu preciso validar a idade.
#     if age <= 0:
#         print('Idade inválida, tente novamente...')
#         continue
#
#     sex = str(input('Informe o sexo da pessoa [M/F]: ')).strip().upper()[0]
#     # aqui eu preciso validar o sexo.
#     if sex != 'F' and sex != 'M':
#         print('Sexo inválido, tente novamente...')
#         continue
#
#     # contador sexo.
#     if sex == 'F':
#         if age < 20:
#             female_U20 += 1
#     elif sex == 'M':
#         male += 1
#
#     # contador idade.
#     if age > 18:
#         age_more_18 += 1
#
#     stop = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
#     if stop == 'N':
#         print('Programa encerrado!')
#         break
#
# print(f'''Tivemos {age_more_18} com mais de 18 anos,
# {male} homens e
# {female_U20} mulheres com menos de 20 anos,
# cadastrados no nosso sistema!''')
