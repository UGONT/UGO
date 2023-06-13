import numpy as np
import random as rd

lista = []
lista2 = []#Numeros dias
NumFaenas = int(input("Ingrese numero de faenas: "))
NumDias = int(input("Ingrese numero de dias: "))



#matriz plan de produccion
for i in range(NumFaenas*NumDias):
    lista.append(0)
#columna enumerada 
for i in range(1,NumDias+1):
    lista2.append(i)

#agregar dato en matriz lista
for i in range(NumFaenas*NumDias):
    print(f"Ingrese Tonelada N°{i+1}: ")
    tonelada= int(input())
    lista[i] = tonelada

#listas arreglos
matr = np.array(lista2)

matriz = np.array(lista)
matriz2 = matriz.reshape(NumFaenas,NumDias)

#matriz enumerada
for fila in matr:
    print(fila, end="   ")
print()

#matriz plan de produccion
for fila in matriz2:
    print(f"Faena  ")
    for elemento in fila:
        print(elemento, end="  ")
    print()

lista.append(rd.randint(0,50))

'''
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
for fila in matrix:
    for elemento in fila:
        print(elemento, end=" ")
    print()
'''