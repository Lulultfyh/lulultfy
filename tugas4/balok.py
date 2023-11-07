import tkinter as tk

def hitung_volume():
    panjang = float(panjang_entry.get())
    lebar = float(lebar_entry.get())
    tinggi = float(tinggi_entry.get())
    volume = panjang * lebar * tinggi
    hasil_volume.set(f"Volume: {volume:.2f}")

def hitung_luas_permukaan():
    panjang = float(panjang_entry.get())
    lebar = float(lebar_entry.get())
    tinggi = float(tinggi_entry.get())
    luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    hasil_luas_permukaan.set(f"Luas Permukaan: {luas_permukaan:.2f}")

app = tk.Tk()
app.title("Aplikasi Balok")

panjang_label = tk.Label(app, text="Panjang:")
panjang_label.pack()

panjang_entry = tk.Entry(app)
panjang_entry.pack()

lebar_label = tk.Label(app, text="Lebar:")
lebar_label.pack()

lebar_entry = tk.Entry(app)
lebar_entry.pack()

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
