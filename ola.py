import numpy as np

lista = []

def agregar_datos(lista,nif,nombre,edad,europea):
    lista.append(nif)
    lista.append(nombre)
    lista.append(edad)
    lista.append(europea)

def buscar_nif(busqueda,matriz):
    for fila in matriz:
        if fila[0] == busqueda:
            return True
    return False

def pertenece(eu):
    if eu == 1:
        return True
    else:
        return False
    
def certificado(busqueda,matriz):
    for fila in matriz:
        if fila[0] == busqueda:
            print(fila)
    return False
    

op = 0
while op != 4:
    print("1.Grabar")
    print("2.Mostrar matriz")
    print("3.Buscar")
    print("4.Salir")
    op = int(input("opcion: "))
    if op == 1:
        nif = input("nif: ")
        nombre = input("nombre: ")
        edad = input("edad: ")
        eu = int(input("Perteneces a la union europea?\n1.Si\n2.No\n->"))
        
        if pertenece(eu) == True:
            europea = "Pertenece a EU"
        else:
            europea = "No pertenece a EU"    
        agregar_datos(lista,nif,nombre,edad,europea)
        arreglo_1 = np.array(lista)
        n_filas = int(len(arreglo_1)/4)
        matriz = arreglo_1.reshape(n_filas,4)



    elif op == 2:
        print("Mostrar matriz")
        busqueda = input("Ingrese nif para imprimir su certificado: ")
        certificado(busqueda,matriz)
        
        

    elif op == 3:
        print("BUSCAR")
        if lista != []:
            busqueda = input("Ingrese nif a buscar: ")
            buscar_nif(busqueda,matriz)
            if buscar_nif(busqueda,matriz) == True:
                print("Nif encontrado")
                print()
            else:
                print("Nif NO ENCONTRADO")
        else:
            print("No se ha agregado ningun dato")







    elif op == 4:
        print("ADIOS")
    
    





