from menu_item import MenuItem

menu_item1 = MenuItem('Roti Lapis', 5)
menu_item2 = MenuItem('Kue Coklat', 4)
menu_item3 = MenuItem('Kopi', 3)
menu_item4 = MenuItem('Jus Jeruk', 2)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

for index, menu_item in enumerate(menu_items):
    print(f'{str(index)}. {menu_item.info()}')
print('--------------------')

order = int(input('Masukkan nomor menu: '))
selected_menu = menu_items[order]
print(f'Item yang di pilih: {selected_menu.name}')

count =  int(input('Jumlah pesanan (diskon 10% untuk 3 atau lebih): '))

result = selected_menu.get_total_price(count)

print(f'Total harga adalah ${str(result)}')
