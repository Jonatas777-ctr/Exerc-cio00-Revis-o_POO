class bola:
    def __init__(self, cor, circunferencia, material, esporte):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        self.esporte = esporte

bola1 = bola("verde", "30cm", "plástico", "futebol")
bola2 = bola("azul", "50cm", "borracha", "vôlei")

print("---------------------------------------------------------------")
print(f"A bola 1 é feita para {bola1.esporte}.")
print("---------------------------------------------------------------")