import tkinter as tk

def konversi_suhu():
    fahrenheit = entry_fahrenheit.get()

    try:
        fahrenheit = float(fahrenheit)
        
        # Konversi ke Celsius
        celsius = (5/9) * (fahrenheit - 32)
        label_celsius.config(text=f"Hasil Konversi ke Celsius: {celsius:.2f} Celsius")
        
        # Konversi ke Reamur
        reamur = (4/9) * (fahrenheit - 32)
        label_reamur.config(text=f"Hasil Konversi ke Reamur: {reamur:.2f} Reamur")
        
        # Konversi ke Kelvin
        kelvin = (5/9) * (fahrenheit - 32) + 273.15
        label.kelvin.config(text=f"Hasil Konversi ke Kelvin: {kelvin:.2f} Kelvin")
        
    except ValueError:
        label_hasil.config(text="Masukkan suhu dalam angka")

# Membuat jendela utama
app = tk.Tk()
app.title("Konversi Suhu Fahrenheit")

# Membuat label dan entry untuk input Fahrenheit
label_fahrenheit = tk.Label(app, text="Masukkan Suhu Fahrenheit:")
label_fahrenheit.pack()

entry_fahrenheit = tk.Entry(app)
entry_fahrenheit.pack()

# Membuat tombol konversi
tombol_konversi = tk.Button(app, text="Konversi", command=konversi_suhu)
tombol_konversi.pack()

# Membuat label untuk menampilkan hasil konversi ke Celsius
label_celsius = tk.Label(app, text="")
label_celsius.pack()

# Membuat label untuk menampilkan hasil konversi ke Reamur
label_reamur = tk.Label(app, text="")
label_reamur.pack()

# Membuat label untuk menampilkan hasil konversi ke Kelvin
label_kelvin = tk.Label(app, text="")
label_kelvin.pack()

# Memulai loop utama aplikasi
app.mainloop()
