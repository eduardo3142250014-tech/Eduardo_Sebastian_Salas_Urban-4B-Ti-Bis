import tkinter as tk
from views.register_view import RegisterView
from views.product_view import ProductView
from models.product_model import ProductModel
from controller.product_controller import ProductController

class Authentication:

    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.vista_registro = None

        self.vista.btn_login.config(
            command=self.iniciar_sesion
        )

        self.vista.btn_register.config(
            command=self.abrir_registro
        )

        self.vista.root.protocol(
            "WM_DELETE_WINDOW",
            self.cerrar_aplicacion
        )

    def iniciar_sesion(self):
        username, password = self.vista.obtener_datos()

        if not username or not password:
            self.vista.mostrar_mensaje(
                "Campos vacíos",
                "Ingresa el usuario y la contraseña.",
                "error"
            )
            return

        usuario = self.modelo.validar_usuario(username, password)

        if usuario is not None:
            id_usuario, nombre = usuario

            self.vista.mostrar_mensaje(
                "Acceso correcto",
                f"Bienvenido, {nombre}."
            )

            self.vista.limpiar_campos()

            self.controlador_productos = ProductController(
                ProductModel(),
                ProductView(self.vista.root)
            )

        else:
            self.vista.mostrar_mensaje(
                "Acceso denegado",
                "Usuario o contraseña incorrectos.",
                "error"
            )

    def abrir_registro(self):
        if (
            self.vista_registro is not None
            and self.vista_registro.ventana.winfo_exists()
        ):
            self.vista_registro.ventana.lift()
            self.vista_registro.ventana.focus_force()
            return

        self.vista_registro = RegisterView(self.vista.root)

        self.vista_registro.btn_guardar.config(
            command=self.registrar_usuario
        )

        self.vista_registro.ventana.protocol(
            "WM_DELETE_WINDOW",
            self.cerrar_registro
        )

    def registrar_usuario(self):
        nombre, username, password, confirmar = (
            self.vista_registro.obtener_datos()
        )

        if not nombre or not username or not password or not confirmar:
            self.vista_registro.mostrar_mensaje(
                "Campos vacíos",
                "Todos los campos son obligatorios.",
                "error"
            )
            return

        if password != confirmar:
            self.vista_registro.mostrar_mensaje(
                "Contraseñas diferentes",
                "Las contraseñas no coinciden.",
                "error"
            )
            return

        resultado = self.modelo.registrar_usuario(
            nombre,
            username,
            password
        )

        if resultado == "ok":
            self.vista_registro.mostrar_mensaje(
                "Registro exitoso",
                "El usuario se registró correctamente."
            )

            self.cerrar_registro()

            self.vista.entry_username.delete(0, tk.END)
            self.vista.entry_username.insert(0, username)

        elif resultado == "duplicado":
            self.vista_registro.mostrar_mensaje(
                "Usuario existente",
                "Ya existe una cuenta con ese usuario.",
                "error"
            )

        else:
            self.vista_registro.mostrar_mensaje(
                "Error",
                "No fue posible registrar el usuario. "
                "Verifica la conexión con MySQL.",
                "error"
            )

    def cerrar_registro(self):
        if self.vista_registro is not None:
            if self.vista_registro.ventana.winfo_exists():
                self.vista_registro.cerrar()

            self.vista_registro = None

    def cerrar_aplicacion(self):
        self.cerrar_registro()
        self.modelo.cerrar()
        self.vista.root.destroy()