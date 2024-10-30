def hitung_faktorial(n):
    #Menghitung faktorial 
    faktorial = 1  # Variabel faktorial
    for i in range(1, n + 1):  # Loop dari 1 sampai n
        faktorial *= i  # Kalikan dengan i
    return faktorial  # Mengembalikan hasil faktorial

def tampilkan_hasil(bilangan, faktorial):
    #Menampilkan hasil faktorial
    print(f"Faktorial dari {bilangan} adalah {faktorial}.")

def main():
    #Fungsi utama 
    bilangan = int(input("Masukkan bilangan bulat non-negatif: "))  # Input dari pengguna
    
    if bilangan < 0:  # Cek jika bilangan negatif
        print("Bilangan yang dimasukan bukan bilangan bulat non-negatif.")
    else:
        # Memanggil fungsi 
        faktorial = hitung_faktorial(bilangan)
        
        # Memanggil prosedur 
        tampilkan_hasil(bilangan, faktorial)

# Memanggil fungsi main
main()