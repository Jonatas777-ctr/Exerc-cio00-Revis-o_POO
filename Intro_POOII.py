class carro:
    def __init__(self, cor, marca, modelo, combustivel):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.combustivel = combustivel

polo = carro("azul", "volkswagen", "polo", "gasolina")
mustang = carro("verde", "ford", "mustang", "gasolina")
prius = carro("vermelho", "toyota", "prius", "eletricidade")
golf = carro("azul", "volkswagen", "golf", "diesel")

print("---------------------------------------------------------------")
print(f"A cor do {prius.modelo} é: {prius.cor}.")
print("---------------------------------------------------------------")