nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Quem tirou {} e {}, tem a média de {}.'.format(nota1, nota2, media))
if media < 5.0:
    print('O aluno está \033[1;31mREPROVADO\033[m.')
elif media >= 5.0 and media < 7.0:
    print('O aluno está em \033[1;33mRECUPERAÇÃO\033[m.')
elif media >= 7.0:
    print('O aluno está \033[1;32mAPROVADO\033[m.')
