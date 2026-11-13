import mysql.connector
from controller.connection import Conexion

class UserModel:

    def __init__(self):
        self.conexion_db = Conexion()

    def registrar_usuario(self, nombre, username, password):
        conexion = self.conexion_db.conectar()

        if conexion is None:
            return "error"

        cursor = None

        try:
            cursor = conexion.cursor()

            
            consulta = """
                INSERT INTO users (username, passw, nombre)
                VALUES (%s, %s, %s)
            """

            cursor.execute(consulta, (username, password, nombre))
            conexion.commit()

            return "ok"

        except mysql.connector.IntegrityError:
            return "duplicado"

        except mysql.connector.Error as error:
            print("Error al registrar usuario:", error)
            return "error"

        finally:
            if cursor is not None:
                cursor.close()
            conexion.close()

    def validar_usuario(self, username, password):
        conexion = self.conexion_db.conectar()

        if conexion is None:
            return None

        cursor = None

        try:
            cursor = conexion.cursor()

            
            consulta = """
                SELECT id_user, nombre
                FROM users
                WHERE username = %s AND passw = %s
            """

            cursor.execute(consulta, (username, password))
            usuario = cursor.fetchone()

            return usuario

        except mysql.connector.Error as error:
            print("Error al validar usuario:", error)
            return None

        finally:
            if cursor is not None:
                cursor.close()
            conexion.close()

    def cerrar(self):
        pass