n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

if n1>n2:
    n1,n2 = n2,n1

while n1<n2:
    n1+=1
    print(n1)
