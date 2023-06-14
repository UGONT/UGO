import numpy as np

lista1 = []#matriz toneladas
lista2 = []#dias


def matrizz(NumFaenas,NumDias):#matriz plan de produccion
    
    for i in range(NumFaenas*NumDias):
        lista1.append(0)
    return lista1

def dias():#columna enumerada
    for i in range(1,NumDias+1):
        lista2.append(i)
    return lista2    

def agregar(NumFaenas,NumDias):#agregar dato en matriz lista
    for i in range(NumFaenas*NumDias):
        print(f"Ingrese Tonelada N°{i+1}: ")
        tonelada= int(input("->"))
        lista1[i] = tonelada
    return lista1







def NumDia(matr):#dias enumeracion
    print("Dias       ",end=" ")
    for fila in matr:
        print(fila, end="   ")
    print()
    return NumDia

def PlanProd(matriz2):#matriz plan de produccion
    n = 1
    for fila in matriz2:
        print(f"Faena N°{n} ",end="  ")
        n += 1
        for elemento in fila:
            print(elemento, end="  ")
        print()
    return PlanProd



NumFaenas = int(input("Ingrese numero de faenas: "))
NumDias = int(input("Ingrese numero de dias: "))


matrizz(NumFaenas,NumDias)
dias()
agregar(NumFaenas,NumDias)

matr = np.array(lista2)
matriz = np.array(lista1)
matriz2 = matriz.reshape(NumFaenas,NumDias)


NumDia(matr)
PlanProd(matriz2)





 













