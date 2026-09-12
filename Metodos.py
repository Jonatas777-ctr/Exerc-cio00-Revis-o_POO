"""Criando a classe pessoa:"""

class pessoa:
    def __init__(self, nome, idade, peso, altura): #destro do parêntesses ficam os parâmetros, que são os valores que o usuário vai me fornecer
        
        self.nome = nome #self.nome é o atributo que vai armazenar o parâmetro fornecido pelo usuário
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def apresentacao(self):
     print(f"O nome da pessoa consultada é {self.nome}; \nA idade dele(a) é: {self.idade};")

    def fazer_aniversario(self):
        self.idade = self.idade+1
        print(f"Feliz aniversário, {self.nome}! Você agora tem {self.idade}.")
        


"""Criando os objetos da classe pessoa:"""

Eu = pessoa("Jonatas", 17, "58kg", "1.82")
Fulano = pessoa("Rhuan", 16, "53kg", "1.62")


Eu.apresentacao()
Eu.fazer_aniversario()