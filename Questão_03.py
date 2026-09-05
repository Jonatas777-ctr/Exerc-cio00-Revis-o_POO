class pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura


Eu = pessoa("Jonatas", "17", "58kg", "1.82")
Rhuan = pessoa("Rhuan", "16", "53kg", "1.62")

print("---------------------------------------------------------------")
print(f"Dados: {Eu.nome}, {Eu.idade}, {Eu.peso}, {Eu.altura}.")
print("---------------------------------------------------------------")