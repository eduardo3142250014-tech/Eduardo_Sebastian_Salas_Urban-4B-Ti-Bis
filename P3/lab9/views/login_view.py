import tkinter as tk
from tkinter import messagebox

class LoginView:

    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de acceso")
        self.root.geometry("440x380")
        self.root.configure(bg="#F8FAFC")
        self.root.resizable(False, False)

        self.titulo = tk.Label(
            root,
            text="Iniciar Sesión",
            font=("Segoe UI", 20, "bold"),
            bg="#F8FAFC",
            fg="#0F172A"
        )
        self.titulo.pack(pady=25)

        self.lbl_username = tk.Label(
            root,
            text="Usuario",
            font=("Segoe UI", 10, "bold"),
            bg="#F8FAFC",
            fg="#475569"
        )
        self.lbl_username.pack(anchor="w", padx=45)

        self.entry_username = tk.Entry(
            root,
            width=36,
            font=("Segoe UI", 11),
            relief="solid",
            bd=1
        )
        self.entry_username.pack(pady=6)

        self.lbl_password = tk.Label(
            root,
            text="Contraseña",
            font=("Segoe UI", 10, "bold"),
            bg="#F8FAFC",
            fg="#475569"
        )
        self.lbl_password.pack(anchor="w", padx=45)

        self.entry_password = tk.Entry(
            root,
            width=36,
            font=("Segoe UI", 11),
            show="*",
            relief="solid",
            bd=1
        )
        self.entry_password.pack(pady=6)

        self.btn_login = tk.Button(
            root,
            text="Ingresar",
            width=22,
            bg="#2563EB",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            bd=0,
            cursor="hand2"
        )
        self.btn_login.pack(pady=15)

        self.btn_register = tk.Button(
            root,
            text="Crear cuenta nueva",
            width=22,
            bg="#E2E8F0",
            fg="#1E293B",
            font=("Segoe UI", 10, "bold"),
            bd=0,
            cursor="hand2"
        )
        self.btn_register.pack()

    def obtener_datos(self):
        username = self.entry_username.get().strip()
        password = self.entry_password.get()
        return username, password

    def limpiar_campos(self):
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje, parent=self.root)
        else:
            messagebox.showinfo(titulo, mensaje, parent=self.root)