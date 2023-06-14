import numpy as np
lista1 = []
lista2 = []#Numeros dias
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


op = 0
while op != 5:
    print("1.Generar plan de produccion")
    print("2.Ingresar datos de produccion")
    print("3.Calcular produccion total de una faena especifica")
    print("4.Calcular produccion total de todas las faenas en un dia especifico")    
    print("5.Salir del programa")
    op = int(input("Ingresa una opcion: "))
    if op == 1:
        lista1 = []
        lista2 = []#Numeros dias
        print("---Generar plan de produccion---")
        NumFaenas = int(input("Ingrese numero de faenas: "))
        NumDias = int(input("Ingrese numero de dias de produccion: "))
        matrizz(NumFaenas,NumDias)
        dias()
        matr = np.array(lista2)
        matriz = np.array(lista1)
        matriz2 = matriz.reshape(NumFaenas,NumDias)
        NumDia(matr)
        PlanProd(matriz2)
              
            



    elif op == 2:
        print("---Ingresar datos de produccion---")
        agregar(NumFaenas,NumDias)
        matr = np.array(lista2)
        matriz = np.array(lista1)
        matriz2 = matriz.reshape(NumFaenas,NumDias)
        NumDia(matr)
        PlanProd(matriz2)





    elif op == 3:
        print("---Calcular produccion total de una faena especifica---")





    elif op == 4:
        print("---Calcular produccion total de todas las faenas en un dia especifico---")





    elif op == 5:
        print("---Salir del programa---")
        
        