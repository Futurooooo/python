#MANEJO DE ARCHIVOS (with open)
#EJEMPLO
with open("nombre_archivo.txt", "modo") as archivo:
    # Operaciones con el archivo

#MODOS PRINCIALES DE APERTURA:

#"r" (Read / Leer): Abre el archivo solo para lectura.
# Si el archivo no existe, Python lanza un FileNotFoundError.
 try:
    with open("bitacora.txt", "r") as archivo:
        contenido = archivo.read()  # Lee todo el texto del archivo
        print("--- CONTENIDO DEL ARCHIVO ---")
        print(contenido)
 except FileNotFoundError:
    print("[!] El archivo 'bitacora.txt' aún no existe.")

#"w" (Write / Escribir): Crea un archivo nuevo. 
#¡Cuidado! Si el archivo ya existe, borra todo su contenido anterior y lo sobrescribe desde cero.
# Al abrirlo en modo "w", el texto previo se elimina al instante.
with open("diario.txt", "w") as archivo:
    pass  # 'pass' indica que no queremos escribir nada, dejándolo en 0 bytes.

print("El archivo 'diario.txt' ahora está completamente vacío.")

#"a" (Append / Añadir): Abre el archivo para agregar nueva información al final sin borrar lo que ya contenía. Si el archivo no existe, lo crea.
with open("bitacora.txt", "a") as archivo:
    archivo.write("Registro de prueba 1\n")  # Usa \n para dar salto de línea