# Vamos a hacer una tienda con todo lo que aprendimos hoy

total = 0
bandera = True

while bandera:
    opcion = int(input("Bienvenidos a la tienda 'Perrito con Chaucha', usted puede comprar los siguientes productos:\n 1- Palito bombo\n 2- Palito de agua\n 3- Palito viral\n 4- 1/4 de helado. \nSi pone otro numero, la tienda se va a cerrar.\n"))

    if opcion == 1:
        total = total + 500
        respuesta = input("¿Quiere salir del bucle? Ponga 'Si': ")
        if respuesta == "Si":
            bandera = False
    elif opcion == 2:
        total = total + 200
        respuesta = input("¿Quiere salir del bucle? Ponga 'Si': ")
        if respuesta == "Si":
            bandera = False
    elif opcion == 3:
        total = total + 5000
        respuesta = input("¿Quiere salir del bucle? Ponga 'Si': ")
        if respuesta == "Si":
            bandera = False
    elif opcion == 4:
        total = total + 2500
        respuesta = input("¿Quiere salir del bucle? Ponga 'Si': ")
        if respuesta == "Si":
            bandera = False
    else:
        print("Te dije que se iba a romper, era mentira pero bien que haces lo que se te cante no?")
        respuesta = input("¿Quiere salir del bucle? Ponga 'Si': ")
        if respuesta == "Si":
            bandera = False

print(f"El sub total de su compra es: {total}")

bandera = True
chismoso = False

if total == 0:
    print("Usted no compro nada...")
else:
    while bandera:
        opcion = int(input("Usted puede pagar con:\n 1- Efectivo\n 2- Tarjeta débito\n 3- Tarjeta crédito\n 4- Cripto\n"))

        if opcion == 1:

            print(f"Con efectivo usted tiene un 10% de descuento")

            respuesta = input("¿Quiere comprar con este medio de pago? Ponga 'Si': ")
            if respuesta == "Si":
                total = total * 0.9
                chismoso = True
                bandera = False
            else:
                respuesta = input("¿Quiere seguir eligiendo metodos de pago? Ponga 'Si': ")
                if respuesta != "Si":
                    bandera = False
        elif opcion == 2:

            print(f"Con debito usted tiene un recargo de 10%")

            respuesta = input("¿Quiere comprar con este medio de pago? Ponga 'Si': ")
            if respuesta == "Si":
                total = total * 1.1
                chismoso = True
                bandera = False
            else:
                respuesta = input("¿Quiere seguir eligiendo metodos de pago? Ponga 'Si': ")
                if respuesta != "Si":
                    bandera = False
        elif opcion == 3:

            print(f"Con credito usted tiene un recargo de 30%")

            respuesta = input("¿Quiere comprar con este medio de pago? Ponga 'Si': ")
            if respuesta == "Si":
                total = total * 1.3
                chismoso = True
                bandera = False
            else:
                respuesta = input("¿Quiere seguir eligiendo metodos de pago? Ponga 'Si': ")
                if respuesta != "Si":
                    bandera = False
        elif opcion == 4:

            print(f"Con crito usted tiene... nada")

            respuesta = input("¿Quiere comprar con este medio de pago? Ponga 'Si': ")
            if respuesta == "Si":
                chismoso = True
                bandera = False
            else:
                respuesta = input("¿Quiere seguir eligiendo metodos de pago? Ponga 'Si': ")
                if respuesta != "Si":
                    bandera = False

        else:
            print("Te dije que se iba a romper, era mentira pero bien que haces lo que se te cante no?")
            respuesta = input("¿Quiere seguir eligiendo metodos de pago? Ponga 'Si': ")
            if respuesta != "Si":
                bandera = False


if chismoso:
    print(f"Gracias por su compra, su total fue de: {total}")
else:
    print("Adios...")