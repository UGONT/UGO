import numpy as np

lista = []

# Funcion Validar edad
def validar_edad(edad):
    if edad in range(16,150):
        return True
    else:
        return False

# Funcion Validar nombre
def validar_nombre(nombre):
    if len(nombre) in range(1,15) and nombre.isalpha():
        return True
    else:
        return False
# Funcion Validar apellido
def validar_apellido(apellido):
    if len(apellido) in range(1,20) and apellido.isalpha():
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
def agregar_datos(lista,nif_completo,nombre_completo,edad,europea):
    lista.append(nif_completo)
    lista.append(nombre_completo)
    lista.append(edad)
    lista.append(europea)

# Funcion Buscar NIF
def buscar_nif(busqueda,matriz):
    for fila in matriz:
        if fila[0] == busqueda:
            return True
    return False

# Funcion Pertenece a EU
def pertenece(eu):
    if eu == 1:
        return True
    else:
        return False

# Funcion Imprimir certificado
def certificado(busqueda,matriz):
    for fila in matriz:
        if fila[0] == busqueda:
            datos = fila
            return datos

# Funcion Estado conyugal
def Estado(estado):
    if estado == 1:
        estado = "Casad@"
    elif estado == 2:
        estado = "Solter@"
    elif estado == 3:
        estado = "Viud@"
    else:
        estado = "No especificado"
    return estado         

#Funcion Fecha nacimiento
def fecha_nacimiento(dia,mes,anio):
    if dia in range(1,32): 
        if mes in range(1,13):
            if anio in range(1900,2024):
                fecha = str(dia)+"/"+str(mes)+"/"+str(anio)
                return fecha
            else:
               return False    
        else:
            return False       
    else:
        return False           
    
opcion = 0
while opcion != 4:
    try:
        print("1.Grabar")
        print("2.Buscar")
        print("3.Imprimir certificados")
        print("4.Salir")
        opcion = int(input('Ingrese una opcion:\n->'))
        print()
        if opcion == 1:
            print("---GRABAR---")
            edad = int(input("---Ingrese su edad---\n->")) # EDAD
            validar_edad(edad)

            if validar_edad(edad) == True:
                print("---Edad ingresada correctamente---")
                print()
                nombre = str(input("---Ingrese su nombre---\n->")) # NOMBRE
                apellido = str(input("---Ingrese su apellido---\n->"))

                if validar_nombre(nombre) == True and validar_apellido(apellido) == True:
                    print("---Nombre ingresado correctamente---")
                    print()
                    nif = input("---Ingrese los 8 digitos de su nif---\n->") # NIF
                    tres_dig = input("---Ingrese ultimos 3 dig/crtr de su nif---\n->") # DIGITOS NIF
                    if validar_nif(nif) == True and validar_nif_dig(tres_dig) == True:
                        
                        print("---NIF ingresado correctamente---")
                        print()
                        eu = int(input("Pertenece a la union europea?\n1.Si\n2.No\n->")) # PERTENECE A EU O NO
                        if pertenece(eu) == True:
                            europea = "Pertenece a EU"
                        else:
                            europea = "No pertenece a EU"
                        print("---Datos registrados correctamente---")
                        nif_completo = str(nif)+"-"+str(tres_dig.upper())
                        nombre_completo = nombre+" "+apellido
                        agregar_datos(lista,nif_completo,nombre_completo,edad,europea)
                        arreglo_1 = np.array(lista)
                        n_filas = int(len(arreglo_1)/4)
                        matriz = arreglo_1.reshape(n_filas,4)
                        
                    else:
                        print("---Nif incorrecto---\nSobre NIF:\n\t1.Solo se permiten numeros\n\t2.Tamaño de Nif debe ser solo 8 dig")
                        print("Sobre dig NIF:\n\t1.No se admiten simbolos\n\t2.Tamaño obligatorio 3 dig/crtr")
                        print()
                else:
                    print("---Nombre incorrecto---\nRecordar:\n\t1.Minimo 8 caracteres\n\t2.Solo se admiten caracteres del alfabeto")
                    print()
            else:
                print("---Debes ser mayor de 15 años---")
                print()

        elif opcion == 2:
            print("---BUSCAR---")
            if lista != []:
                busqueda = input("Ingrese nif a buscar:\n->")
                busqueda = busqueda.upper()

                if buscar_nif(busqueda,matriz) == True:
                    print("---NIF ENCONTRADO---")
                    print(f"Nombre: {certificado(busqueda,matriz)[1]}")
                    print(f"Edad: {certificado(busqueda,matriz)[2]}")
                    print(f"EU: {certificado(busqueda,matriz)[3]}")
                    print(f"NIF: {certificado(busqueda,matriz)[0]}")
                    print()
                else:
                    print("---NIF NO REGISTRADO---")
                    print()
            else:
                print("---No se ha agregado ningun dato---")
                print()
        elif opcion == 3:
            print("---IMPRIMIR CERTIFICADOS---")
            if lista != []:
                busqueda = input("---Ingrese nif para imprimir su respectivo certificado---\n->")
                busqueda = busqueda.upper()
                
                if buscar_nif(busqueda,matriz) == True:
                    print("Indica segun el caso:")
                    print("1.Casad@")
                    print("2.Solter@")
                    print("3.Viud@")
                    print("4.Otro")
                    estado = int(input("->"))
                    print("---Ingrese fecha de nacimiento---")
                    dia = int(input("Dia: "))
                    mes = int(input("Mes: "))
                    anio = int(input("Año: "))
                    if fecha_nacimiento(dia,mes,anio) == False:
                        print("---Fecha fuera de rangos---")
                    else:
                        print("----------------------------------")
                        print(f"CERTIFICADO DE {certificado(busqueda,matriz)[1]}")
                        print(f"NIF: {certificado(busqueda,matriz)[0]}")
                        print("----------------------------------")
                        print(f"Fecha Nacimiento: {fecha_nacimiento(dia,mes,anio)}")
                        print(f"Edad: {certificado(busqueda,matriz)[2]}")
                        print(f"EU: {certificado(busqueda,matriz)[3]}")
                        print(f"Estado conyugal: {Estado(estado)}")
                        print("----------------------------------")    

                else:
                    print("---NIF NO ENCONTRADO---")
            else:
                print("---No se ha agregado ningun dato---")
                print()

        elif opcion == 4:
            print("---SALIR---")
            print("Version 3.0.en.su.prime")
        else:
            print("---No seleccionaste ninguna opcion---")
    except:
        print("--ERROR--\nPosible causa de error:\n\t1.Ingreso de caracter en seleccion de opcion\n\t2.Ingreso erroneo dentro de algun dato")    
        print()

    







