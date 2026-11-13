import tkinter as tk
from tkinter import messagebox

class RegisterView:

    def __init__(self, root):
        self.ventana = tk.Toplevel(root)
        self.ventana.title("Registro de usuarios")
        self.ventana.geometry("440x500")
        self.ventana.configure(bg="#F8FAFC")
        self.ventana.resizable(False, False)

        self.ventana.transient(root)
        self.ventana.grab_set()

        self.titulo = tk.Label(
            self.ventana,
            text="Crear Cuenta",
            font=("Segoe UI", 20, "bold"),
            bg="#F8FAFC",
            fg="#0F172A"
        )
        self.titulo.pack(pady=20)

        self.lbl_nombre = tk.Label(
            self.ventana,
            text="Nombre completo",
            font=("Segoe UI", 10, "bold"),
            bg="#F8FAFC",
            fg="#475569"
        )
        self.lbl_nombre.pack(anchor="w", padx=45)

        self.entry_nombre = tk.Entry(
            self.ventana,
            width=36,
            font=("Segoe UI", 11),
            relief="solid",
            bd=1
        )
        self.entry_nombre.pack(pady=4)

        self.lbl_username = tk.Label(
            self.ventana,
            text="Usuario",
            font=("Segoe UI", 10, "bold"),
            bg="#F8FAFC",
            fg="#475569"
        )
        self.lbl_username.pack(anchor="w", padx=45)

        self.entry_username = tk.Entry(
            self.ventana,
            width=36,
            font=("Segoe UI", 11),
            relief="solid",
            bd=1
        )
        self.entry_username.pack(pady=4)

        self.lbl_password = tk.Label(
            self.ventana,
            text="Contraseña",
            font=("Segoe UI", 10, "bold"),
            bg="#F8FAFC",
            fg="#475569"
        )
        self.lbl_password.pack(anchor="w", padx=45)

        self.entry_password = tk.Entry(
            self.ventana,
            width=36,
            font=("Segoe UI", 11),
            show="*",
            relief="solid",
            bd=1
        )
        self.entry_password.pack(pady=4)

        self.lbl_confirmar = tk.Label(
            self.ventana,
            text="Confirmar contraseña",
            font=("Segoe UI", 10, "bold"),
            bg="#F8FAFC",
            fg="#475569"
        )
        self.lbl_confirmar.pack(anchor="w", padx=45)

        self.entry_confirmar = tk.Entry(
            self.ventana,
            width=36,
            font=("Segoe UI", 11),
            show="*",
            relief="solid",
            bd=1
        )
        self.entry_confirmar.pack(pady=4)

        self.btn_guardar = tk.Button(
            self.ventana,
            text="Registrar usuario",
            width=22,
            bg="#2563EB",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            bd=0,
            cursor="hand2"
        )
        self.btn_guardar.pack(pady=15)

        self.btn_cancelar = tk.Button(
            self.ventana,
            text="Cancelar",
            width=22,
            bg="#E2E8F0",
            fg="#1E293B",
            font=("Segoe UI", 10, "bold"),
            bd=0,
            command=self.cerrar,
            cursor="hand2"
        )
        self.btn_cancelar.pack()

        self.entry_nombre.focus_set()

    def obtener_datos(self):
        nombre = self.entry_nombre.get().strip()
        username = self.entry_username.get().strip()
        password = self.entry_password.get()
        confirmar = self.entry_confirmar.get()
        return nombre, username, password, confirmar

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje, parent=self.ventana)
        else:
            messagebox.showinfo(titulo, mensaje, parent=self.ventana)

    def cerrar(self):
        self.ventana.destroy()