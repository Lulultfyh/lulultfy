import tkinter as tk

class KonversiSuhuReamurApp:
    def __init__(self, master):
        self.master = master
        master.title("Konversi Suhu Reamur")

        # Membuat label dan entry untuk input Reamur
        self.label_reamur = tk.Label(master, text="Masukkan Suhu Reamur:")
        self.label_reamur.pack()

        self.entry_reamur = tk.Entry(master)
        self.entry_reamur.pack()

        # Membuat tombol konversi
        self.tombol_konversi = tk.Button(master, text="Konversi", command=self.konversi_suhu)
        self.tombol_konversi.pack()

        # Membuat label untuk menampilkan hasil konversi ke Celsius
        self.label_celsius = tk.Label(master, text="")
        self.label_celsius.pack()

        # Membuat label untuk menampilkan hasil konversi ke Fahrenheit
        self.label_fahrenheit = tk.Label(master, text="")
        self.label_fahrenheit.pack()

        # Membuat label untuk menampilkan hasil konversi ke Kelvin
        self.label_kelvin = tk.Label(master, text="")
        self.label_kelvin.pack()

    def konversi_suhu(self):
        reamur = self.entry_reamur.get()

        try:
            reamur = float(reamur)

            # Membuat objek KonversiSuhuReamur dan melakukan konversi
            konversi_suhu = KonversiSuhuReamur(reamur)

            # Menampilkan hasil konversi ke Celsius
            self.label_celsius.config(text=f"Hasil Konversi ke Celsius: {konversi_suhu.ke_celsius():.2f} Celsius")

            # Menampilkan hasil konversi ke Fahrenheit
            self.label_fahrenheit.config(text=f"Hasil Konversi ke Fahrenheit: {konversi_suhu.ke_fahrenheit():.2f} Fahrenheit")

            # Menampilkan hasil konversi ke Kelvin
            self.label_kelvin.config(text=f"Hasil Konversi ke Kelvin: {konversi_suhu.ke_kelvin():.2f} Kelvin")

        except ValueError:
            self.label_celsius.config(text="Masukkan suhu dalam angka")

class KonversiSuhuReamur:
    def __init__(self, reamur):
        self.reamur = reamur

    def ke_celsius(self):
        return (5/4) * self.reamur

    def ke_fahrenheit(self):
        return (9/4) * self.reamur + 32

    def ke_kelvin(self):
        return (5/4) * self.reamur + 273

if __name__ == "__main__":
    root = tk.Tk()
    app = KonversiSuhuReamurApp(root)
    root.mainloop()
