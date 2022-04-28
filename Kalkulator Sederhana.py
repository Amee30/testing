def tambah (x, y):
    return x + y

def kurang (x, y):
    return x - y

def bagi (x, y):
    return x / y

def kali (x, y):
    return x * y

while True:
    print("=" * 25)
    print("Selamat Datang Di Kalkulator Sederhana")
    print("Silahkan Pilih Operasi Bilangan Berikut")
    print("\nMenu Operasi:\n1. Penjumlahan\n2. Pengurangan\n3. Pembagian\n4. Perkalian\n5. Tutup Kalkulator")
    operasi =int(input("Masukan Operasi Yang Di Inginkan (Dalam Bentuk Angka): "))
    if operasi == 1:
        x = int(input("Masukan Angka Pertama: "))
        y = int(input("Masukan Angka Kedua: "))
        print("Hasilnya =  {}".format(tambah(x, y)))
    elif operasi == 2:
        x = int(input("Masukan Angka Pertama: "))
        y = int(input("Masukan Angka Kedua: "))
        print("Hasilnya =  {}".format(kurang(x, y)))
    elif operasi == 3:
        x = int(input("Masukan Angka Pertama: "))
        y = int(input("Masukan Angka Kedua: "))
        print("Hasilnya =  {}".format(bagi(x, y)))
    elif operasi == 4:
        x = int(input("Masukan Angka Pertama: "))
        y = int(input("Masukan Angka Kedua: "))
        print("Hasilnya =  {}".format(kali(x, y)))
    elif operasi == 5:
        print("Menutup Kalkulator, Have A Nice Day :)")
        print("=" * 25)
        break
    else:
        print("Operasi Tidak Tersedia, Menutup Kalkulator")
        print("=" * 25)
        break
    

#Di Buat Tanggal 11 November 2021 :)
#By Ame
#Code Copy Dari Google Benernya Tapi Saya Edit Dikit wkkwkwk