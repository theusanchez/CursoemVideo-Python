altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
print('Com uma parede de {} metros quadrados, você precisaria de {} litros de tinta'.format(area, (area/2)))