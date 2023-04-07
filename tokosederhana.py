ask = input("Selamat Datang di Toko Kami, Apakah Anda ingin melakukan pembelian?(Y/N) ")
while ask == 'Y':
    money = int(input('Masukkan uang yang Anda miliki : '))
    items = {'apel': 2, 'pisang': 4, 'jeruk': 6}
    for item_name in items:
        print('--------------------------------------------------')
        print('Anda memiliki ' + str(money) + ' dolar di dompet Anda')
        print('Harga setiap ' + item_name + ' ' + str(items[item_name]) + ' dolar')
        input_count = int(input('Mau berapa '+item_name+'?: '))
        print('Anda akan membeli '+str(input_count)+' '+item_name)
        total_price = input_count * items[item_name]
        print('Harga total adalah '+str(total_price))
        if money > total_price:
            print('Anda telah membeli ' + str(input_count) + ' ' + item_name)
            money -= total_price
        elif money == total_price:
            print('Anda telah membeli ' + str(input_count) + ' ' + item_name)
            print('Uang Anda pas')
        else:
            print('Uang Anda tidak mencukupi')
            print('Anda tidak dapat membeli ' + str(item_name) + ' sebanyak itu')
    print('Uang Anda tersisa '+ str(money) +' dolar')
    ask = input('Apakah Anda ingin melakukan ini kembali?(Y/N) ')
if ask == 'N' :
    print("Terima Kasih, Sampai Jumpa Kembali!")
elif ask != "N" and ask != "Y" :
    print("Inputan Anda Salah!")

