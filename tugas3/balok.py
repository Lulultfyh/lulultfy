import tkinter as tk

# Fungsi untuk menghitung volume dan luas permukaan balok
def hitung():
    panjang = float(entry_panjang.get())
    lebar = float(entry_lebar.get())
    tinggi = float(entry_tinggi.get())

    volume = panjang * lebar * tinggi
    luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

    hasil_volume.config(text=f"Volume: {volume:.2f} satuan kubik")
    hasil_luas_permukaan.config(text=f"Luas Permukaan: {luas_permukaan:.2f} satuan persegi")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Balok")

# Membuat label dan input fields untuk panjang, lebar, dan tinggi balok
label_panjang = tk.Label(root, text="Panjang:")
label_lebar = tk.Label(root, text="Lebar:")
label_tinggi = tk.Label(root, text="Tinggi:")

entry_panjang = tk.Entry(root)
entry_lebar = tk.Entry(root)
entry_tinggi = tk.Entry(root)

label_panjang.grid(row=0, column=0)
label_lebar.grid(row=1, column=0)
label_tinggi.grid(row=2, column=0)

entry_panjang.grid(row=0, column=1)
entry_lebar.grid(row=1, column=1)
entry_tinggi.grid(row=2, column=1)

# Tombol untuk menghitung
hitung_button = tk.Button(root, text="Hitung", command=hitung)
hitung_button.grid(row=3, columnspan=2)

# Hasil perhitungan
hasil_volume = tk.Label(root, text="")
hasil_luas_permukaan = tk.Label(root, text="")

hasil_volume.grid(row=4, columnspan=2)
hasil_luas_permukaan.grid(row=5, columnspan=2)

# Menjalankan aplikasi
root.mainloop()
