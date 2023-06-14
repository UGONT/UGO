import numpy as np

lista1 = []
lista2 = []#Numeros dias

def Matriz_plan(NumFaenas,NumDias):#matriz plan de produccion
    for i in range(NumFaenas*NumDias):
        lista1.append(0)
    return lista1

def Enumeracion_dias():#columna enumerada
    for i in range(1,NumDias+1):
        lista2.append(i)
    return lista2    

def Agregar_produccion(NumFaenas,NumDias):#agregar dato en matriz lista
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
    try:
        print("1.Generar plan de produccion")
        print("2.Ingresar datos de produccion")
        print("3.Calcular produccion total de una faena especifica")
        print("4.Calcular produccion total de todas las faenas en un dia especifico")    
        print("5.Salir del programa")
        op = int(input("Ingresa una opcion: "))

        if op == 1:
            lista1 = []
            lista2 = []
            print("---Generar plan de produccion---")
            NumFaenas = int(input("Ingrese numero de faenas: "))
            NumDias = int(input("Ingrese numero de dias de produccion: "))
            Matriz_plan(NumFaenas,NumDias)
            Enumeracion_dias()
            arreglo_lista2 = np.array(lista2)
            arreglo_lista1 = np.array(lista1)
            matriz_pro = arreglo_lista1.reshape(NumFaenas,NumDias)
            NumDia(arreglo_lista2)
            PlanProd(matriz_pro)
            print("---PLAN DE PRODUCCION GENERADO CON EXITO---")
                            
        elif op == 2:
            print("---Ingresar datos de produccion---")
            Agregar_produccion(NumFaenas,NumDias)
            arreglo_lista2 = np.array(lista2)
            arreglo_lista1 = np.array(lista1)
            matriz_pro = arreglo_lista1.reshape(NumFaenas,NumDias)
            NumDia(arreglo_lista2)
            PlanProd(matriz_pro)

        elif op == 3:
            print("---Calcular produccion total de una faena especifica---")
            suma = int(input("Ingrese numero de faena a calcular: "))
            







        elif op == 4:
            print("---Calcular produccion total de todas las faenas en un dia especifico---")





        elif op == 5:
            print("---Salir del programa---")
    except:
        print("Error")   
        