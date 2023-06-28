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
            return fila
    
    

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
        print("certificado")
        if lista != []:
            busqueda = input("Ingrese nif para imprimir su certificado: ")
            
            if buscar_nif(busqueda,matriz) == True:
                
                print(f"Nombre: {certificado(busqueda,matriz)[1]}")
                print(f"NIF: {certificado(busqueda,matriz)[0]}")
                print(f"Edad: {certificado(busqueda,matriz)[2]}")
                print(f"EU: {certificado(busqueda,matriz)[3]}")
                print(f"Estado conyugal: {certificado(busqueda,matriz)[0]}")
            else:
                print("Nif NO ENCONTRADO")
        else:
            print("No se ha agregado ningun dato")

        
        
        
        

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
    
    





