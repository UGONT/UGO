import numpy as np

lista = []
lista2 = []
NumFaenas = int(input("Ingrese numero de faenas: "))
NumDias = int(input("Ingrese numero de dias: "))

for i in range(NumFaenas*NumDias):
    lista.append(0)

for i in range(1,NumDias+1):
    lista2.append(i)

matr = np.array(lista2)



matriz = np.array(lista)
matriz2 = matriz.reshape(NumFaenas,NumDias)
#print(matriz2)

print(matr)
for fila in matr:
    print(fila, end=" ")



for fila in matriz2:
    for elemento in fila:
        print(elemento, end=" ")
    print()



'''
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
for fila in matrix:
    for elemento in fila:
        print(elemento, end=" ")
    print()
'''