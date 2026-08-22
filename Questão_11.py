lista = []
#roda 5 vezes para o usuario digitar os números
for i in range(5):
   X = int(input(f"Digite o {i+1} número inteiros: "))
   lista.append(X)

#exibe cada item da lista
for i in lista:
   print(i)
