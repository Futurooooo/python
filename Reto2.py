#Una Calculadora de Promedio de Estudiante.
usuario = input("Por favor ingrese su nombre de usuario: ")

calificacion1 = float(input("Ingrese su calificacion de Algebra:"))
calificacion2 = float(input("Ingrese su calificacion de Ingenieria de pruebas"))
calificacion3 = float(input("Ingrese su calificacion de Metodos Numericos"))

suma = calificacion1 + calificacion2 +calificacion3
promedio = round(suma/3,2)

usuario_edad = int(input("Ingrese por favor su edad"))

edad_final = 30-usuario_edad
print(f"Hola {usuario}, tu promedio final es de tres materias es: {promedio}.Te faltan {edad_final} para cumplir 30 ")