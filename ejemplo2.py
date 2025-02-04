import random


num1 = random.randint(1, 100)
print(num1)

contador = 0
bandera = True

while bandera:
    contador = contador + 1
    num2 = int(input("Ingrese un numero para adivinar: "))
    if num1 == num2:
        print("Adivinaste el numero random! Felicidades!")
        bandera = False
    elif num1 > num2:
        print("Tu numero es menor al numero a adivinar")
    else:
        print("Tu numero es mayor al numero que tienes que adivinar")

print("Usted gano con: " + str(contador) + " puntos. recuerde que mientras menos puntos tenga, mayor es su puntaje")