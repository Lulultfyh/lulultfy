import tkinter as tk
from tkinter import Canvas

# Fungsi untuk menggambar kubus
def draw_cube():
    canvas.delete("all")
    
    # Koordinat titik sudut kubus
    x0, y0 = 100, 100
    x1, y1 = 200, 100
    x2, y2 = 200, 200
    x3, y3 = 100, 200
    x4, y4 = 150, 50
    x5, y5 = 250, 150

    # Menggambar garis-garis kubus
    canvas.create_line(x0, y0, x1, y1)
    canvas.create_line(x1, y1, x2, y2)
    canvas.create_line(x2, y2, x3, y3)
    canvas.create_line(x3, y3, x0, y0)
    canvas.create_line(x0, y0, x4, y4)
    canvas.create_line(x1, y1, x5, y5)
    canvas.create_line(x2, y2, x5, y5)
    canvas.create_line(x3, y3, x4, y4)

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Kubus")

# Membuat canvas untuk menggambar kubus
canvas = Canvas(root, width=300, height=300)
canvas.pack()

# Tombol untuk menggambar kubus
draw_button = tk.Button(root, text="Gambar Kubus", command=draw_cube)
draw_button.pack()

# Menjalankan aplikasi
root.mainloop()
