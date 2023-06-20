
tradicional = 12000
peperoni = 14000
carnes = 17000

diurno = False #20%
vespertino = False #15%
admin = False #5%

total_pagar = 0
descuento_final = 0

cantidad_tradi = 0
cantidad_pepe = 0
cantidad_carnes = 0

total_tradi = 0
total_pepe = 0
total_carnes = 0


# MENU
opcion = 0
while opcion != 4:
    try: 

        print("1.Menu")
        print("2.Pago")
        print("3.Anular pedido")
        print("4.Salir")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1: 
            print("MENU RAPID")
            print(f"1.Pizza tradicional ${tradicional}")
            print(f"2.Pizza peperoni ${peperoni}")
            print(f"3.Pizza All carnes ${carnes}")
            opcion_pizza = int(input("Seleccione tipo de pizza: "))
            if opcion_pizza == 1:
                print("Seleccionaste pizza tradicional")
                cantidad_pizza = int(input("Ingrese cantidad de pizzas: "))
                while cantidad_pizza <= 0:
                    print("Numero fuera de rango")
                    cantidad_pizza = int(input("Ingrese cantidad de pizzas: "))
                total_pagar += tradicional * cantidad_pizza
                total_tradi += tradicional * cantidad_pizza
                cantidad_tradi += cantidad_pizza

            elif opcion_pizza == 2:
                print("Seleccionaste pizza peperoni")
                cantidad_pizza = int(input("Ingrese cantidad de pizzas: "))
                while cantidad_pizza <= 0:
                    print("Numero fuera de rango")
                    cantidad_pizza = int(input("Ingrese cantidad de pizzas: "))
                total_pagar += peperoni * cantidad_pizza
                total_pepe += peperoni * cantidad_pizza
                cantidad_pepe += cantidad_pizza
            
            elif opcion_pizza == 3:
                print("Seleccionaste pizza All carnes")
                cantidad_pizza = int(input("Ingrese cantidad de pizzas: "))
                while cantidad_pizza <= 0:
                    print("Numero fuera de rango")
                    cantidad_pizza = int(input("Ingrese cantidad de pizzas: "))
                total_pagar += carnes * cantidad_pizza
                total_carnes += carnes * cantidad_pizza
                cantidad_carnes += cantidad_pizza
            
            else:
                print("No seleccionaste ninguna pizza caezon")

        elif opcion == 2:
            print("PAGO")

            print("1.diurno")
            print("2.vespertino")
            print("3.admin")
            descuento = int(input("Ingresa segun tu caso: "))
            if descuento == 1:
                descuento_final += total_pagar * 0.20
            elif descuento == 2:
                descuento_final += total_pagar * 0.15
            elif descuento == 3:
                descuento_final +=  total_pagar * 0.05

            print("Pizza duoc")
            print("----------------------------")
            print(f"{cantidad_tradi} pizza tradicional ${total_tradi}")
            print(f"{cantidad_pepe} pizza peperoni ${total_pepe}")
            print(f"{cantidad_carnes} pizza All carnes ${total_carnes}")
            print("----------------------------")
            print(f"Subtotal            ${total_pagar}")
            print(f"Descuento           ${descuento_final}")
            print("----------------------------")
            print(f"Total a pagar        ${total_pagar - descuento_final}")
            opcion = 4

        elif opcion == 3:
            print("ANULAR PEDIDO")

            total_pagar = 0

            cantidad_tradi = 0
            cantidad_pepe = 0
            cantidad_carnes = 0

            total_tradi = 0
            total_pepe = 0
            total_carnes = 0

        elif opcion == 4:
            print("SALIR")

        else:
            print("Debes ingresar una opcion valida")

    except:
        print("Debes ingresar un numero")  

        

    







