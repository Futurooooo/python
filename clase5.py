#Lista es una secuencia ordenada de elementos.
# En Python se definen encerrando los valores entre corchetes [] separados por comas.
materias = ["Álgebra", "Métodos Numéricos", "Redes", "Bases de Datos"]
print(materias)

#Acceso por indice
materias = ["Álgebra", "Métodos Numéricos", "Redes"]
# Índices:      0              1               2

print(materias[0])  # Salida: Álgebra
print(materias[2])  # Salida: Redes

# Índices negativos: cuentan desde el final hacia atrás
print(materias[-1]) # Salida: Redes (último elemento)

#Modificar elementos
materias[1] = "Física"
print(materias)  # ['Álgebra', 'Física', 'Redes']

#Métodos principales para manipular listas
alumnos = ["Ana", "Carlos"]

# 1. append(valor): Agrega un elemento al FINAL de la lista
alumnos.append("Irving")

# 2. insert(posicion, valor): Agrega un elemento en una posición ESPECÍFICA
alumnos.insert(1, "Beatriz")

# 3. remove(valor): Elimina la primera ocurrencia de un valor
alumnos.remove("Carlos")

# 4. len(lista): Devuelve la cantidad TOTAL de elementos
print(f"Hay {len(alumnos)} alumnos en la lista.")

# 5. Recorrer una lista con un bucle for
for alumno in alumnos:
    print(f"Estudiante: {alumno}")

#TUPLAS
# Una tupla es casi idéntica a una lista, pero con una diferencia crítica:
# es inmutable. Una vez creada, no puedes agregar, eliminar ni modificar sus elementos.
# Se definen encerrando los valores entre paréntesis ().
# Datos que NO deben cambiar en el tiempo
coordenadas_ipn = (19.5042, -99.1469)
dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")

print(coordenadas_ipn[0])  # Acceso igual que en listas (19.5042)

# Esto causará un ERROR si intentas ejecutarlo:
# dias_semana[0] = "Domingo"  <-- TypeError: 'tuple' object does not support item assignment