vet = []
for i in range(10):
   X = int(input(f"Digite o {i+1}º número inteiros: "))
   vet.append(X)

print("lista atual", vet)
vet.reverse()
print("Nova lista", vet)