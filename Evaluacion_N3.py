def validar_nombre(nombre):
    if len(nombre) >= 8 and nombre.isalpha():
        return True
    else:
        return False

nombre = input("---Ingrese su nombre (Minimo 8 caracteres y todo junto)---\n->")
if validar_nombre(nombre) == True:
    print("---Nombre ingresado correctamente---")
    print()
else:
    print("Mal")


