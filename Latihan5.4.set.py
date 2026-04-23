# Deskripsi: Set akan otomatis membuang data yang duplikat/kembar.

# Kita sengaja memasukkan angka 2 dan 3 berkali-kali
angka = {1, 2, 2, 3, 3, 3}

# Coba lihat hasilnya, yang kembar akan otomatis dibuang oleh Set
print("Isi set angka:", angka)

# Operasi 1: Menambah angka baru
angka.add(4)
print("Setelah ditambah angka 4:", angka)

# Operasi 2: Menghapus angka 1
angka.remove(1)
print("Setelah angka 1 dihapus:", angka)
