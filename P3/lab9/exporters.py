import csv
import json
from fpdf import FPDF


class Exporter:
    def export(self, data, file_path):
        """Base method to be overridden by subclasses"""
        raise NotImplementedError("This method must be implemented by the subclass.")


class CSVExporter(Exporter):
    def export(self, data, file_path):
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nombre", "Precio", "Stock"])
            for product in data:
                writer.writerow([product[0], product[1], product[2], product[3]])
        print(f"CSV file generated at: {file_path}")


class TXTExporter(Exporter):
    def export(self, data, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("--- REPORTE DE PRODUCTOS ---\n")
            for product in data:
                file.write(f"ID: {product[0]} | Nombre: {product[1]} | Precio: ${product[2]} | Stock: {product[3]}\n")
        print(f"TXT file generated at: {file_path}")


class JSONExporter(Exporter):
    def export(self, data, file_path):
        products = []
        for product in data:
            products.append({
                "id": product[0],
                "nombre": product[1],
                "precio": float(product[2]),
                "stock": product[3]
            })
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(products, file, indent=4, ensure_ascii=False)
        print(f"JSON file generated at: {file_path}")


class PDFExporter(Exporter):
    def export(self, data, file_path):
        pdf = FPDF()
        pdf.add_page()

        # Title configuration
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="Reporte de Inventario de Productos", ln=True, align='C')

        # Line break
        pdf.ln(10)

        # Body configuration
        pdf.set_font("Arial", size=12)

        for product in data:
            line_text = f"Producto: {product[1]} - Precio: ${product[2]} - Stock: {product[3]}"
            pdf.cell(200, 10, txt=line_text, ln=True)

        pdf.output(file_path)
        print(f"PDF file generated at: {file_path}")
