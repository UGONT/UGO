import numpy as np

lista = []
num1 = int(input("Ingrese un numero entre 3 y 6: "))
num2 = int(input("Ingrese un segundo numero entre 3 y 6: "))

while num1 < 3 or num2 > 6:
    print("Debes ingresar 2 numeros entre 3 y 6")
    num1 = int(input(""))
    num2 = int(input(""))

arreglo1 = np.zeros(lista)
print(arreglo1)

