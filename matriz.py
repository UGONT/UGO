import numpy as np

lista = []

# Funcion Validar edad
def validar_edad(edad):
    if edad > 15:
        return True
    else:
        return False

# Funcion Validar nombre
def validar_nombre(nombre):
    if len(nombre) >= 8 and nombre.isalpha():
        return True
    else:
        return False

# Funcion Validar NIF    
def validar_nif(nif):     
    if len(nif) == 8 and nif.isdigit():
        return True
    else:
        return False  

# Funcion Validar digitos de NIF
def validar_nif_dig(tres_dig):
    if len(tres_dig) == 3 and tres_dig.isalnum():
        return True
    else:
        return False    

# Funcion Agregar datos en la lista
def agregar_datos(lista,nif_completo,nombre,edad):
    lista.append(nif_completo)
    lista.append(nombre)
    lista.append(edad)

# Funcion Buscar NIF
def buscar_nif(busqueda,matriz):
    for fila in matriz:
        if fila[0] == busqueda:
            return True
    return False
    


opcion = 0
while opcion != 4:
    try:
        print("1.Grabar")
        print("2.Buscar")
        print("3.Imprimir certificados")
        print("4.Salir")
        opcion = int(input('Ingrese una opcion: '))
        print()
        if opcion == 1:
            print("GRABAR")
            edad = int(input("Ingrese su edad: ")) # EDAD
            validar_edad(edad)
            if validar_edad(edad) == True:
                print("Edad correcta")
                nombre = str(input("Ingrese su nombre (Minimo 8 caracteres): ")) # NOMBRE
                validar_nombre(nombre)
                if validar_nombre(nombre) == True:
                    print("Nombre correcto")
                    nif = input("Ingrese los 8 digitos de su nif: ") # NIF
                    validar_nif(nif)
                    if validar_nif(nif) == True:
                        print("Nif correcto")
                        tres_dig = input("Ingrese ultimos 3 dig/crtr de su nif: ") # DIGITOS NIF
                        validar_nif_dig(tres_dig)
                        if validar_nif_dig(tres_dig) == True:
                            print("NIF ingresado correctamente")
                            nif_completo = str(nif)+"-"+str(tres_dig.upper())
                            agregar_datos(lista,nif_completo,nombre,edad)
                            arreglo_1 = np.array(lista)
                            n_filas = int(len(arreglo_1)/3)
                            matriz = arreglo_1.reshape(n_filas,3)





                        else:
                            print("Nif incorrecto\nRecordar;\n\t1.No se admiten simbolos\n\t2.Tamaño obligatorio 3 dig/crtr")
                    else:
                        print("Nif incorrecto\nRecordar;\n\t1.Solo se permiten numeros\n\t2.Tamaño de Nif debe ser solo 8 dig")
                else:
                    print("Nombre incorrecto\nRecordad;\n\t1.Minimo 8 caracteres\n\t2.Solo se admiten caracteres del alfabeto")
            else:
                print("Debes ser mayor de 15 años")

        elif opcion == 2:
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

        elif opcion == 3:
            print("IMPRIMIR")
        elif opcion == 4:
            print("SALIR")
    except:
        print("--ERROR--\nPosible causa de error:\n\t1.Ingreso de caracter en seleccion de opcion")    
        print()

    







