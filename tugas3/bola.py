import tkinter as tk

def calculate_volume_length():
    length = float(length_entry.get())
    width = float(width_entry.get())
    height = float(height_entry.get())
    volume = length * width * height
    result_label.config(text=f"Volume: {volume:.2f} cubic units")

def calculate_surface_area():
    length = float(length_entry.get())
    width = float(width_entry.get())
    height = float(height_entry.get())
    surface_area = 2 * (length * width + length * height + width * height)
    result_label.config(text=f"Surface Area: {surface_area:.2f} square units")

# Membuat jendela utama
root = tk.Tk()
root.title("Balok Calculator")

# Label dan entry untuk panjang
length_label = tk.Label(root, text="Panjang:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Label dan entry untuk lebar
width_label = tk.Label(root, text="Lebar:")
width_label.pack()
width_entry = tk.Entry(root)
width_entry.pack()

# Label dan entry untuk tinggi
height_label = tk.Label(root, text="Tinggi:")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

# Tombol untuk menghitung volume dan luas permukaan
calculate_volume_button = tk.Button(root, text="Hitung Volume", command=calculate_volume_length)
calculate_volume_button.pack()
calculate_surface_area_button = tk.Button(root, text="Hitung Luas Permukaan", command=calculate_surface_area)
calculate_surface_area_button.pack()

# Label untuk menampilkan hasil perhitungan
result_label = tk.Label(root, text="")
result_label.pack()

# Menjalankan aplikasi
root.mainloop()
