soma = 0
for i in range(5):
    soma += int(input(f"Insira o {i+1} número: "))

media = soma/5
print(f"A soma dos números inseridos é: {soma}")

print(f"A média dos números inseridos é: {media:.2f}")
