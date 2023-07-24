from food import Food
from drink import Drink

food1 = Food('Roti Lapis', 5, 330)
food2 = Food('Kue Coklat', 4, 450)
food3 = Food('Kue Sus', 2, 180)

foods = [food1, food2, food3]

drink1 = Drink('Kopi', 3, 180)
drink2 = Drink('Jus Jeruk', 2, 350)
drink3 = Drink('Espresso', 3, 30)

drinks = [drink1, drink2, drink3]

print('Makanan')
index = 0
for food in foods:
    print(str(index+1) + '. ' + food.info())
    index += 1

print('Minuman')
index = 0
for drink in drinks:
    print(str(index+1) + '. ' + drink.info())
    index += 1

print('--------------------')

food_order = int(input('Masukkan nomor makanan: '))
selected_food = foods[food_order-1]

drink_order = int(input('Masukkan nomor minuman: '))
selected_drink = drinks[drink_order-1]


count = int(input('Mau berapa paket makanan? (Diskon 10% untuk 3 atau lebih): '))


result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)


print('Total harga adalah $' + str(result))
