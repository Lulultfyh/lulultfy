def hitung_ukuran_celana(berat_badan, bentuk_tubuh):
    if bentuk_tubuh == "langsing":
        ukuran_celana = berat_badan * 2
    elif bentuk_tubuh == "berisi":
        ukuran_celana = berat_badan * 1.5
    else:
        ukuran_celana = berat_badan

    return ukuran_celana

berat_badan = float(input("Masukkan berat badan Anda (kg): "))
bentuk_tubuh = input("Masukkan bentuk tubuh Anda (langsing/berisi/lainnya): ")

ukuran_celana = hitung_ukuran_celana(berat_badan, bentuk_tubuh)
print(f"Ukuran celana Anda adalah {ukuran_celana}")
