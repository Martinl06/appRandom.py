import random

numero_secreto = random.randint(1,50)
print({numero_secreto})

numero = 0
acumulador = 0
adivino = False

while numero != numero_secreto and acumulador < 5:
    numero = int(input("Ingrese un numero entre el 1 y el 50: "))
    acumulador += 1
    if numero == numero_secreto:
        adivino = True
        print("Ganaste")
    else:
        if numero > numero_secreto:
            print("El numero ingresado es mayor al numero secreto, volve a intentarlo")
        elif numero < numero_secreto:
            print("El numero ingresado es menor al numero secreto, volve a intentarlo")    

if not adivino:
    print(f"Perdiste, el numero era {numero_secreto}")
     


