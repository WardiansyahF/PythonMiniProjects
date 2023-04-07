#fungsi untuk menambah data
def tambahData(dataNama,dataNpm,dataKelas):
    nama.append(dataNama)
    npm.append(dataNpm)
    kelas.append(dataKelas)
    
#fungsi untuk mengubah data
def ubahData(dataKe,dataNama,dataNpm,dataKelas):
    nama[dataKe-1] = dataNama
    npm[dataKe-1] = dataNpm
    kelas[dataKe-1] = dataKelas

#fungsi untuk menghapus data
def hapusData(datake):
    nama.remove(nama[datake-1])
    npm.remove(npm[datake-1])
    kelas.remove(kelas[datake-1])

#fungsi utama
def main():
    #variable untuk menampung data
    global nama, npm, kelas
    nama = []
    npm = []
    kelas = []

    tanya = input("SELAMAT DATANG DI PROGRAM DATA MAHASISWA\nAPAKAH ANDA INGIN MELAKUKAN OLAH DATA?(Y/N) ")
    print("==================================")
    print("===== PROGRAM DATA MAHASISWA =====")
    print("==================================")
    while tanya == 'Y':
        print("PILIH PROGRAM YANG INGIN DIJALANKAN\n1. Tambah Data\n2. Ubah Data\n3. Hapus Data\n4. Tampilkan Data")
        kode = int(input("Masukkan Kode Program(1/2/3/4): "))
        
        if kode == 1 :
            dataNama = input("Masukkan Nama mahasiswa: ")
            dataNpm = input("Masukkan NPM mahasiswa: ")
            dataKelas = input("Masukkan Kelas mahasiswa: ")
            tambahData(dataNama,dataNpm,dataKelas)
        elif kode == 2:
            panjang = len(nama)
            if panjang == 0:
                print("Tidak ada data yang ditemukan")
            else:
                for i in range(panjang):
                    print(str(i+1)+". Nama  :",nama[i],"\n   NPM   :",npm[i],"\n   Kelas :",kelas[i])
                dataKe = int(input("Data ke-berapa yang ingin Anda ubah? "))
                dataNama = input("Masukkan perubahan Nama mahasiswa: ")
                dataNpm = input("Masukkan perubahan NPM mahasiswa: ")
                dataKelas = input("Masukkan perubahan Kelas mahasiswa: ")
                ubahData(dataKe,dataNama,dataNpm,dataKelas)
        elif kode == 3:
            panjang = len(nama)
            if panjang == 0:
                print("Tidak ada data yang ditemukan")
            else:
                for i in range(panjang):
                    print(str(i+1)+". Nama  :",nama[i],"\n   NPM   :",npm[i],"\n   Kelas :",kelas[i])   
                dataKe = int(input("Data ke-berapa yang ingin Anda Hapus? "))
                hapusData(dataKe)
        elif kode == 4:
            panjang = len(nama)
            for i in range(panjang):
                print(str(i+1)+". Nama  :",nama[i],"\n   NPM   :",npm[i],"\n   Kelas :",kelas[i])
        else:
            print("INPUT ANDA SALAH SILAHKAN ULANGI KEMBALI!")
            
        
        tanya = input("APAKAH ANDA INGIN MELAKUKAN INI KEMBALI?(Y/N) ")
    
    if tanya == 'N':
        print("======================================")
        print("======= PROGRAM DATA MAHASISWA =======")
        print("======================================")
        print("               TERIMAKASIH\n           SAMPAI JUMPA KEMBALI!")
        quit()
    elif tanya != 'Y' and tanya != 'N':
        print("INPUT SALAH SILAHKAN ULANGI KEMBALI!")
        quit()
        

     

main()