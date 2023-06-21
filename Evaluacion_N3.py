import numpy as np

lista = []
union = False


def buscar(busqueda):
    print()

def certificado():
    print()


#MENU
opcion = 0
while opcion != 4:
    try:
        print("1.Grabar")
        print("2.Buscar")
        print("3.Imprimir certificados")
        print("4.Salir")
        opcion = int(input("Seleccione una opcion: "))
        print()
        if opcion == 1:
            print("GRABAR DATOS")
            
            edad = int(input("Ingrese su edad: "))
            if edad < 15:
                print("Debes ser mayor de 15 años")
            else:
                nif = input("Ingrese los 8 numeros de su nif: ")
                n = int(nif)
                if len(nif) != 8:
                    print("Fuera de rango")
                else:
                    letrasnif = str(input("Ingrese 3 letras de su nif: "))

                    if len(letrasnif) != 3:
                        print("Nif no valido")
                    else:
                        
                        nombre = input("Ingrese su nombre: ")
                        
                        if len(nombre) < 8:
                            print("Nombre no valido (min 8 caracteres)")
                        else:
                            pertenece = int(input("Pertenece a la Union Europea?\n1.Si\n2.No\n->"))
                            if pertenece == 1:
                                union = True
                                letrasM = letrasnif.upper()
                                lista.append(str(nif)+"-"+(letrasM))                        
                                lista.append(nombre)
                                lista.append(edad)
                                arreglo_lista1 = np.array(lista)
                                print(arreglo_lista1)

                            elif pertenece == 2:

                                letrasM = letrasnif.upper()
                                lista.append(str(nif)+"-"+(letrasM))                        
                                lista.append(("Nombre: ")+ nombre)
                                lista.append(("Edad: ")+str(edad))
                                arreglo_lista1 = np.array(lista)
                                print(arreglo_lista1)
                            else:
                                print("No seleccionaste ninguna opcion")
                    
        elif opcion == 2:
            print("BUSCAR")
            busqueda = input("Ingrese NIF completo y con guion: ")
            if arreglo_lista1[0] == busqueda:
                print("NIF ENCONTRADO")
                for i in arreglo_lista1:
                    print(i,end=" ")
                print()
                if union == True:
                    print("Pertenece a la Union Europea")
                else:
                    print("No pertenece a la Union Europea")
            else:
                
                print("NIF no encontrado")

        elif opcion == 3:
            print("IMPRIMIR CERTIFICADOS")
            estado = input("ingrese su estado conyugal: ")
            print("-----------------------------")
            print(f"NIF: {arreglo_lista1[0]}")
            print(f"Nombre: {arreglo_lista1[1]}")
            print(f"Edad: {arreglo_lista1[2]}")
            print(f"Estado: {estado}")
            if union == True:
                print("Si pertenece a la Union Europea")
            else:
                print("No pertenece a la Union Europea")
            print("-----------------------------")

        elif opcion == 4:
            
            if lista == []:
                print("Adios")
            else:
                print(f"Adios Don {arreglo_lista1[1]}")

        else:
            print("No ingreso ninguna opcion valida")    
    except:
        print("ERROR")





