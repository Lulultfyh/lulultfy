print ( "Konversi Suhu reamur" )
def get_fahrenheit(suhu):
    F = (9/4 * float(suhu)) + 32
    return F

def get_celcius(suhu):
    c = (5/4 * float(suhu)) 
    return C 

def get_kelvin(suhu):
    K = 5/4 * float(suhu) + 273
    return K

# Entry
suhu = input("Masukkan suhu dalam Reamur:")

# rumus
F = get_fahrenheit(suhu)
C = get_celcius(suhu)
K = get_kelvin(suhu)

#output
print(suhu + " reamur sama dengan ")
print(str(F) + " Fahrenheit")
print(str(C) + " celcius ")
print(str(K) + " Kelvin")