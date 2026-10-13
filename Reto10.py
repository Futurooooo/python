class vehiculo:
    def __init__ (self, marca, modelo, nivel_gasolina):
        self.marca = marca
        self.modelo = modelo
        self.nivel_gasolina = float(nivel_gasolina)

    def mostrar_estado(self):
        print(f"vehiculo: {self.marca} | modelo: {self.modelo} | nivel_gasolina: {self.nivel_gasolina:.3f}")

    def conducir(self, kilometros):
        consumo = (kilometros * 0.5)
        print(f"El consumo de gasolina es {consumo}")
        if self.nivel_gasolina >= consumo:
           self.nivel_gasolina -= consumo
           print(f"Gasolina consumida durante el viaje {self.nivel_gasolina}")
        else:
            print("No hay suficiente gasolina para el viaje")

    def recargar_gasolina(self, cantidad):
        self.nivel_gasolina += cantidad
        print(f"El nivel de gasolina es: {cantidad}")


mi_auto = vehiculo("Toyota", "Corolla", 20.0)

#Estado inicial
mi_auto.mostrar_estado()
#Conducion auto 50 km (requiere 25 L, pero solo hay 20 L)
mi_auto.conducir(50)
#Recarga de gasolina de 30 litros
mi_auto.recargar_gasolina(30.2)
# 5. Volvemos a intentar conducir 50 km
mi_auto.conducir(50)
# 6. Estado final
mi_auto.mostrar_estado()
        