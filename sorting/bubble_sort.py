def bubble_sort(data):
    # Lakukan perulangan array (for) sebanyak data yang ada dikurangi 1
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            isTheOrderCorrect = data[j] < data[j + 1]
            if not isTheOrderCorrect:
                # Jika angka sekarang (data[j]) lebih besar dari (>) angka berikutnya (data[j + 1])
                # Kedua elemen tersebut di tukar (swap)
                data[j], data[j + 1] = data[j + 1], data[j]
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
bubble_sort(data)

# Hasil/Output
print("=" * 45)
print("Hasil pengurutan menggunakan Bubble Sort:")
print(data)
print("=" * 45)
