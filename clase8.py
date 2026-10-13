#MANEJO DE ERRORES Y EXCEPCIONES}
#ESTRUCTURA
#try (intentar): Pones el código "peligroso" que podría fallar.
#except (excepción): Pones el código que se ejecutará solo si ocurre un error,
# evitando que el programa truene.

try:
    edad = int(input("Ingresa tu edad: "))
    print(f"Tienes {edad} años.")
except ValueError:
    print(" [!] Error: Debes ingresar un número entero válido, no texto.")
    
#USO DE EXCEPT
try:
    num1 = float(input("Número 1: "))
    num2 = float(input("Número 2: "))
    
    resultado = num1 / num2
    print(f"Resultado: {resultado}")

except ValueError:
    print(" [!] Error: Ingrese valores numéricos válidos.")

except ZeroDivisionError:
    print(" [!] Error: No es posible dividir entre cero.")

#try / except en bucles while: Validación Robusta
while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        break  # Si la conversión a int() funcionó, rompemos el bucle
    except ValueError:
        print("Entrada no válida. Inténtalo de nuevo con un número.")

print(f"Edad guardada con éxito: {edad}")