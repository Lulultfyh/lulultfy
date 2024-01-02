import tkinter as tk

class KonversiSuhuApp:
    def __init__(self, master):
        self.master = master
        master.title("Konversi Suhu Fahrenheit")

        # Membuat label dan entry untuk input Fahrenheit
        self.label_fahrenheit = tk.Label(master, text="Masukkan Suhu Fahrenheit:")
        self.label_fahrenheit.pack()

        self.entry_fahrenheit = tk.Entry(master)
        self.entry_fahrenheit.pack()

        # Membuat tombol konversi
        self.tombol_konversi = tk.Button(master, text="Konversi", command=self.konversi_suhu)
        self.tombol_konversi.pack()

        # Membuat label untuk menampilkan hasil konversi ke Celsius
        self.label_celsius = tk.Label(master, text="")
        self.label_celsius.pack()

        # Membuat label untuk menampilkan hasil konversi ke Reamur
        self.label_reamur = tk.Label(master, text="")
        self.label_reamur.pack()

        # Membuat label untuk menampilkan hasil konversi ke Kelvin
        self.label_kelvin = tk.Label(master, text="")
        self.label_kelvin.pack()

    def konversi_suhu(self):
        fahrenheit = self.entry_fahrenheit.get()

        try:
            fahrenheit = float(fahrenheit)
            
            # Konversi ke Celsius
            celsius = (5/9) * (fahrenheit - 32)
            self.label_celsius.config(text=f"Hasil Konversi ke Celsius: {celsius:.2f} Celsius")
            
            # Konversi ke Reamur
            reamur = (4/9) * (fahrenheit - 32)
            self.label_reamur.config(text=f"Hasil Konversi ke Reamur: {reamur:.2f} Reamur")
            
            # Konversi ke Kelvin
            kelvin = (5/9) * (fahrenheit - 32) + 273.15
            self.label_kelvin.config(text=f"Hasil Konversi ke Kelvin: {kelvin:.2f} Kelvin")
            
        except ValueError:
            self.label_celsius.config(text="Masukkan suhu dalam angka")

if __name__ == "__main__":
    root = tk.Tk()
    app = KonversiSuhuApp(root)
    root.mainloop()
