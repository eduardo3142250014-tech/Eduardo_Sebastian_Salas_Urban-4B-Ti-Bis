import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class ProductView:

    def __init__(self, root):
        self.ventana = tk.Toplevel(root)
        self.ventana.title("Productos")
        self.ventana.geometry("560x420")
        self.ventana.configure(bg="#F8FAFC")

        self.titulo = tk.Label(
            self.ventana,
            text="Inventario de Productos",
            font=("Segoe UI", 16, "bold"),
            bg="#F8FAFC",
            fg="#0F172A"
        )
        self.titulo.pack(pady=15)

        # Panel de controles de exportación
        self.panel = tk.Frame(self.ventana, bg="#F8FAFC")
        self.panel.pack(pady=5)

        self.combo_formato = ttk.Combobox(
            self.panel,
            values=["CSV", "TXT", "JSON", "PDF"],
            state="readonly",
            width=10
        )
        self.combo_formato.current(0)
        self.combo_formato.pack(side="left", padx=5)

        self.btn_exportar = tk.Button(
            self.panel,
            text="Exportar Reporte",
            bg="#2563EB",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            bd=0,
            cursor="hand2"
        )
        self.btn_exportar.pack(side="left", padx=5)

        # Tabla de productos
        self.tabla = ttk.Treeview(
            self.ventana,
            columns=("id", "nombre", "precio", "stock"),
            show="headings"
        )
        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("precio", text="Precio")
        self.tabla.heading("stock", text="Stock")
        self.tabla.column("id", width=50, anchor="center")
        self.tabla.column("nombre", width=250)
        self.tabla.column("precio", width=100, anchor="e")
        self.tabla.column("stock", width=70, anchor="center")
        self.tabla.pack(fill="both", expand=True, padx=20, pady=15)

    def mostrar_productos(self, productos):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for producto in productos:
            self.tabla.insert("", "end", values=producto)

    def obtener_formato(self):
        return self.combo_formato.get()

    def pedir_ruta(self, formato):
        extension = formato.lower()
        return filedialog.asksaveasfilename(
            parent=self.ventana,
            title="Guardar reporte",
            defaultextension=f".{extension}",
            initialfile=f"reporte_productos.{extension}",
            filetypes=[(formato, f"*.{extension}")]
        )

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje, parent=self.ventana)
        else:
            messagebox.showinfo(titulo, mensaje, parent=self.ventana)
