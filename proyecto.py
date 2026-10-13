class Libro:
    def __init__(self, titulo, autor, year):
        self.titulo = titulo
        self.autor = autor
        self.year = year

    def convertir_a_linea(self):
        return f"{self.titulo},{self.autor},{self.year}\n"

    def mostrar_info(self):
        print(f"📖 '{self.titulo}' - {self.autor} ({self.year})")


while True:
        print("---MENU---")
        print("1.Registrar libro: ")
        print("2.Ver catalogo completo")
        print("3.Vaciar biblioteca")
        print("4.Salir")
       

        opcion = input("Por favor escoja una opcion (1,2,3,4)")

        if opcion == "1":
            titulo = input("Digite el titulo de la obra: ")
            autor = input("Digite el nombre del autor")
            while True:
              try:
                  year = input("Digite el año de publicacion por favor")
                  break
              except: ValueError
              print("[!] ERROR, Ingrese un año valido por favor.")

              nuevo_libro = Libro(autor, titulo, year)
              with open("biblioteca.txt","a") as archivo:
                  archivo.write(nuevo_libro.convertir_a_linea())
                  print("Libro registrado con exito!")

        elif opcion == "2":
            try:
                with open ("biblioteca.txt", "r")as archivo:
                    print("\n CATALOGO DE LIBROS")
                    lineas = archivo.readlines()
                    if not lineas:
                        print("La biblioteca esta vacia")
                    else:
                        for linea in lineas:
                         datos =linea.strip().split(",")
                        if len(datos) == 3:
                            t, a, y = datos
                            libro_temp = Libro(t,a,y)
                            libro_temp = mostrar_info()
            except: FileNotFoundError
            print("[ERROR]EL ARCHIVO NO EXISTE")
        elif opcion == "3":
            with open ("biblioteca.txt", "w")as archivo:
                pass
            print("Se ha eliminado los registros de la biblioteca")
        elif opcion == "4":
            print ("Gracias por usar el sistema")
            break
        else:
            print("Error vuelva a digitar otra opcion")





         



    