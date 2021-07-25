def binary_search(data, key, batas_atas, batas_bawah):
    # Lakukan perulangan (while) selama batas atas kecil atau sama dengan (<=) batas bawah
    while batas_atas <= batas_bawah:
        tengah = (batas_bawah + batas_atas) // 2
        if data[tengah] == key:
            # Jika angka yang dicari (key) ditemukan (sama dengan) pada data index ke tengah (data[tengah])
            # Kembalikan nilai index-nya (tengah)
            return tengah
        elif data[tengah] > key:
            # Jika data index ke tengah (data[tengah]) lebih besar dari (>) angka yang dicari (key)
            # Cari di bagian kiri array (batasBawah = tengah - 1)
            batas_bawah = tengah - 1
        elif data[tengah] < key:
            # Jika data index ke tengah (data[tengah]) lebih kecil dari (<) angka yang dicari (key)
            # Cari di bagian kanan array (batasAtas = tengah + 1)
            batas_atas = tengah + 1
    # Jika angka yang dicari (key) tidak ditemukan di dalam array (data)
    # Kembalikan nilai index -1 (-1 bukan index array, artinya data tidak ditemukan)
    return -1


# Input
data = []
print("Masukkan 10 bilangan (harus terurut)")
for i in range(10):
    data.append(int(input("Masukkan Angka index ke {}: ".format(i))))
key = int(input("Masukkan Angka Yang Ingin Dicari: "))
batas_atas = 0
batas_bawah = len(data) - 1

# Proses
result = binary_search(data, key, batas_atas, batas_bawah)

# Hasil/Output
print("=" * 45)
print("Hasil pencarian menggunakan Binary Search:")
if result == -1:
    # Jika fungsi mengembalikan nilai -1
    # Tampilkan pesan bahwa data tidak ditemukan (-1 bukan index array, artinya data tidak ditemukan)
    print("Angka {} tidak terdapat pada array".format(key))
else:
    # Jika fungsi mengembalikan nilai >= 0
    # Tampilkan pesan bahwa data ditemukan pada index ke i (result)
    print("Angka {} terdapat pada array index ke {}".format(key, result))
print("=" * 45)
