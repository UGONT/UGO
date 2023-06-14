import numpy as np


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

#dias enumeracion
print("Dias       ",end=" ")
for fila in matr:
    print(fila, end="   ")
print()

#matriz plan de produccion
n = 1
for fila in matriz2:
    print(f"Faena N°{n} ",end="  ")
    n += 1
    for elemento in fila:
        print(elemento, end="  ")
    print()
