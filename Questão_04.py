class aluno:
    def __init__(self, matricula, nome, nota1, nota2, nota3, nota4, nota5):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.nota5 = nota5

aluno1 = aluno("123", "Jonatas", 6, 8, 7, 10, 9)
aluno2 = aluno("321", "Fulano", 5, 9, 2, 8, 3)
aluno3 = aluno("765", "Ciclano", 8, 3, 4, 9, 2)  

print("---------------------------------------------------------------")
print(aluno1.__dict__)
print(aluno2.__dict__)
print(aluno3.__dict__)
print("---------------------------------------------------------------") 