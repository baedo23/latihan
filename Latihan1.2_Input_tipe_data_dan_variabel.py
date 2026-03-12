

#baris atas berisi variable  input data yang berfungsi sebagai inputan dari sebuah data yang ingin dipanggil
barang = str(input("masukkan nama barang : ")) # meminta input nama barang (string)
berat = int(input("masukkan berat : "))  # meminta input nama barang (interger)
tinggi = float(input("masukkan tinggi barang : ")) # meminta input nama barang (float)
normal = bool(input("apakah kondisi barang baik? : ")) # meminta input nama barang (boolean)

#Baris bawah berisi output atau keluaran dari sebuah data yang dipanggil
print ("Nama barang :", barang )
print ("Berat barang :", berat, "gram")
print ("tinggi barang :", tinggi, "mm")
print ("Kondisi barang ?", normal)