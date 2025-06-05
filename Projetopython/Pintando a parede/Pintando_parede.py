largura_p = int(input("Digite a largura da parede: "))
altura_p = int(input("Digite a altura da parede: "))

baldes_de_tinta = 2
area = altura_p * largura_p

pintando_parede = area / baldes_de_tinta

print("a parede tem area de {}m² logo vai precisar de {} baldes de tinta para pintala".format(area, pintando_parede))
