import mysql.connector
from controller.connection import Conexion

class ProductModel:

    def __init__(self):
        self.conexion_db = Conexion()

    def obtener_productos(self):
        conexion = self.conexion_db.conectar()

        if conexion is None:
            return None

        cursor = None

        try:
            cursor = conexion.cursor()

            consulta = """
                SELECT id, nombre, precio, stock
                FROM productos
            """

            cursor.execute(consulta)
            return cursor.fetchall()

        except mysql.connector.Error as error:
            print("Error al obtener productos:", error)
            return None

        finally:
            if cursor is not None:
                cursor.close()
            conexion.close()
