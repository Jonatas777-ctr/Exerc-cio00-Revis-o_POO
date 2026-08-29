nome = input("Digite o nome do estudante: ")
soma = 0
boletim = []

for i in range(4):
   notas = float(input(f"Digite a {i+1}º nota: "))
   boletim.append(notas)
   soma = soma + notas
   media = soma / 4


   print("\n Boletim de ", nome)
   print("----------------------------------------------------------")

   for i in boletim:
      print(i)

   print("----------------------------------------------------------")
   print(f"A soma das notas do estudadnte {nome} é: {soma:.1f}")
   print(f"A média das notas do estudadnte {nome} é: {media:.1f}")

