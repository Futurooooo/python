def calcular_area_cuadrado(lado):
    area = lado * lado
    return area

def calcular_area_circulo(radio):
    area = 3.1416 * (radio ** 2)
    return area

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False
    
while True:
    print("\n---MENU---")
    print("1.Calcular el area de un cuadrado")
    print("2.Calcular el area de un circulo")
    print("3.Verificar si una persona es mayor de edad")
    print("4.Salir")

    opcion = input("¿Qué opción desea realizar? (1, 2, 3, 4): ")

    if opcion =="1":
       lado = float(input("Ingrese la medida del lado del cuadrado: "))
       resultado = calcular_area_cuadrado(lado)
       print(f"El área del cuadrado es: {resultado}")  

    elif opcion == "2":
         radio = float(input("Ingrese el radio del circulo"))
         resultado = calcular_area_circulo(radio)
         print(f"El área del círculo es: {resultado}")
    elif opcion == "3":
         edad = int(input("Ingrese la edad de la persona: "))
         if es_mayor_de_edad(edad):
          print("La persona es mayor de edad")
         else:
          print("La persona es menor de edad")
    elif opcion == "4":
         print("Gracias por usar el sistema")
         break
    else:
          print("La opcion no esta disponible vuelva a intentarlo")

