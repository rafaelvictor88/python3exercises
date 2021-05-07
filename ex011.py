largura = float(input('Qual a largura da sua parede? '))
altura = float(input('Qual a altura da sua parede? '))
area = largura * altura
print('A sua parede tem a dimensão de {} x {} e uma área de {}. '.format(largura, altura, area))
litros = area / 2
print('Pra pintar uma área de {}m², você precisará de {}L de tinta. '.format(area, litros))
