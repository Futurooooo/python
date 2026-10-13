class Mascota:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def convertir_a_linea(self):
        return f"{self.nombre},{self.especie}\n"

    def mostrar_info(self):
        print(f"🐾 Nombre: {self.nombre} | Especie: {self.especie}")

while True:
    print("---MENU---")
    print("1.Registrar mascotas: ")
    print("2.Ver mascotas")
    print("3.Salir")

    opcion = input("Por favor escoja una opcion: (1,2,3)")

    if opcion == "1":
        nombre = input("Escriba el nombre de su mascota por favor: ")
        especie = input("Escriba la especie de su mascota por favor: ")
        nueva_mascota = Mascota (nombre, especie)
        with open ("mascotas.txt","a") as archivo:
            archivo.write(nueva_mascota.convertir_a_linea())
    elif opcion == "2":
        try:
            with open ("mascotas.txt", "r") as archivo:
                print("---INVENTARIO DE MASCOTAS---")
                lineas = archivo.readlines()
                if not lineas:
                    print("El inventario esta vacio")
                else:
                    for linea in lineas:
                        datos = linea.strip().split(",")
                    if len(datos) == 2:
                       n,e = datos
                       mascotas_temp = Mascota(n,e)
                       mascotas_temp = mostrar_info()
        except FileNotFoundError:
            print("[ERRROR!!!!!] Archivo no encontrado")
    elif opcion == "3":
        print("Gracias por usar el sistema de inventario")
        break
    else:
        print("ERROR, Opciones no disponibles, vuelva a intentarlo")


