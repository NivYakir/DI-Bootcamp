# Challenge 1: Letter Index Disctionary

my_dict = {}
my_string = input(f"Please enter a string:\n")

for index, letter in enumerate(my_string):
    if letter not in my_dict.keys():
        my_dict[letter] = [index]
    else:
        my_dict[letter].append(index)

print(my_dict)

# Challenge 2: Affordable Items

items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet = "$100"
my_money = int(wallet.replace('$',''))
result = []
for key, value in items_purchase.items():
    new_price = int(value.replace("$","").replace(",",""))
    items_purchase[key] = new_price
    if my_money >  new_price:
        result.append(key)
    else:
        continue

print(sorted(result))