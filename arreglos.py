import numpy as np


lista = [1, 2, 3, 4, 5]
arreglo = np.array(lista)
print(arreglo)

#ndim indica cuantas dimenciones posee el arreglo 
print(f"El arreglo es de {arreglo.ndim} dimencion")

#len indica el largo de arreglo
print(f"El arreglo es de largo {len(arreglo)}")

#slice
# Star:Stop:Step = indica cuanto quiero mostrar del arreglo
# Star Indica desde donde vamos a consultar
# Stop Indica hasta donde va consultar
# Step Indica de cuanto en cuanto va a contar

print(arreglo[::])

#Rellenar arreglos
# for 
lista2 = [i for i in range(1,11)]
arreglo2 = np.array(lista2)
print(arreglo2)

#arange(Star:Stop:Step) = rellena el arreglo con valores segun lo indicado
arreglo3 = np.arange(1,11)
print(arreglo3)

#operaciones
# sumar

arreglo3 += 5
print(arreglo3)

arreglo3 *= 10
print(arreglo3)

#comparaciones o operadores relacionales
print(arreglo3>arreglo2)

##sum() = Entrega la suma de los valores del arreglo
print(arreglo3.sum())

#Mean() = Entrega el promedio de valores del arreglo
print(arreglo3.mean())

#Max = Muestra el valor mas alto 
#Min = Muestra el valor mas bajo
print(f"Numero mas alto {arreglo3.max()}")
print(f"Numero mas bajo {arreglo3.min()}")
