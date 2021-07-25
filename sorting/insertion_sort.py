def insertion_sort(data):
    # Lakukan perulangan array (for) dari 1 sampai banyak data
    for i in range(1, len(data)):
        key = data[i]
        # Jika kita mendapatkan nilai yang lebih kecil dari key,
        # maka kita berhenti di indeks itu
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        # Kita akan menempatkan key pada indeks itu
        data[j + 1] = key
        # Print the process
        print("Perulangan ke {}\t: ".format(i), end="")
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
insertion_sort(data)

# Hasil/Output
print("=" * 45)
print("Hasil pengurutan menggunakan Insertion Sort:")
print(data)
print("=" * 45)
