import random


# num = int(input("Ingrese un numero: "))

# while num != 99:
#     if num == 0:
#         print("Es es cero")
#     elif num % 2 == 0:
#         print("Este numero es par")
#     else:
#         print("Este numero es impar")
#     num = int(input("Ingrese un numero:  (Si es 99 el bucle se cerrar)"))

num1 = random.randint(1, 10)
ganador = False
contador = 0
print(num1)

for i in range(3):
    contador = contador + 1
    num2 = int(input("Ingrese un numero para adivinar: "))
    if num1 == num2:
        print("Adivinaste el numero random! Felicidades!")
        ganador = True
        break
    elif num1 > num2:
        print("Tu numero es menor al numero a adivinar")
    else:
        print("Tu numero es mayor al numero que tienes que adivinar")

if ganador:
    print("Ganaste y usaste " + str(contador) + " esta cantidad de vidas.")
else:
    print("Perdiste, mas suerte la proxima.")
