import tkinter as tk
import math

def hitung_volume():
    jari_jari = float(jari_jari_entry.get())
    tinggi = float(tinggi_entry.get())
    volume = math.pi * jari_jari ** 2 * tinggi
    hasil_volume.set(f"Volume Tabung: {volume:.2f}")

def hitung_luas_permukaan():
    jari_jari = float(jari_jari_entry.get())
    tinggi = float(tinggi_entry.get())
    luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    hasil_luas_permukaan.set(f"Luas Permukaan Tabung: {luas_permukaan:.2f}")

app = tk.Tk()
app.title("Aplikasi Tabung")

jari_jari_label = tk.Label(app, text="Jari-Jari:")
jari_jari_label.pack()

jari_jari_entry = tk.Entry(app)
jari_jari_entry.pack()

tinggi_label = tk.Label(app, text="Tinggi:")
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
