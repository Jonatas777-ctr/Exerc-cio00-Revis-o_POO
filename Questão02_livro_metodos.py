class livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def mostrar_tudo(self):
     print(f"Dados do livro: autor: {livro1.autor}, titulo: {livro1.titulo}, ano: {livro1.ano}.")

    def editar_titulo(self, novo_titulo):
       self.titulo = novo_titulo
       print(f"O novo título do livro é: {self.titulo}")
       


livro1 = livro("Dom Casmurro", "Machado de Assis", "1899")

print("--------------------------------------------------------------------------------")
print(f"O titulo do livro é {livro1.titulo}.")
livro1.mostrar_tudo()
livro1.editar_titulo("Traiu ou não traiu?")
livro1.mostrar_tudo()
print("--------------------------------------------------------------------------------")      