class ErrorInventario(Exception):
    pass

class ProductoNoEncontrado(ErrorInventario):
    pass

class CantidadInvalida(ErrorInventario):
    pass

class StockInsuficiente(ErrorInventario):
    pass

class Producto:
    def __init__(self, codigo, stock):
        self.codigo = codigo
        self.stock = stock

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise CantidadInvalida("La cantidad a retirar debe ser mayor que cero.")
        if cantidad > self.stock:
            raise StockInsuficiente("No hay suficiente stock para retirar la cantidad solicitada.")
        self.stock -= cantidad


class Inventario:
    def __init__(self):
        self.productos = {
            "sarten": Producto("sarten", 5),
            "salchichas": Producto("salchichas", 10),
            "pan": Producto("pan", 30)
        }
    def retirar_producto(self, codigo, cantidad):
        if codigo not in self.productos:
            raise ProductoNoEncontrado(f"El producto con código '{codigo}' no se encuentra en el inventario.")
        producto = self.productos[codigo]
        producto.retirar(cantidad)
            
def main ():
    inventario = Inventario()
    codigo_producto = input("Ingrese el código del producto a retirar: ")
    try:
        cantidad = int(input("Ingrese la cantidad a retirar: "))
        inventario.retirar_producto(codigo_producto, cantidad)
        if cantidad <= inventario.productos[codigo_producto].stock:
            print(f"La cantidad de {cantidad} unidades del producto '{codigo_producto}' fue retirada exitosamente.")

    except ValueError:
        print("Error: La cantidad ingresada no es un número válido.")

    except ErrorInventario as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()


