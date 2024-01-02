print("Konversi Suhu reamur")

# Entry
suhu = input("Masukkan suhu dalam Reamur:")

# rumus
F = (9/4 * float(suhu)) + 32
C = (5/4 * float(suhu)) 
K = 5/4 * float(suhu) + 273

#output
print(suhu + " celcius sama dengan ")
print(str(F) + " Fahrenheit")
print(str(C) + " celcius")
print(str(K) + " Kelvin")