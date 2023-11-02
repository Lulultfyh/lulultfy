import tkinter as tk
import math

def hitung_volume():
    alas = float(alas_entry.get())
    tinggi = float(tinggi_entry.get())
    volume = (alas * alas * tinggi) / 3
    hasil_volume.set(f"Volume Limas Segi Empat: {volume:.2f}")

def hitung_luas_permukaan():
    alas = float(alas_entry.get())
    tinggi = float(tinggi_entry.get())
    luas_permukaan = (alas * alas) + 4 * (alas * tinggi) / 2
    hasil_luas_permukaan.set(f"Luas Permukaan Limas Segi Empat: {luas_permukaan:.2f}")

app = tk.Tk()
app.title("Aplikasi Limas Segi Empat")

alas_label = tk.Label(app, text="Panjang Sisi Alas:")
alas_label.pack()

alas_entry = tk.Entry(app)
alas_entry.pack()

tinggi_label = tk.Label(app, text="Tinggi Limas:")
tinggi_label.pack()

tinggi_entry = tk.Entry(app)
tinggi_entry.pack()

hitung_volume_button = tk.Button(app, text="Hitung Volume", command=hitung_volume)
hitung_volume_button.pack()

hitung_luas_permukaan_button = tk.Button(app, text="Hitung Luas Permukaan", command=hitung_luas_permukaan)
hitung_luas_permukaan_button.pack()

hasil_volume = tk.StringVar()
hasil_volume_label = tk.Label(app, textvariable=hasil_volume)
hasil_volume_label.pack()

hasil_luas_permukaan = tk.StringVar()
hasil_luas_permukaan_label = tk.Label(app, textvariable=hasil_luas_permukaan)
hasil_luas_permukaan_label.pack()

app.mainloop()
