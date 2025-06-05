km = float(input("quantos kilometros você rodou com o carro: "))
dias = int(input("Quantos dias você alugou o carro: "))

preco_km = km * 0.15
preco_dias = dias * 60

total = (preco_km + preco_dias)

print("o total deu {: .2f}".format(total))