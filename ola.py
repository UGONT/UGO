s = True
while s == True:
    
    try:

        numero = input("Ingrese un numero: ")
        lista = []
        for i in numero:
            lista.append(i)
        num = int(lista[2]+lista[1]+lista[0])
        print(num)
        s = False

    except:
        print("Ingresar un NUMERO de 3 DIGITOS")