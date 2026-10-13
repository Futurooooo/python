#---CLASE PADRE---
class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_pago(self):
        return self.salario_base

    def mostrar_info(self):
        pago_final = self.calcular_pago()
        print(f"nombre: {self.nombre} | salario:{self.salario_base} ")

#--CLASE HIJA--
class Gerente(Empleado):
    def __init__(self, nombre, salario_base, bono_gerencial):
        super().__init__(nombre, salario_base)
        self.bono_gerencial = bono_gerencial

    def calcular_pago(self):
        return self.salario_base + self.bono_gerencial

class Desarrollador(Empleado):
    def __init__(self, nombre, salario_base, lenguaje_principal):
        super().__init__(nombre, salario_base)
        self.lenguaje_principal = lenguaje_principal

    def programar(self):
        f"{self.nombre} está codificando en {self.lenguaje_principal}."

Ana = Gerente(nombre="Ana", salario_base=20000, bono_gerencial=5000)
Irving = Desarrollador(nombre="Irving", salario_base=15000, lenguaje_principal="Python")

#OBJETOS
Ana.mostrar_info ()
Irving.programar()
Irving.mostrar_info()
        


        
