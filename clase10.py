class Producto:
    # Constructor: inicializa los atributos cuando creas un objeto
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # Método: una acción que realiza el producto
    def mostrar_info(self):
        print(f"Producto: {self.nombre} | Precio: ${self.precio:.2f}")

    # Método para aplicar un descuento
    def aplicar_descuento(self, porcentaje):
        monto_descuento = (self.precio * porcentaje) / 100
        self.precio -= monto_descuento
        print(f"--> ¡Descuento de {porcentaje}% aplicado a {self.nombre}!")


# --- CREACIÓN Y USO DE OBJETOS ---

# Creamos 2 objetos independientes usando el mismo molde
lapto = Producto("Laptop Gamer", 15000.0)
mouse = Producto("Mouse Inalámbrico", 350.0)

# Llamamos a sus métodos
lapto.mostrar_info()
lapto.aplicar_descuento(10)
lapto.mostrar_info()  # Muestra el precio con el descuento ya aplicado