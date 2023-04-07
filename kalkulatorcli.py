def hitung(x,y,pilih) :
    if pilih == 1 :
        hasil = x + y
        return print(f'{x} + {y} = {hasil}')
    elif pilih == 2 :
        hasil = x-y
        return print(f'{x} - {y} = {hasil}')
    elif pilih == 3 :
        hasil = x*y
        return print(f'{x} x {y} = {hasil}')
    elif pilih == 4 :
        hasil = x/y
        return print(f'{x} : {y} = {hasil}')
    else :
        return 'Input anda salah, silahkan input sesuai pilihan'
print('Pilih Operasi.\n1. Jumlah\n2. Kurang\n3. Kali\n4. Bagi')
pilih = int(input('Masukkan pilihan(1/2/3/4): '))
x = int(input('Masukkan bilangan pertama: '))
y = int(input('Masukkan bilangan kedua: '))
hitung(x,y,pilih)