import tkinter as tk

def hitung_volume():
    sisi = float(sisi_entry.get())
    volume = sisi ** 3
    hasil_volume.set(f"Volume: {volume}")

def hitung_luas_permukaan():
    sisi = float(sisi_entry.get())
    luas_permukaan = 6 * sisi ** 2
    hasil_luas_permukaan.set(f"Luas Permukaan: {luas_permukaan}")

app = tk.Tk()
app.title("Aplikasi Kubus")

sisi_label = tk.Label(app, text="Panjang Sisi:")
sisi_label.pack()

sisi_entry = tk.Entry(app)
sisi_entry.pack()

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
