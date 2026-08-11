#Dicionarios
#Un dicionario almacena pares de Clave: Valor (Key: Value).
# Ficha de un estudiante
alumno = {
    "nombre": "Irving",
    "edad": 24,
    "carrera": "Informática",
    "promedio": 8.5
}

# 1. Acceder a un valor mediante su clave
print(alumno["nombre"])    # Salida: Irving
print(alumno["promedio"])  # Salida: 8.5

# 2. Modificar un valor existente
alumno["promedio"] = 9.0

# 3. Agregar una nueva clave con su valor
alumno["semestre"] = 6

# 4. Eliminar una clave
del alumno["edad"]

print(alumno)

#Métodos útiles en diccionarios:
#alumno.keys() -> Devuelve la lista de solo las claves (nombre, carrera, etc.).
#alumno.values() -> Devuelve la lista de solo los valores (Irving, Informática, etc.).
#alumno.items() -> Devuelve pares (clave, valor) para recorrerlos con un for:

#for clave, valor in alumno.items():
#   print(f"{clave.capitalize()}: {valor}")

#CONJUNTOS
#Un conjunto es una colección de elementos que NO permite duplicados 
#y cuyos elementos no tienen un orden fijo.
# Definición de un conjunto
alumnos_inscritos = {"Irving", "Ana", "Carlos", "Irving", "Ana"}

# ¡Automáticamente elimina los duplicados!
print(alumnos_inscritos)  # Salida: {'Irving', 'Ana', 'Carlos'}

# Agregar y eliminar
alumnos_inscritos.add("Beatriz")
alumnos_inscritos.remove("Carlos")

# Comprobar si existe un elemento de forma ultrarrápida
if "Irving" in alumnos_inscritos:
    print("Irving está registrado.")

#Caso de uso clásico: Eliminar duplicados de una lista
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 4, 5]
lista_limpia = list(set(lista_con_duplicados))
print(lista_limpia)  # [1, 2, 3, 4, 5]
