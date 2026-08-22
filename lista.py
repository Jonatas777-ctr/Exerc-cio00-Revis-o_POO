'''
list = ["maça", "banana", "mamao"]

#print(len(list)) #mostra o tamanho da lista.

list.append('lanja') #insere um item ao final da lista.
#print("lista após o uso do append: ", list)

list.insert(0, 'caqui') #insere o item na posição desejada
#print("lista após o uso do insert: ", list)

list.insert(3, 'uva')
#print("lista após o uso do insert do item uva na posição 3: ", list)

#list.remove('caqui') #remove um item através de um valor determinado

list.pop(0) #remove o último item da lista caso o index não seja determinado

print(list)

print(list.pop(2)) #mostra o item removido 


numeros = [1,2,3,4,5]
print(numeros)

#1º forma de inserir um valor:
numeros.insert(1,0)
print(numeros)

#2º insere um valor através da subistituição:

numeros[1] = 50
print(numeros)
'''
#-------------------------------------------------------------------------------------------------------------------------------------

usuario1 = ["João", "111.333.444-07", "14/02/1990"]
print(usuario1)

usuario1[0] = "Lucas Pereira"
print(usuario1)

usuario1[2] = "14/02/2000"
print(usuario1)

usuario1.append("26 anos")
print(usuario1)

if "Lucas Pereira" in usuario1: #verifica se um item exste na lista
    usuario1.remove("Lucas Pereira")
    print(usuario1)

usuario1.clear() #apaga a lista
print(usuario1)