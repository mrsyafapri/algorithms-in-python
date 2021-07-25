def selection_sort(data):
    # Lakukan perulangan array (for) sebanyak data yang ada dikurangi 1
    for i in range(len(data) - 1):
        # Atur array index ke i sebagai lokasi/angka minimum
        # Temukan (cari) angka terkecil di dalam array (data) yang belum diurutkan
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        # Tukar (swap) angka terkecil yang ditemukan ke lokasi/angka minimum
        # Atur angka selanjutnya (sebelah kanannya) sebagai lokasi/angka minimum
        data[i], data[min_idx] = data[min_idx], data[i]
        # Print the process
        print("Perulangan ke {}\t: ".format(i + 1), end="")
        print_array(data)


def print_array(data):
    for i in range(len(data)):
        print(data[i], end=" ")
    print()


# Input
data = []
print("Masukkan 10 bilangan yang ingin diurutkan")
for i in range(10):
    data.append(int(input("Masukkan Angka bilangan ke {}: ".format(i + 1))))

# Proses
selection_sort(data)

# Hasil/Output
print("=" * 45)
print("Hasil pengurutan menggunakan Selection Sort:")
print(data)
print("=" * 45)
