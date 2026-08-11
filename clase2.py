#operadores matematicos
usuario = input ("Ingresa tu nombre de usuario: ")
print("Bienvenido al sistema usuario", usuario)
#Conversion de tipos de datos (Type casting)
#Se pone antes de input int() convierte a entero.
#float() convierte a decimal.
# str() convierte cualquier dato a texto.

numero1 = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa otro numero: "))

suma =  numero1 + numero2
print("Resultado!",suma)

#Cadenas F-Strings
nombre = "Irving"
edad = 24

# En lugar de: print("Me llamo", nombre, "y tengo", edad, "años.")
print(f"Me llamo {nombre} y tengo {edad} años.")
