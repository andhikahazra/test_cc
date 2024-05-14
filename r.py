import math
from pywebio.input import input
from pywebio.output import put_text, put_markdown, popup
from pywebio.platform.flask import webio_view
from flask import Flask
from pywebio import start_server

def hitung_cc(diameter_piston, stroke_piston, jumlah_silinder):
    pi = math.pi
    volume_silinder = pi * (diameter_piston / 2) ** 2 * stroke_piston
    kapasitas_mesin = (volume_silinder / 1000) * jumlah_silinder
    return kapasitas_mesin

def main():
    put_text("Raadi Engginering - UNS - Program Menghitung Kapasitas Mesin Motor")

    history = []  # To store calculation history

    while True:
        try:
            # Ask user to input piston diameter (in mm)
            diameter_piston_str = input("Masukkan diameter piston (mm): ")
            diameter_piston = float(diameter_piston_str)
            # Ask user to input piston stroke (in mm)
            stroke_piston_str = input("Masukkan stroke piston (mm): ")
            stroke_piston = float(stroke_piston_str)
            # Ask user to input number of cylinders
            jumlah_silinder_str = input("Masukkan jumlah silinder: ")
            jumlah_silinder = int(jumlah_silinder_str)

            # Calculate engine displacement
            kapasitas = hitung_cc(diameter_piston, stroke_piston, jumlah_silinder)
            
            # Display calculation result in a popup
            with popup("Kapasitas Mesin"):
                put_text("Kapasitas mesin adalah: %.2f cc" % kapasitas)

            # Add the calculation result to history
            history.append((diameter_piston, stroke_piston, jumlah_silinder, kapasitas))

        except ValueError:
            put_text("\nInput tidak valid. Pastikan Anda memasukkan angka.\n")
        
        # Ask user if they want to calculate again
        ulangi = input("\nApakah ingin menghitung lagi? (y/n): ")
        if ulangi.lower() != 'y':
            put_text("Terima kasih telah menggunakan program ini.")
            break

    # Display calculation history
    put_markdown("### Histori Penghitungan:")
    markdown_content = "| No | Diameter Piston (mm) | Stroke Piston (mm) | Jumlah Silinder | Kapasitas Mesin (cc) |\n"
    markdown_content += "|----|-----------------------|----------------------|------------------|-----------------------|\n"
    for idx, (diameter, stroke, silinder, kapasitas) in enumerate(history, 1):
        markdown_content += f"| {idx} | {diameter} | {stroke} | {silinder} | {kapasitas} |\n"
    put_markdown(markdown_content)

# Define Flask application
app = Flask(__name__)

# Register main function as a PyWebIO web application using Flask
app.add_url_rule('/pywebio', 'webio_view', webio_view(main), methods=['GET', 'POST'])

if __name__ == '__main__':
    start_server(main, port=8080)  # Changed port to 8080, you can choose any available port above 1024
    
