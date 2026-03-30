# Nama File : Latihan2.1.Oprator.py
# Deskripsi : Program utuk menghitung Energi Kinetik berdasarkan input yuser

# 1. Mengabil input dari yuser 
# Menggunakan float agar yuser bisa memasukkan angka desimal (seprti 2.5)
massa = float(input("Masukkan massa benda (kg): "))
kecepatan = float(input("Masukkan kecepatan benda (m/s): "))

# 2. Mengimplementasikan Rumus Energi Kinetik: Ek = 1/2 * m * v^2
# Operator yang digunakan: 
# * untuk perkalian
# ** untuk perpangkatan (v pangkat 2)
# /  untuk pembagian (1/2 atau 0.5)
energi_kinetik = 0.5 * massa * (kecepatan ** 2)

# 3. Menampilkan hasil perhitungan 
print("\n--- Hasil Perhitungan ---")
print(f"Massa benda     : {massa} kg")
print(f"Kecepatan benda : {kecepatan} m/s")
print(f"Energi Kinetik  : {energi_kinetik} joule")
