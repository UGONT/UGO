import numpy as np

datos = []
base_datos = np.array(datos)




lista = []

rut = input("Ingresa tu rut: ")
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

lista.append(rut)
lista.append(nombre)
lista.append(edad)
arreglo_lista = np.array(lista)

base_datos = np.concatenate((base_datos,arreglo_lista))

lista = []

rut = input("Ingresa tu rut: ")
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

lista.append(rut)
lista.append(nombre)
lista.append(edad)
arreglo_lista = np.array(lista)

base_datos = np.concatenate((base_datos,arreglo_lista))
n = len(base_datos)
matriz = base_datos.reshape(int(n/3),3)


print(matriz)