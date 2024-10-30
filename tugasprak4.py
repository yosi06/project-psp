# Fungsi enkripsi sederhana
def enkripsi_pesan(data_awal, key):
    hasil = ""  # Variabel untuk menyimpan hasil enkripsi
    for huruf in data_awal:
        # Mengubah huruf ke kode ASCII, menambahkan kunci, lalu kembali ke huruf
        angka_ascii = ord(huruf)  # Mendapatkan nilai ASCII dari huruf
        angka_baru = angka_ascii + key  # Menambahkan nilai key ke ASCII
        if angka_baru > ord('z'):  # Jika lebih dari 'z', kembali ke 'a'
            angka_baru = ord('a') + (angka_baru - ord('z') - 1)  # Perhitungan untuk kembali ke 'a'
        huruf_baru = chr(angka_baru)  # Mengubah kembali ke huruf
        hasil += huruf_baru  # Menambahkan huruf baru ke hasil
    return hasil
print(hasil_1)  # Output: fnaqv
print(hasil_2)  # Output: wtztg