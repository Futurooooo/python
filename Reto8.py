#Divisor y Módulo de Números "A Prueba de Errores"
def dividir_numeros(a,b):
    resultado = a/b
    return resultado

while True:
    try: 
           a = float(input("Digite el primer numero por favor"))
           b = float(input("Digite el segundo numero"))
           resultado = dividir_numeros(a,b)
           print(f"Resultado: {resultado}")
           break

    except ValueError:
     print(" [!] Error: Ingrese valores numéricos válidos.")
    except ZeroDivisionError:
     print(" [!] Error: No es posible dividir entre cero.")


