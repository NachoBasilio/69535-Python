saldo = 1000
pin = "3731"
bandera = True


while bandera:
    print("Bienvendio al cajero de 'Perrito con Chaucha'")
    codigo = input("Manda tu pin, kpo")

    if codigo == pin:
        print("Hola amiguito ¿Que queres hacer hoy?")
        opciones = int(input("Usted puede: \n1- Retirar dinero \n2- Ingresar dinero \n3- Enviar dinero \n 4-Ver saldo \n\n"))
        if opciones == 1:

            dinero_a_retirar = int(input(f"¿Cuanto dinero quiere retirar? su saldo es {saldo}\n\n"))
            if dinero_a_retirar > saldo:
                print("¡Usted no puede sacar mas dinero del que posee!")
            else:
                saldo = saldo - dinero_a_retirar
                print(f"¡Perfecto! su saldo ahora es de {saldo}")

            respuesta = input("¿Quiere salir en el cajero? Ponga 'Si': \n\n")
            if respuesta == "Si":
                bandera = False

        elif opciones == 2:

            dinero_a_ingresar = int(input(f"¿Cuanto dinero quiere ingresar? su saldo es {saldo}\n\n"))
            if dinero_a_ingresar < 0:
                print("¿Vos queres ingresar dinero negativo, flaco?")
            else:
                saldo = saldo + dinero_a_ingresar
                print(f"Su saldo actual es de: {saldo}")

            respuesta = input("¿Quiere salir en el cajero? Ponga 'Si': \n\n")
            if respuesta == "Si":
                bandera = False
        elif opciones == 3:

            cbu_a_enviar = int(input(f"¿A quien le quiere mandar dinero? ponga el CBU de esa persona. \nSu saldo es {saldo}\n\n"))
            dinero_a_enviar = int(input(f"¿Cuanto dinero quiere enviar?\n\n"))
            if dinero_a_enviar < 0:
                print("¿Vos queres enviar dinero negativo, flaco?")
            elif dinero_a_enviar > saldo:
                print("¡Usted no puede enviar mas dinero del que posee!")
            else:
                saldo = saldo - dinero_a_enviar
                print(f"El dinero fue enviado, su saldo ahora {saldo}")

            respuesta = input("¿Quiere salir en el cajero? Ponga 'Si': \n\n")
            if respuesta == "Si":
                bandera = False

        elif opciones == 4:

            print(f"Este es tu saldo: {saldo}")
            respuesta = input("¿Quiere salir en el cajero? Ponga 'Si': \n\n")
            if respuesta == "Si":
                bandera = False
        else:
            print("Te dije que se iba a romper, era mentira pero bien que haces lo que se te cante no?")
            respuesta = input("¿Quiere salir en el cajero? Ponga 'Si': \n\n")
            if respuesta == "Si":
                bandera = False
    else:
        print("Tu pin esta mal")


