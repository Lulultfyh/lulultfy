import tkinter as tk
import math

def hitung_volume_tabung():
    try:
        jari_jari = float(entry_jari_jari.get())
        tinggi = float(entry_tinggi.get())
        volume = math.pi * jari_jari**2 * tinggi
        result_label.config(text=f"Volume Tabung: {volume:.2f} unit kubik")
    except ValueError:
        result_label.config(text="Masukkan angka yang valid!")

app = tk.Tk()
app.title("Kalkulator Volume Tabung")

jari_jari_label = tk.Label(app, text="Jari-Jari Tabung:")
jari_jari_label.pack()
entry_jari_jari = tk.Entry(app)
entry_jari_jari.pack()

tinggi_label = tk.Label(app, text="Tinggi Tabung:")
tinggi_label.pack()
entry_tinggi = tk.Entry(app)
entry_tinggi.pack()

hitung_button = tk.Button(app, text="Hitung Volume", command=hitung_volume_tabung)
hitung_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
