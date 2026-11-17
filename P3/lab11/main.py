from inventory import *
from products import *
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
