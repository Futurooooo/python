#DRY (Don't Repeat Yourself / No te repitas).
# 1. DEFINIR la función (instrucciones guardadas)
def saludar():
    print("¡Hola! Bienvenido al sistema.")

# 2. LLAMAR a la función (ejecutarla)
saludar()
saludar()  # La puedes llamar las veces que quieras

#Parámetros y Argumentos
#Las funciones pueden recibir datos desde afuera para trabajar con ellos.

def saludar_estudiante(nombre, carrera):
    print(f"Hola {nombre}, bienvenido a la carrera de {carrera}.")

# Pasamos los valores (argumentos) al llamarla:
saludar_estudiante("Irving", "Informática")
saludar_estudiante("Ana", "Industrial")

#Retornar valores con return
def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area  # Devuelve el resultado hacia afuera

# Guardamos lo que devuelve la función en una variable
resultado = calcular_area_triangulo(10, 5)
print(f"El área del triángulo es: {resultado}")