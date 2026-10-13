#POO Herencia Y SOBREESCRITURA
#HERENCIA: La herencia permite crear una clase hija que hereda automáticamente todos los atributos y métodos de una clase padre.
#Ejemplo real: La clase Vehiculo (padre) tiene atributos como marca y modelo. Las clases Auto y Motocicleta (hijas) heredan esos atributos básicos, pero cada una agrega sus características únicas (por ejemplo, num_puertas para el auto o cilindrada para la moto).
#FUNCION:Para inicializar los atributos de la clase padre dentro de la clase hija, utilizamos super().__init__()
# --- CLASE PADRE ---
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")


# --- CLASE HIJA (Hereda de Persona) ---
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        # super() invoca el constructor de la clase Persona
        super().__init__(nombre, edad)
        self.carrera = carrera  # Atributo exclusivo del estudiante

    # Sobrescritura de método: adaptamos presentarse() para el estudiante
    def presentarse(self):
        print(f"Hola, soy {self.nombre}, estudio {self.carrera} y tengo {self.edad} años.")