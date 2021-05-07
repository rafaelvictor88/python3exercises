from datetime import date
atual = date.today().year
ano = int(input('Digite o seu ano de nascimento: '))
idade = atual - ano
alistamento = ano + 18
if idade < 18:
    temporestante = 18 - idade
    print('Quem nasceu em {}, tem hoje {} anos de idade.\n'
          'Ainda faltam {} anos para os eu alistamento, '
          'que acontecerá em {}.'.format(ano, idade, temporestante, alistamento))
elif idade > 18:
    tempopassado = idade - 18
    print('Quem nasceu em {}, tem hoje {} anos de idade.\n'
          'Já se passaram {} anos do seu alistamento, '
          'que deveria ter sido em {}.'.format(ano, idade, tempopassado, alistamento))
else:
    print('Quem nasceu em {}, tem hoje 18 anos de idade.\n'
          'Seu alistamento deve ser IMEDIATO.'.format(ano))
