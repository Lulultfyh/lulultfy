import tkinter as tk

def hitung_volume_prisma():
    try:
        alas = float(entry_alas.get())
        tinggi_alas = float(entry_tinggi_alas.get())
        tinggi_prisma = float(entry_tinggi_prisma.get())
        volume = alas * tinggi_alas * tinggi_prisma
        result_label.config(text=f"Volume Prisma: {volume:.2f} unit kubik")
    except ValueError:
        result_label.config(text="Masukkan angka yang valid!")

app = tk.Tk()
app.title("Kalkulator Volume Prisma Segitiga")

alas_label = tk.Label(app, text="Panjang Alas Segitiga:")
alas_label.pack()
entry_alas = tk.Entry(app)
entry_alas.pack()

tinggi_alas_label = tk.Label(app, text="Tinggi Alas Segitiga:")
tinggi_alas_label.pack()
entry_tinggi_alas = tk.Entry(app)
entry_tinggi_alas.pack()

tinggi_prisma_label = tk.Label(app, text="Tinggi Prisma:")
tinggi_prisma_label.pack()
entry_tinggi_prisma = tk.Entry(app)
entry_tinggi_prisma.pack()

hitung_button = tk.Button(app, text="Hitung Volume", command=hitung_volume_prisma)
hitung_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
