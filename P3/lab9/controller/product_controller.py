from exporters import CSVExporter, TXTExporter, JSONExporter, PDFExporter

class ProductController:

    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

        self.exportadores = {
            "CSV": CSVExporter,
            "TXT": TXTExporter,
            "JSON": JSONExporter,
            "PDF": PDFExporter
        }

        self.vista.btn_exportar.config(
            command=lambda: self.generate_report(self.vista.obtener_formato())
        )

        productos = self.modelo.obtener_productos()
        if productos is not None:
            self.vista.mostrar_productos(productos)

    def generate_report(self, formato):
        productos = self.modelo.obtener_productos()

        if productos is None:
            self.vista.mostrar_mensaje(
                "Error",
                "No fue posible obtener los productos. "
                "Verifica la conexión con MySQL.",
                "error"
            )
            return

        ruta = self.vista.pedir_ruta(formato)

        if not ruta:
            return

        exportador = self.exportadores[formato]()

        try:
            exportador.export(productos, ruta)
            self.vista.mostrar_mensaje(
                "Exportación exitosa",
                f"Archivo {formato} generado correctamente."
            )
        except Exception as error:
            self.vista.mostrar_mensaje(
                "Error",
                f"No fue posible generar el archivo: {error}",
                "error"
            )
