# # Challenge 1: Letter Index Disctionary

# my_dict = {}
# my_string = input(f"Please enter a string:\n")

# for index, letter in enumerate(my_string):
#     if letter not in my_dict.keys():
#         my_dict[letter] = [index]
#     else:
#         my_dict[letter].append(index)

# print(my_dict)

# Challenge 2: Affordable Items

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$10"
my_amount = int(wallet.replace('$',''))
result = []

for item in items_purchase.keys():
    clean_price = int(items_purchase[item].replace("$","").replace(",",""))
    items_purchase[item] = clean_price 
    if my_amount > clean_price:
        result.append(item)
        my_amount -= clean_price
print(sorted(result))