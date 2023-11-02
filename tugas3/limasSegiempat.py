import tkinter as tk

def hitung_volume_limas():
    try:
        panjang_sisi = float(entry_sisi.get())
        tinggi_limas = float(entry_tinggi.get())
        volume = (1/3) * (panjang_sisi ** 2) * tinggi_limas
        result_label.config(text=f"Volume Limas: {volume:.2f} unit kubik")
    except ValueError:
        result_label.config(text="Masukkan angka yang valid!")

app = tk.Tk()
app.title("Kalkulator Volume Limas Segiempat")

sisi_label = tk.Label(app, text="Panjang Sisi Alas:")
sisi_label.pack()
entry_sisi = tk.Entry(app)
entry_sisi.pack()

tinggi_label = tk.Label(app, text="Tinggi Limas:")
tinggi_label.pack()
entry_tinggi = tk.Entry(app)
entry_tinggi.pack()

hitung_button = tk.Button(app, text="Hitung Volume", command=hitung_volume_limas)
hitung_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
