import tkinter as tk
import math

# Fungsi untuk menghitung volume limas segitiga
def hitung():
    alas = float(entry_alas.get())
    tinggi_alas = float(entry_tinggi_alas.get())
    tinggi_limas = float(entry_tinggi_limas.get())

    volume = (1/3) * (1/2 * alas * tinggi_alas) * tinggi_limas
    hasil_volume.config(text=f"Volume: {volume:.2f} satuan kubik")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Limas Segitiga")

# Membuat label dan input fields untuk alas, tinggi alas, dan tinggi limas segitiga
label_alas = tk.Label(root, text="Alas segitiga:")
label_tinggi_alas = tk.Label(root, text="Tinggi alas:")
label_tinggi_limas = tk.Label(root, text="Tinggi limas:")

entry_alas = tk.Entry(root)
entry_tinggi_alas = tk.Entry(root)
entry_tinggi_limas = tk.Entry(root)

label_alas.grid(row=0, column=0)
label_tinggi_alas.grid(row=1, column=0)
label_tinggi_limas.grid(row=2, column=0)

entry_alas.grid(row=0, column=1)
entry_tinggi_alas.grid(row=1, column=1)
entry_tinggi_limas.grid(row=2, column=1)

# Tombol untuk menghitung
hitung_button = tk.Button(root, text="Hitung", command=hitung)
hitung_button.grid(row=3, columnspan=2)

# Hasil perhitungan
hasil_volume = tk.Label(root, text="")

hasil_volume.grid(row=4, columnspan=2)

# Menjalankan aplikasi
root.mainloop()
