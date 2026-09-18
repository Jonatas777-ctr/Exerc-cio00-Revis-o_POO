"""Criando a classe pessoa:"""

class pessoa:
    def __init__(self, nome, idade, peso, altura): #destro do parêntesses ficam os parâmetros, que são os valores que o usuário vai me fornecer
        
        self.nome = nome #self.nome é o atributo que vai armazenar o parâmetro fornecido pelo usuário
        self.idade = idade
        self.peso = peso
        self.altura = altura

"""Criando os objetos da classe pessoa:"""

Eu = pessoa("Jonatas", "17", "58kg", "1.82")
Fulano = pessoa("Rhuan", "16", "53kg", "1.62")

"""Imprimindo os objetos da classe pessoa:"""
print("---------------------------------------------------------------")
print(f"Dados da pessoa 1: {Eu.nome}, {Eu.idade}, {Eu.peso}, {Eu.altura}.")
print(f"Dados da pessoa 2: {Fulano.nome}, {Fulano.idade}, {Fulano.peso}, {Fulano.altura}.")
print("---------------------------------------------------------------")


"""for atributo, valor in vars(Fulano).items():
    print(atributo+":",valor)"""
