class livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano


livro1 = livro("Dom Casmurro", "Machado de Assis", "1899")

print("---------------------------------------------------------------")
print(f"O titulo do livro é {livro1.titulo}.")
print("---------------------------------------------------------------")
