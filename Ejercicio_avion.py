import numpy as np

lista_A = []
lista_B = []
lista_C = []

asiento_normal = 78900
asiento_vip = 240000

#Agrega 30 asientos en lista A Nor
for i in range(1,31):
    lista_A.append(str(i))

#Agrega 12 asientos en lista B VIP
for i in range(31,43):
    lista_B.append(str(i))

#arreglo listas
arreglo_A = np.array(lista_A)
arreglo_B = np.array(lista_B)

#creacion matrizes
matriz_nor = arreglo_A.reshape(5,6)
matriz_vip = arreglo_B.reshape(2,6)

#dibujo avion
for fila in matriz_nor:#print(matriz_nor)
    print(end="| ")

    for columna in fila:     
        print(columna, end="\t")
    print()

print("|-----------------     -------------------|")

for fila in matriz_vip:#print(matriz_vip)
    print(end="| ")
    for columna in fila:
        print(columna, end="\t")
    print()

selec_asiento = int(input("Seleccione un asiento\n->"))
for asiento in range(5*6):
    if asiento == selec_asiento:
        lista_A[asiento]= selec_asiento    

print(lista_A[selec_asiento])


