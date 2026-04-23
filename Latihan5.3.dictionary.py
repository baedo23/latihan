# Deskripsi: Dictionary menyimpan data berpasangan seperti buku kontak.

kontak = {
    "Andi": "0812345",
    "Budi": "0898765"
}
print("Kontak awal:", kontak)

# Operasi 1: Memanggil nomor HP si Budi
print("Nomor HP Budi adalah:", kontak["Budi"])

# Operasi 2: Menambahkan kontak teman baru (Citra)
kontak["Citra"] = "0855555"
print("Setelah Citra ditambahkan:", kontak)

# Operasi 3: Mengubah nomor HP Andi karena dia ganti nomor
kontak["Andi"] = "0811111"
print("Setelah nomor Andi diubah:", kontak)
