def sequential_search(data, key):
    # Lakukan perulangan array (for) sebanyak data yang ada
    for i in range(len(data)):
        # Jika angka yang dicari (key) ditemukan (sama dengan) pada data index ke i (data[i])
        if data[i] == key:
            # Kembalikan nilai index-nya
            return i
    # Jika angka yang dicari (key) tidak ditemukan di dalam array (data),
    # Kembalikan nilai index -1 (-1 bukan index array, artinya data tidak ditemukan)
    return -1


# Input
data = []
print("Masukkan 10 bilangan")
for i in range(10):
    data.append(int(input("Masukkan Angka index ke {}: ".format(i))))
key = int(input("Masukkan Angka Yang Ingin Dicari: "))

# Proses
result = sequential_search(data, key)

# Hasil/Output
print("=" * 45)
print("Hasil pencarian menggunakan Sequential Search:")
if result == -1:
    # Jika fungsi mengembalikan nilai -1
    # Tampilkan pesan bahwa data tidak ditemukan (-1 bukan index array, artinya data tidak ditemukan)
    print("Angka {} tidak terdapat pada array".format(key))
else:
    # Jika fungsi mengembalikan nilai >= 0
    # Tampilkan pesan bahwa data ditemukan pada index ke i (result)
    print("Angka {} terdapat pada array index ke {}".format(key, result))
print("=" * 45)
