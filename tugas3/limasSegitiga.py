import tkinter as tk
import math

def hitung_volume():
    alas = float(alas_entry.get())
    tinggi = float(tinggi_entry.get())
    volume = (alas * tinggi) / 3
    hasil_volume.set(f"Volume Limas Segitiga: {volume:.2f}")

app = tk.Tk()
app.title("Aplikasi Limas Segitiga")

alas_label = tk.Label(app, text="Panjang Alas Segitiga:")
alas_label.pack()

alas_entry = tk.Entry(app)
alas_entry.pack()

tinggi_label = tk.Label(app, text="Tinggi Limas:")
tinggi_label.pack()

tinggi_entry = tk.Entry(app)
tinggi_entry.pack()

hitung_volume_button = tk.Button(app, text="Hitung Volume", command=hitung_volume)
hitung_volume_button.pack()

hasil_volume = tk.StringVar()
hasil_volume_label = tk.Label(app, textvariable=hasil_volume)
hasil_volume_label.pack()

app.mainloop()
