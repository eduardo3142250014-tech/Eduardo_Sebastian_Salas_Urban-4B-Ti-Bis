from inventory import *

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
