# Meminta input jumlah bilangan dari pengguna
n = int(input("Masukkan jumlah bilangan: "))
total = 0

# Meminta input bilangan dari pengguna dan menghitung jumlahnya
for i in range(n):
    bil = int(input(f"Masukkan bilangan ke-{i+1}: "))
    total += bil  # Menambahkan bilangan ke total

# Menghitung rata-rata
rata_rata = total / n

# Menampilkan hasil rata-rata
print(f"Rata-rata bilangan adalah: {rata_rata:.2f}")