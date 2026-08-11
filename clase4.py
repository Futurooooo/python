intentos = 1

while intentos <= 3:
    print(f"Intento número: {intentos}")
    intentos = intentos + 1  # También se puede escribir: intentos += 1

print("Fin del bucle.")

# range(5) genera una secuencia del 0 al 4 (5 números en total)
for i in range(5):
    print(f"Número de iteración: {i}")

#Si quieres definir inicio y fin, usas range(inicio, fin) (el número final nunca se incluye):
    # Imprime del 1 al 5
for numero in range(1, 6):
    print(f"Contando: {numero}")

#Control de bucles: break y continue
for num in range(1, 10):
    if num == 5:
        print("Encontré el 5, me salgo del bucle.")
        break  # Se rompe el bucle
    print(f"Número: {num}")

#Bucle white true
while True:
    respuesta = input("¿Quieres salir del programa? (si/no): ")
    
    if respuesta == "si":
        print("¡Saliendo del programa!")
        break  # <--- Aquí rompes el bucle infinito y el programa termina
    else:
        print("Continuamos dentro del bucle...\n")
    