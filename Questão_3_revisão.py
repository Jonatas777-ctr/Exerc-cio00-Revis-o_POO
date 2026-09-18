i = input("Olá, em que turno você estuda?(M-matutino, V-vespertino, N-noturno) ").upper()
if i == "M":
    print("Bom Dia!")
elif i == "V":
    print("Boa Tarde!")
elif i == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido")
