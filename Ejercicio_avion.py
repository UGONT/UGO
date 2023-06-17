import numpy as np

lista_A = []
lista_B = []
asiento_normal = 78900
asiento_vip = 240000
N = range(1,31)
V = range(31,43)
Duoc = False

def datos_usuario():
    nombre = input("Nombre pasajero: ")
    rut = input("Rut pasajero: ")
    telefono = input("Telefono pasajero: ")
    banco = input("Banco pasajero: ")
    return nombre,rut,telefono,banco


#Agrega 30 asientos en lista A Nor
for i in range(1,31):
    lista_A.append(i)

#Agrega 12 asientos en lista B VIP
for i in range(31,43):
    lista_B.append(i)

selec_asiento = int(input("Seleccione un asiento\n->"))
#Bloquear asiento
while selec_asiento not in N and V:
    print("Asiento fuera de rango\n->")
    selec_asiento = int(input())
    
if selec_asiento in N:
    lista_A[selec_asiento - 1] = "X"
elif selec_asiento in V:
    lista_B[selec_asiento - 31] = "X"

 #arreglo lista A creacion matriz
arreglo_A = np.array(lista_A)
matriz_nor = arreglo_A.reshape(5,6)
  
#arreglo lista B creacion matriz
arreglo_B = np.array(lista_B)
matriz_vip = arreglo_B.reshape(2,6)

#dibujo avion
for fila in matriz_nor:#Asientos normales
    print(end="| ")
    for columna in fila:     
        print(columna, end="\t")
    print()

print("|-----------------     -------------------|")

for fila in matriz_vip:#Asientos VIP
    print(end="| ")
    for columna in fila:
        print(columna, end="\t")
    print()



#  MENU
opcion = 0

while opcion != 5:
    try:
        print("1.Ver asientos disponibles")
        print("2.Comprar asientos")
        print("3.Anular voleto")
        print("4.Modificar datos de pasajero")
        print("5.Salir")
        opcion = int(input("Seleccione una opcion\n->"))
        if opcion == 1:
            print()



        elif opcion == 2:
            print()



        elif opcion == 3:
            print()



        elif opcion == 4:
            print()



        elif opcion == 5:
            print()
    except:
        print("Error")




