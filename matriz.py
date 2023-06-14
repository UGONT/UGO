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

arreglo_lista2 = np.array(lista2)
arreglo_lista1 = np.array(lista1)
matriz_pro = arreglo_lista1.reshape(NumFaenas,NumDias)


NumDia(arreglo_lista2)
PlanProd(matriz_pro)

num_faena = int(input("Ingrese numero de faena a calcular: "))
prod_faena = np.sum(matriz_pro[(num_faena-1),:])
print(prod_faena)

num_dia = int(input("Ingrese numero del dia a calcular: "))
prod_dia = np.sum(matriz_pro[:,(num_dia-1)])
print(prod_dia)



 













