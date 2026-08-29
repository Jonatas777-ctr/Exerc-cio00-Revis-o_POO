list = []

for i in range(10):
   X = int(input(f"Digite o {i+1}º número inteiros: "))
   list.append(X)
 
print("Os números digitados foram:")

for i in list:
   print(i)