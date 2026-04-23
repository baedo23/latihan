# Deskripsi: Tuple isinya dikunci/permanen. Tidak bisa ditambah atau dibuang.

lampu_lalin = ("Merah", "Kuning", "Hijau")
print("Warna lampu lalu lintas:", lampu_lalin)

# Operasi 1: Kita cuma bisa melihat isinya. Misalnya melihat warna kedua (indeks 1)
print("Warna urutan kedua adalah:", lampu_lalin[1])

# Operasi 2: Menghitung ada berapa kata "Merah" di dalam tuple tersebut
jumlah_merah = lampu_lalin.count("Merah")
print("Jumlah warna merah ada:", jumlah_merah)

# Catatan: Kita tidak bisa memakai lampu_lalin.append("Biru") karena akan error!
